import os

lines=['<!DOCTYPE html>',' <html>','\n','     <head>     <link href=\"prism.css\" rel="stylesheet"> <script type="text/javascript-lazy"  >  	var admobid = {}; if( /(android)/i.test(navigator.userAgent) ) {     admobid = {            banner: \'ca-app-pub-5170973579111533/1085713519\',        interstitial: \'ca-app-pub-5830283354936773/1902239267\'     }; } else if(/(ipod|iphone|ipad)/i.test(navigator.userAgent)) {     admobid = {            banner: \'ca-app-pub-6869992474017983/4806197152\',         interstitial: \'ca-app-pub-6869992474017983/7563979554\'    }; } else {     admobid = {              banner: \'ca-app-pub-6869992474017983/8878394753\',         interstitial: \'ca-app-pub-6869992474017983/1355127956\'     }; } if(( /(ipad|iphone|ipod|android|windows phone)/i.test(navigator.userAgent) )) {     document.addEventListener(\'deviceready\', initApp, false); } else {     initApp(); }  function initApp() {     if (! AdMob ) { alert( \'admob plugin not ready\' ); return; }       AdMob.createBanner( {         adId: admobid.banner,         isTesting: false,         overlap: false,         offsetTopBar: false,         position: AdMob.AD_POSITION.BOTTOM_CENTER,         bgColor: \'black\'     } );      AdMob.prepareInterstitial({         adId: admobid.interstitial,         autoShow: true     }); }    </script></head>','\n'    ,' <body style="background-color:white;" >'   '\n'  ,'<div class="topcoat-navigation-bar" ng-controller="HomeCtrl">'  ,'\n'  ,' <div class="topcoat-navigation-bar__item left quarter">'   ,'\n'     ,'<a class="topcoat-icon-button--quiet" ng-click="slidePage(\'/\',\'modal\')">'  ,'\n' , '<span class="topcoat-icon home-icon"></span></a></div><div class="topcoat-navigation-bar__item center half"><h1 class="topcoat-navigation-bar__title">Cake</h1></div></div><script type="text/javascript" src="prism.js"></script><pre  ng-prism  class="language-python"><code>',  ' \n  ']

directory = '/sdcard/Numpy'

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if  filename.endswith(".py"): 
        print(os.path.join(directory, filename))
        path=os.path.join(directory,filename)
        with open(path+'.html','w+''') as f3,open(path) as f1:
           f3.writelines(lines)
           f3.write(f1.read().strip())
           f3.write('\n')
           f3.write('</code></pre></body></html>    ')
