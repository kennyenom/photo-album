const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    
    //Toggle Nav
    burger.addEventListener('click', ()=>{
      nav.classList.toggle('nav-active');
     
      
      //Animate Links
      navLinks.forEach((link, index)=>{
        if(link.style.animation){
          link.style.animation = ''
          
        }else{
              link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
              
        }
      });
      
      //burger animation
      burger.classList.toggle('toggle');
      
      
      
    });
    
    
    
    
  }
  
  navSlide();
  

//
const scrolltop = document.querySelector('.scrollTotop');
scrolltop.addEventListener('click',()=>{
  window.scrolltop({top:0});

});

window.addEventListener('scroll',() =>{
  window.pageYOffset>20
  ?(scrolltop.style.display = 'block')
  :(scrolltop.style.display='none');
})

// Scroll Reveal Animations
const sr = ScrollReveal({
  origin: "top",
  distance: "80px",
  duration: 2000,
  reset: false,
});

sr.reveal(
  `.list-group-item,
  .jeyy,
  .navbar,
  .hero,
  .services,
  .deals,
  .recent__products,
  .recent__posts,
  .newsletter,
  footer`,
  {
    interval: 500,
  }
);