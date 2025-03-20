        // Sélectionne l'élément de l'input de mot de passe et l'icône
        const passwordField = document.getElementById('password');
        const togglePassword = document.getElementById('toggle-password');

        // Ajoute un événement de clic sur l'icône
        togglePassword.addEventListener('click', function() {
            // Si le type du champ est "password", on le change en "text" pour afficher le mot de passe
            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                togglePassword.classList.remove('fa-eye');
                togglePassword.classList.add('fa-eye-slash');
            } else {
                // Sinon, on revient au type "password" pour masquer le mot de passe
                passwordField.type = 'password';
                togglePassword.classList.remove('fa-eye-slash');
                togglePassword.classList.add('fa-eye');
            }
        });