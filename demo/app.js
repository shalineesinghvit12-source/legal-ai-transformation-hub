const tabs=[...document.querySelectorAll('.tab')];
const panels=[...document.querySelectorAll('.panel')];

function showPanel(id){
  tabs.forEach(tab=>tab.classList.toggle('active',tab.dataset.panel===id));
  panels.forEach(panel=>panel.classList.toggle('active',panel.id===id));
  window.scrollTo({top:0,behavior:'smooth'});
}

tabs.forEach(tab=>tab.addEventListener('click',()=>showPanel(tab.dataset.panel)));
document.querySelectorAll('.next').forEach(button=>button.addEventListener('click',()=>showPanel(button.dataset.next)));
document.getElementById('restart').addEventListener('click',()=>showPanel('intake'));

