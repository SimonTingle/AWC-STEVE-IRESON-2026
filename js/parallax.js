(function(){
  if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  var els=[].slice.call(document.querySelectorAll('[data-parallax]'));
  if(!els.length)return;
  var items=els.map(function(w){return{w:w,img:w.querySelector('img'),vis:false,s:parseFloat(w.getAttribute('data-speed'))||0.12}}).filter(function(i){return i.img});
  var mq=matchMedia('(max-width:900px)'),ticking=false;
  function update(){
    ticking=false;
    var vh=window.innerHeight,k=mq.matches?0.5:1;
    items.forEach(function(it){
      if(!it.vis)return;
      var r=it.w.getBoundingClientRect(),h=it.img.offsetHeight;
      var max=Math.max(0,(h-r.height)/2-1);
      var y=((r.top+r.height/2)-vh/2)*it.s*k;
      y=Math.max(-max,Math.min(max,y));
      it.img.style.transform='translate3d(0,'+y.toFixed(2)+'px,0)';
    });
  }
  function req(){if(!ticking){ticking=true;requestAnimationFrame(update)}}
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){items.forEach(function(it){if(it.w===e.target)it.vis=e.isIntersecting})});
      req();
    },{rootMargin:'100px 0px'});
    items.forEach(function(it){io.observe(it.w)});
  }else items.forEach(function(it){it.vis=true});
  addEventListener('scroll',req,{passive:true});
  addEventListener('resize',req);
  req();
})();
