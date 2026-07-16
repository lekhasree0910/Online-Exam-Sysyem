// NexExam Global JavaScript Controller

document.addEventListener('DOMContentLoaded', () => {
    setupNavbar();
    bindFormSubmissions();
    loadFeaturedExams();
});

// 1. Setup Navbar based on Logged-in State
function setupNavbar() {
    const user = JSON.parse(localStorage.getItem('currentUser'));
    const navLinks = document.getElementById('nav-links');
    const navActions = document.getElementById('user-nav-action');

    if (!navLinks) return; // not on standard pages with nav

    // Clear dynamic links
    const linksToRemove = navLinks.querySelectorAll('.dynamic-nav-link');
    linksToRemove.forEach(el => el.remove());

    if (user) {
        // Logged in
        if (user.role === 'student') {
            // Student link to Dashboard
            const li = document.createElement('li');
            li.className = 'dynamic-nav-link';
            li.innerHTML = `<a href="student_dashboard.html" class="nav-link"><i class="fa-solid fa-gauge"></i> Dashboard</a>`;
            navLinks.appendChild(li);
        } else if (user.role === 'admin') {
            // Admin link to Dashboard
            const li = document.createElement('li');
            li.className = 'dynamic-nav-link';
            li.innerHTML = `<a href="admin_dashboard.html" class="nav-link"><i class="fa-solid fa-user-shield"></i> Admin Panel</a>`;
            navLinks.appendChild(li);
        }

        // Action panel with Profile and Logout
        if (navActions) {
            navActions.innerHTML = `
                <div class="user-profile-nav">
                    <div style="text-align: right; line-height: 1.2;">
                        <div style="font-weight: 700; font-size: 0.9rem;">${user.full_name}</div>
                        <div style="font-size: 0.75rem; color: var(--text-secondary);">${user.role === 'admin' ? 'Administrator' : 'Student'}</div>
                    </div>
                    <div class="avatar-circle" style="${user.role === 'admin' ? 'background: linear-gradient(135deg, var(--accent) 0%, var(--primary) 100%);' : ''}">
                        ${user.full_name.charAt(0)}
                    </div>
                    <button class="nav-btn-outline btn-sm" onclick="logoutUser()" style="padding: 0.5rem 0.8rem;">
                        <i class="fa-solid fa-right-from-bracket"></i>
                    </button>
                </div>
            `;
        }
    } else {
        // Guest
        if (navActions) {
            navActions.innerHTML = `
                <a href="login.html" class="nav-btn-outline"><i class="fa-solid fa-right-to-bracket"></i> Login</a>
                <a href="register.html" class="nav-btn"><i class="fa-solid fa-user-plus"></i> Register</a>
            `;
        }
    }
}

// 2. Logout function
function logoutUser() {
    localStorage.removeItem('currentUser');
    showNotification("Logged out successfully", "info");
    setTimeout(() => {
        window.location.href = 'index.html';
    }, 1000);
}

// 3. Global Notification Toast System
function showNotification(message, type = 'info') {
    const container = document.getElementById('notification-container');
    if (!container) return;

    const notif = document.createElement('div');
    notif.className = `notification ${type}`;

    let icon = '<i class="fa-solid fa-circle-info"></i>';
    if (type === 'success') icon = '<i class="fa-solid fa-circle-check"></i>';
    if (type === 'error') icon = '<i class="fa-solid fa-circle-exclamation"></i>';
    if (type === 'warning') icon = '<i class="fa-solid fa-triangle-exclamation"></i>';

    notif.innerHTML = `${icon} <span>${message}</span>`;
    container.appendChild(notif);

    // Fade out and remove
    setTimeout(() => {
        notif.style.animation = 'slide-in 0.3s reverse forwards';
        setTimeout(() => {
            notif.remove();
        }, 300);
    }, 4000);
}

// 4. Bind Forms Submissions (Login, Register)
function bindFormSubmissions() {
    // Student registration
    const regForm = document.getElementById('register-form');
    if (regForm) {
        regForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const full_name = document.getElementById('reg-name').value;
            const email = document.getElementById('reg-email').value;
            const phone = document.getElementById('reg-phone').value;
            const college = document.getElementById('reg-college').value;
            const password = document.getElementById('reg-password').value;

            try {
                // Post register
                const response = await fetch('/students/add/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ full_name, email, phone, college, password })
                });

                if (!response.ok) {
                    const errors = await response.json();
                    throw new Error(errors.email ? "Email already exists" : "Registration failed. Please check inputs.");
                }

                showNotification("Registration successful! Logging in...", "success");

                // Auto login student
                const loginRes = await fetch('/login/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password, role: 'student' })
                });

                if (loginRes.ok) {
                    const loginData = await loginRes.json();
                    localStorage.setItem('currentUser', JSON.stringify(loginData.user));
                    setTimeout(() => {
                        window.location.href = 'student_dashboard.html';
                    }, 1200);
                } else {
                    setTimeout(() => {
                        window.location.href = 'login.html';
                    }, 1200);
                }

            } catch (err) {
                console.error(err);
                showNotification(err.message, "error");
            }
        });
    }

    // Consolidated Login (Student or Admin)
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const email = document.getElementById('login-email').value;
            const password = document.getElementById('login-password').value;
            const role = currentRole; // Referenced from script on login.html

            try {
                const response = await fetch('/login/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password, role })
                });

                if (!response.ok) {
                    const errData = await response.json();
                    throw new Error(errData.error || "Authentication failed");
                }

                const data = await response.json();
                localStorage.setItem('currentUser', JSON.stringify(data.user));
                
                showNotification(data.message, "success");

                setTimeout(() => {
                    if (role === 'admin') {
                        window.location.href = 'admin_dashboard.html';
                    } else {
                        window.location.href = 'student_dashboard.html';
                    }
                }, 1000);

            } catch (err) {
                console.error(err);
                showNotification(err.message, "error");
            }
        });
    }
}

// 5. Load Featured Exams on Homepage
async function loadFeaturedExams() {
    const briefContainer = document.getElementById('featured-exams-list');
    if (!briefContainer) return; // not homepage

    try {
        const res = await fetch('/exams/');
        if (!res.ok) throw new Error("Failed to load featured exams");
        const exams = await res.json();

        if (exams.length === 0) {
            briefContainer.innerHTML = `
                <div class="card" style="width: 100%; text-align: center; color: var(--text-secondary);">
                    <i class="fa-solid fa-box-open fa-2x"></i>
                    <p style="margin-top: 1rem;">No active examinations listed at the moment.</p>
                </div>
            `;
            return;
        }

        briefContainer.innerHTML = '';
        // Slice top 3 for featured section
        exams.slice(0, 3).forEach(exam => {
            const card = document.createElement('div');
            card.className = 'card exam-card';
            card.innerHTML = `
                <div class="exam-header">
                    <span class="exam-subject">${exam.subject}</span>
                    <span class="exam-date-badge"><i class="fa-regular fa-calendar"></i> ${exam.exam_date}</span>
                </div>
                <h3 class="exam-card-title">${exam.exam_title}</h3>
                <div class="exam-details">
                    <div class="detail-item">
                        <span class="detail-label">Duration</span>
                        <span class="detail-val"><i class="fa-regular fa-clock"></i> ${exam.duration}m</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Total Marks</span>
                        <span class="detail-val"><i class="fa-regular fa-circle-check"></i> ${exam.total_marks} pts</span>
                    </div>
                </div>
                <a href="exams.html" class="nav-btn exam-action" style="text-align: center;">
                    <i class="fa-solid fa-circle-arrow-right"></i> View Details
                </a>
            `;
            briefContainer.appendChild(card);
        });

    } catch (err) {
        console.error(err);
        briefContainer.innerHTML = `
            <div class="card" style="width: 100%; text-align: center; color: var(--danger);">
                <i class="fa-solid fa-circle-exclamation fa-2x"></i>
                <p style="margin-top: 1rem;">Unable to load featured exams. API server offline.</p>
            </div>
        `;
    }
}
