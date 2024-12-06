document.addEventListener('DOMContentLoaded', function() {
    const categorie = document.querySelector('.categorie');
    const sousMenu = document.querySelector('.sous-menu');

    categorie.addEventListener('mouseover', function() {
        sousMenu.style.display = 'block';
    });

    categorie.addEventListener('mouseout', function(event) {
        if (!categorie.contains(event.relatedTarget)) {
            sousMenu.style.display = 'none';
        }
    });

    sousMenu.addEventListener('mouseover', function() {
        sousMenu.style.display = 'block';
    });

    sousMenu.addEventListener('mouseout', function(event) {
        if (!sousMenu.contains(event.relatedTarget)) {
            sousMenu.style.display = 'none';
        }
    });
    
    
});

document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('iconi');
    const menu = document.getElementById('navi');

    menuIcon.addEventListener('click', function() {
        menu.classList.toggle('show'); // Ajouter ou retirer la classe 'show'
    });
});


