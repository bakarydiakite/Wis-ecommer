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

let counter = 0;
Plus.addEventListener('click', () => {
    counter++;
    countElement.textContent = counter;
})
Moins.addEventListener('click', () => {
    counter--;
    countElement.textContent = counter;
})



// prix = document.querySelectorAll('.prix')
//                 vl = document.querySelectorAll('.quantite')
//                 n = 0
//                 s=0
//                 k=0
//                 vl.forEach(Element =>{
//                     n++
//                 })
//                 for (i=0;i<n ; i++){
//                     k = prix[i].textContent
//                     k = parseInt(k)
//                     l= vl[i].value
//                     l = parseInt(l)
//                     s+= k*l
                    
//                 }
//                 total = document.getElementById('total')
//                 total.textContent+=s
//                 s_total = document.querySelectorAll('.s_total')
//                 nbr =0
//                 s_total.forEach(Element =>{
//                     k = prix[nbr].textContent
//                     k = parseInt(k)
//                     l= vl[nbr].value
//                     l = parseInt(l)
//                     prod = k*l
//                     nbr++
//                     Element.textContent = prod
//                 })