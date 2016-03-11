<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />
<title>wrangling-openstreetmap-finalproject</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*//*! normalize.css v3.0.2 | MIT License | git.io/normalize */html{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-size:10px;-webkit-tap-highlight-color:transparent}article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}audio:not([controls]){display:none;height:0}[hidden],template{display:none}a{background-color:transparent}a:active,a:hover{outline:0}abbr[title]{border-bottom:1px dotted}b,optgroup,strong{font-weight:700}dfn{font-style:italic}h1{font-size:2em;margin:.67em 0}mark{background:#ff0;color:#000}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-.5em}sub{bottom:-.25em}img{border:0;vertical-align:middle}svg:not(:root){overflow:hidden}hr{-moz-box-sizing:content-box;box-sizing:content-box;height:0}pre,textarea{overflow:auto}code,kbd,pre,samp{font-size:1em}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0}button{overflow:visible}button,select{text-transform:none}button,html input[type=button],input[type=reset],input[type=submit]{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type=checkbox],input[type=radio]{box-sizing:border-box;padding:0}input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{height:auto}input[type=search]::-webkit-search-cancel-button,input[type=search]::-webkit-search-decoration{-webkit-appearance:none}table{border-collapse:collapse;border-spacing:0}td,th{padding:0}/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */@media print{*,:after,:before{background:0 0!important;color:#000!important;box-shadow:none!important;text-shadow:none!important}a,a:visited{text-decoration:underline}a[href]:after{content:" (" attr(href)")"}abbr[title]:after{content:" (" attr(title)")"}a[href^="javascript:"]:after,a[href^="#"]:after{content:""}blockquote,pre{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}img,tr{page-break-inside:avoid}img{max-width:100%!important}h2,h3,p{orphans:3;widows:3}h2,h3{page-break-after:avoid}select{background:#fff!important}.navbar{display:none}.btn>.caret,.dropup>.btn>.caret{border-top-color:#000!important}.label{border:1px solid #000}.table{border-collapse:collapse!important}.table td,.table th{background-color:#fff!important}.table-bordered td,.table-bordered th{border:1px solid #ddd!important}}@font-face{font-family:'Glyphicons Halflings';src:url(../components/bootstrap/fonts/glyphicons-halflings-regular.eot);src:url(../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix)format('embedded-opentype'),url(../components/bootstrap/fonts/glyphicons-halflings-regular.woff2)format('woff2'),url(../components/bootstrap/fonts/glyphicons-halflings-regular.woff)format('woff'),url(../components/bootstrap/fonts/glyphicons-halflings-regular.ttf)format('truetype'),url(../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular)format('svg')}.glyphicon{position:relative;top:1px;display:inline-block;font-family:'Glyphicons Halflings';font-style:normal;font-weight:400;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.glyphicon-asterisk:before{content:"\2a"}.glyphicon-plus:before{content:"\2b"}.glyphicon-eur:before,.glyphicon-euro:before{content:"\20ac"}.glyphicon-minus:before{content:"\2212"}.glyphicon-cloud:before{content:"\2601"}.glyphicon-envelope:before{content:"\2709"}.glyphicon-pencil:before{content:"\270f"}.glyphicon-glass:before{content:"\e001"}.glyphicon-music:before{content:"\e002"}.glyphicon-search:before{content:"\e003"}.glyphicon-heart:before{content:"\e005"}.glyphicon-star:before{content:"\e006"}.glyphicon-star-empty:before{content:"\e007"}.glyphicon-user:before{content:"\e008"}.glyphicon-film:before{content:"\e009"}.glyphicon-th-large:before{content:"\e010"}.glyphicon-th:before{content:"\e011"}.glyphicon-th-list:before{content:"\e012"}.glyphicon-ok:before{content:"\e013"}.glyphicon-remove:before{content:"\e014"}.glyphicon-zoom-in:before{content:"\e015"}.glyphicon-zoom-out:before{content:"\e016"}.glyphicon-off:before{content:"\e017"}.glyphicon-signal:before{content:"\e018"}.glyphicon-cog:before{content:"\e019"}.glyphicon-trash:before{content:"\e020"}.glyphicon-home:before{content:"\e021"}.glyphicon-file:before{content:"\e022"}.glyphicon-time:before{content:"\e023"}.glyphicon-road:before{content:"\e024"}.glyphicon-download-alt:before{content:"\e025"}.glyphicon-download:before{content:"\e026"}.glyphicon-upload:before{content:"\e027"}.glyphicon-inbox:before{content:"\e028"}.glyphicon-play-circle:before{content:"\e029"}.glyphicon-repeat:before{content:"\e030"}.glyphicon-refresh:before{content:"\e031"}.glyphicon-list-alt:before{content:"\e032"}.glyphicon-lock:before{content:"\e033"}.glyphicon-flag:before{content:"\e034"}.glyphicon-headphones:before{content:"\e035"}.glyphicon-volume-off:before{content:"\e036"}.glyphicon-volume-down:before{content:"\e037"}.glyphicon-volume-up:before{content:"\e038"}.glyphicon-qrcode:before{content:"\e039"}.glyphicon-barcode:before{content:"\e040"}.glyphicon-tag:before{content:"\e041"}.glyphicon-tags:before{content:"\e042"}.glyphicon-book:before{content:"\e043"}.glyphicon-bookmark:before{content:"\e044"}.glyphicon-print:before{content:"\e045"}.glyphicon-camera:before{content:"\e046"}.glyphicon-font:before{content:"\e047"}.glyphicon-bold:before{content:"\e048"}.glyphicon-italic:before{content:"\e049"}.glyphicon-text-height:before{content:"\e050"}.glyphicon-text-width:before{content:"\e051"}.glyphicon-align-left:before{content:"\e052"}.glyphicon-align-center:before{content:"\e053"}.glyphicon-align-right:before{content:"\e054"}.glyphicon-align-justify:before{content:"\e055"}.glyphicon-list:before{content:"\e056"}.glyphicon-indent-left:before{content:"\e057"}.glyphicon-indent-right:before{content:"\e058"}.glyphicon-facetime-video:before{content:"\e059"}.glyphicon-picture:before{content:"\e060"}.glyphicon-map-marker:before{content:"\e062"}.glyphicon-adjust:before{content:"\e063"}.glyphicon-tint:before{content:"\e064"}.glyphicon-edit:before{content:"\e065"}.glyphicon-share:before{content:"\e066"}.glyphicon-check:before{content:"\e067"}.glyphicon-move:before{content:"\e068"}.glyphicon-step-backward:before{content:"\e069"}.glyphicon-fast-backward:before{content:"\e070"}.glyphicon-backward:before{content:"\e071"}.glyphicon-play:before{content:"\e072"}.glyphicon-pause:before{content:"\e073"}.glyphicon-stop:before{content:"\e074"}.glyphicon-forward:before{content:"\e075"}.glyphicon-fast-forward:before{content:"\e076"}.glyphicon-step-forward:before{content:"\e077"}.glyphicon-eject:before{content:"\e078"}.glyphicon-chevron-left:before{content:"\e079"}.glyphicon-chevron-right:before{content:"\e080"}.glyphicon-plus-sign:before{content:"\e081"}.glyphicon-minus-sign:before{content:"\e082"}.glyphicon-remove-sign:before{content:"\e083"}.glyphicon-ok-sign:before{content:"\e084"}.glyphicon-question-sign:before{content:"\e085"}.glyphicon-info-sign:before{content:"\e086"}.glyphicon-screenshot:before{content:"\e087"}.glyphicon-remove-circle:before{content:"\e088"}.glyphicon-ok-circle:before{content:"\e089"}.glyphicon-ban-circle:before{content:"\e090"}.glyphicon-arrow-left:before{content:"\e091"}.glyphicon-arrow-right:before{content:"\e092"}.glyphicon-arrow-up:before{content:"\e093"}.glyphicon-arrow-down:before{content:"\e094"}.glyphicon-share-alt:before{content:"\e095"}.glyphicon-resize-full:before{content:"\e096"}.glyphicon-resize-small:before{content:"\e097"}.glyphicon-exclamation-sign:before{content:"\e101"}.glyphicon-gift:before{content:"\e102"}.glyphicon-leaf:before{content:"\e103"}.glyphicon-fire:before{content:"\e104"}.glyphicon-eye-open:before{content:"\e105"}.glyphicon-eye-close:before{content:"\e106"}.glyphicon-warning-sign:before{content:"\e107"}.glyphicon-plane:before{content:"\e108"}.glyphicon-calendar:before{content:"\e109"}.glyphicon-random:before{content:"\e110"}.glyphicon-comment:before{content:"\e111"}.glyphicon-magnet:before{content:"\e112"}.glyphicon-chevron-up:before{content:"\e113"}.glyphicon-chevron-down:before{content:"\e114"}.glyphicon-retweet:before{content:"\e115"}.glyphicon-shopping-cart:before{content:"\e116"}.glyphicon-folder-close:before{content:"\e117"}.glyphicon-folder-open:before{content:"\e118"}.glyphicon-resize-vertical:before{content:"\e119"}.glyphicon-resize-horizontal:before{content:"\e120"}.glyphicon-hdd:before{content:"\e121"}.glyphicon-bullhorn:before{content:"\e122"}.glyphicon-bell:before{content:"\e123"}.glyphicon-certificate:before{content:"\e124"}.glyphicon-thumbs-up:before{content:"\e125"}.glyphicon-thumbs-down:before{content:"\e126"}.glyphicon-hand-right:before{content:"\e127"}.glyphicon-hand-left:before{content:"\e128"}.glyphicon-hand-up:before{content:"\e129"}.glyphicon-hand-down:before{content:"\e130"}.glyphicon-circle-arrow-right:before{content:"\e131"}.glyphicon-circle-arrow-left:before{content:"\e132"}.glyphicon-circle-arrow-up:before{content:"\e133"}.glyphicon-circle-arrow-down:before{content:"\e134"}.glyphicon-globe:before{content:"\e135"}.glyphicon-wrench:before{content:"\e136"}.glyphicon-tasks:before{content:"\e137"}.glyphicon-filter:before{content:"\e138"}.glyphicon-briefcase:before{content:"\e139"}.glyphicon-fullscreen:before{content:"\e140"}.glyphicon-dashboard:before{content:"\e141"}.glyphicon-paperclip:before{content:"\e142"}.glyphicon-heart-empty:before{content:"\e143"}.glyphicon-link:before{content:"\e144"}.glyphicon-phone:before{content:"\e145"}.glyphicon-pushpin:before{content:"\e146"}.glyphicon-usd:before{content:"\e148"}.glyphicon-gbp:before{content:"\e149"}.glyphicon-sort:before{content:"\e150"}.glyphicon-sort-by-alphabet:before{content:"\e151"}.glyphicon-sort-by-alphabet-alt:before{content:"\e152"}.glyphicon-sort-by-order:before{content:"\e153"}.glyphicon-sort-by-order-alt:before{content:"\e154"}.glyphicon-sort-by-attributes:before{content:"\e155"}.glyphicon-sort-by-attributes-alt:before{content:"\e156"}.glyphicon-unchecked:before{content:"\e157"}.glyphicon-expand:before{content:"\e158"}.glyphicon-collapse-down:before{content:"\e159"}.glyphicon-collapse-up:before{content:"\e160"}.glyphicon-log-in:before{content:"\e161"}.glyphicon-flash:before{content:"\e162"}.glyphicon-log-out:before{content:"\e163"}.glyphicon-new-window:before{content:"\e164"}.glyphicon-record:before{content:"\e165"}.glyphicon-save:before{content:"\e166"}.glyphicon-open:before{content:"\e167"}.glyphicon-saved:before{content:"\e168"}.glyphicon-import:before{content:"\e169"}.glyphicon-export:before{content:"\e170"}.glyphicon-send:before{content:"\e171"}.glyphicon-floppy-disk:before{content:"\e172"}.glyphicon-floppy-saved:before{content:"\e173"}.glyphicon-floppy-remove:before{content:"\e174"}.glyphicon-floppy-save:before{content:"\e175"}.glyphicon-floppy-open:before{content:"\e176"}.glyphicon-credit-card:before{content:"\e177"}.glyphicon-transfer:before{content:"\e178"}.glyphicon-cutlery:before{content:"\e179"}.glyphicon-header:before{content:"\e180"}.glyphicon-compressed:before{content:"\e181"}.glyphicon-earphone:before{content:"\e182"}.glyphicon-phone-alt:before{content:"\e183"}.glyphicon-tower:before{content:"\e184"}.glyphicon-stats:before{content:"\e185"}.glyphicon-sd-video:before{content:"\e186"}.glyphicon-hd-video:before{content:"\e187"}.glyphicon-subtitles:before{content:"\e188"}.glyphicon-sound-stereo:before{content:"\e189"}.glyphicon-sound-dolby:before{content:"\e190"}.glyphicon-sound-5-1:before{content:"\e191"}.glyphicon-sound-6-1:before{content:"\e192"}.glyphicon-sound-7-1:before{content:"\e193"}.glyphicon-copyright-mark:before{content:"\e194"}.glyphicon-registration-mark:before{content:"\e195"}.glyphicon-cloud-download:before{content:"\e197"}.glyphicon-cloud-upload:before{content:"\e198"}.glyphicon-tree-conifer:before{content:"\e199"}.glyphicon-tree-deciduous:before{content:"\e200"}.glyphicon-cd:before{content:"\e201"}.glyphicon-save-file:before{content:"\e202"}.glyphicon-open-file:before{content:"\e203"}.glyphicon-level-up:before{content:"\e204"}.glyphicon-copy:before{content:"\e205"}.glyphicon-paste:before{content:"\e206"}.glyphicon-alert:before{content:"\e209"}.glyphicon-equalizer:before{content:"\e210"}.glyphicon-king:before{content:"\e211"}.glyphicon-queen:before{content:"\e212"}.glyphicon-pawn:before{content:"\e213"}.glyphicon-bishop:before{content:"\e214"}.glyphicon-knight:before{content:"\e215"}.glyphicon-baby-formula:before{content:"\e216"}.glyphicon-tent:before{content:"\26fa"}.glyphicon-blackboard:before{content:"\e218"}.glyphicon-bed:before{content:"\e219"}.glyphicon-apple:before{content:"\f8ff"}.glyphicon-erase:before{content:"\e221"}.glyphicon-hourglass:before{content:"\231b"}.glyphicon-lamp:before{content:"\e223"}.glyphicon-duplicate:before{content:"\e224"}.glyphicon-piggy-bank:before{content:"\e225"}.glyphicon-scissors:before{content:"\e226"}.glyphicon-bitcoin:before,.glyphicon-btc:before,.glyphicon-xbt:before{content:"\e227"}.glyphicon-jpy:before,.glyphicon-yen:before{content:"\00a5"}.glyphicon-rub:before,.glyphicon-ruble:before{content:"\20bd"}.glyphicon-scale:before{content:"\e230"}.glyphicon-ice-lolly:before{content:"\e231"}.glyphicon-ice-lolly-tasted:before{content:"\e232"}.glyphicon-education:before{content:"\e233"}.glyphicon-option-horizontal:before{content:"\e234"}.glyphicon-option-vertical:before{content:"\e235"}.glyphicon-menu-hamburger:before{content:"\e236"}.glyphicon-modal-window:before{content:"\e237"}.glyphicon-oil:before{content:"\e238"}.glyphicon-grain:before{content:"\e239"}.glyphicon-sunglasses:before{content:"\e240"}.glyphicon-text-size:before{content:"\e241"}.glyphicon-text-color:before{content:"\e242"}.glyphicon-text-background:before{content:"\e243"}.glyphicon-object-align-top:before{content:"\e244"}.glyphicon-object-align-bottom:before{content:"\e245"}.glyphicon-object-align-horizontal:before{content:"\e246"}.glyphicon-object-align-left:before{content:"\e247"}.glyphicon-object-align-vertical:before{content:"\e248"}.glyphicon-object-align-right:before{content:"\e249"}.glyphicon-triangle-right:before{content:"\e250"}.glyphicon-triangle-left:before{content:"\e251"}.glyphicon-triangle-bottom:before{content:"\e252"}.glyphicon-triangle-top:before{content:"\e253"}.glyphicon-console:before{content:"\e254"}.glyphicon-superscript:before{content:"\e255"}.glyphicon-subscript:before{content:"\e256"}.glyphicon-menu-left:before{content:"\e257"}.glyphicon-menu-right:before{content:"\e258"}.glyphicon-menu-down:before{content:"\e259"}.glyphicon-menu-up:before{content:"\e260"}*,:after,:before{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}body{margin:0;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:13px;line-height:1.42857143;color:#000;background-color:#fff}button,input,select,textarea{font-family:inherit;font-size:inherit;line-height:inherit}a{color:#337ab7;text-decoration:none}a:focus,a:hover{color:#23527c;text-decoration:underline}a:focus{outline:dotted thin;outline:-webkit-focus-ring-color auto 5px;outline-offset:-2px}figure{margin:0}.carousel-inner>.item>a>img,.carousel-inner>.item>img,.img-responsive,.thumbnail a>img,.thumbnail>img{display:block;max-width:100%;height:auto}.img-rounded{border-radius:3px}.img-thumbnail{padding:4px;line-height:1.42857143;background-color:#fff;border:1px solid #ddd;border-radius:2px;-webkit-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;transition:all .2s ease-in-out;display:inline-block;max-width:100%;height:auto}.img-circle{border-radius:50%}hr{margin-top:18px;margin-bottom:18px;border:0;border-top:1px solid #eee}.sr-only{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);border:0}.sr-only-focusable:active,.sr-only-focusable:focus{position:static;width:auto;height:auto;margin:0;overflow:visible;clip:auto}[role=button]{cursor:pointer}.h1,.h2,.h3,.h4,.h5,.h6,h1,h2,h3,h4,h5,h6{font-family:inherit;font-weight:500;line-height:1.1;color:inherit}.h1 .small,.h1 small,.h2 .small,.h2 small,.h3 .small,.h3 small,.h4 .small,.h4 small,.h5 .small,.h5 small,.h6 .small,.h6 small,h1 .small,h1 small,h2 .small,h2 small,h3 .small,h3 small,h4 .small,h4 small,h5 .small,h5 small,h6 .small,h6 small{font-weight:400;line-height:1;color:#777}.h1,.h2,.h3,h1,h2,h3{margin-top:18px;margin-bottom:9px}.h1 .small,.h1 small,.h2 .small,.h2 small,.h3 .small,.h3 small,h1 .small,h1 small,h2 .small,h2 small,h3 .small,h3 small{font-size:65%}.h4,.h5,.h6,h4,h5,h6{margin-top:9px;margin-bottom:9px}.h4 .small,.h4 small,.h5 .small,.h5 small,.h6 .small,.h6 small,h4 .small,h4 small,h5 .small,h5 small,h6 .small,h6 small{font-size:75%}.h1,h1{font-size:33px}.h2,h2{font-size:27px}.h3,h3{font-size:23px}.h4,h4{font-size:17px}.h5,h5{font-size:13px}.h6,h6{font-size:12px}p{margin:0 0 9px}.lead{margin-bottom:18px;font-size:14px;font-weight:300;line-height:1.4}@media (min-width:768px){.lead{font-size:19.5px}}.small,small{font-size:92%}.mark,mark{background-color:#fcf8e3;padding:.2em}.text-left{text-align:left}.text-right{text-align:right}.text-center{text-align:center}.text-justify{text-align:justify}.text-nowrap{white-space:nowrap}.text-lowercase{text-transform:lowercase}.text-uppercase{text-transform:uppercase}.text-capitalize{text-transform:capitalize}.text-muted{color:#777}.text-primary{color:#337ab7}a.text-primary:hover{color:#286090}.text-success{color:#3c763d}a.text-success:hover{color:#2b542c}.text-info{color:#31708f}a.text-info:hover{color:#245269}.text-warning{color:#8a6d3b}a.text-warning:hover{color:#66512c}.text-danger{color:#a94442}a.text-danger:hover{color:#843534}.bg-primary{color:#fff;background-color:#337ab7}a.bg-primary:hover{background-color:#286090}.bg-success{background-color:#dff0d8}a.bg-success:hover{background-color:#c1e2b3}.bg-info{background-color:#d9edf7}a.bg-info:hover{background-color:#afd9ee}.bg-warning{background-color:#fcf8e3}a.bg-warning:hover{background-color:#f7ecb5}.bg-danger{background-color:#f2dede}a.bg-danger:hover{background-color:#e4b9b9}.page-header{padding-bottom:8px;margin:36px 0 18px;border-bottom:1px solid #eee}ol,ul{margin-top:0;margin-bottom:9px}ol ol,ol ul,ul ol,ul ul{margin-bottom:0}.list-unstyled{padding-left:0;list-style:none}.list-inline{padding-left:0;list-style:none;margin-left:-5px}.list-inline>li{display:inline-block;padding-left:5px;padding-right:5px}dl{margin-top:0;margin-bottom:18px}dd,dt{line-height:1.42857143}dt{font-weight:700}dd{margin-left:0}@media (min-width:541px){.dl-horizontal dt{float:left;width:160px;clear:left;text-align:right;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.dl-horizontal dd{margin-left:180px}}abbr[data-original-title],abbr[title]{cursor:help;border-bottom:1px dotted #777}.initialism{font-size:90%;text-transform:uppercase}blockquote{padding:9px 18px;margin:0 0 18px;font-size:inherit;border-left:5px solid #eee}blockquote ol:last-child,blockquote p:last-child,blockquote ul:last-child{margin-bottom:0}blockquote .small,blockquote footer,blockquote small{display:block;font-size:80%;line-height:1.42857143;color:#777}blockquote .small:before,blockquote footer:before,blockquote small:before{content:'\2014 \00A0'}.blockquote-reverse,blockquote.pull-right{padding-right:15px;padding-left:0;border-right:5px solid #eee;border-left:0;text-align:right}.blockquote-reverse .small:before,.blockquote-reverse footer:before,.blockquote-reverse small:before,blockquote.pull-right .small:before,blockquote.pull-right footer:before,blockquote.pull-right small:before{content:''}.blockquote-reverse .small:after,.blockquote-reverse footer:after,.blockquote-reverse small:after,blockquote.pull-right .small:after,blockquote.pull-right footer:after,blockquote.pull-right small:after{content:'\00A0 \2014'}address{margin-bottom:18px;font-style:normal;line-height:1.42857143}code,kbd,pre,samp{font-family:monospace}code{padding:2px 4px;font-size:90%;background-color:#f9f2f4;border-radius:2px}kbd{padding:2px 4px;font-size:90%;color:#fff;background-color:#333;border-radius:1px;box-shadow:inset 0 -1px 0 rgba(0,0,0,.25)}kbd kbd{padding:0;font-size:100%;font-weight:700;box-shadow:none}pre{display:block;padding:8.5px;margin:0 0 9px;word-break:break-all;word-wrap:break-word;color:#333;background-color:#f5f5f5;border:1px solid #ccc;border-radius:2px}pre code{padding:0;font-size:inherit;color:inherit;white-space:pre-wrap;background-color:transparent;border-radius:0}.pre-scrollable{max-height:340px;overflow-y:scroll}.container{margin-right:auto;margin-left:auto;padding-left:0;padding-right:0}@media (min-width:768px){.container{width:768px}}@media (min-width:992px){.container{width:940px}}@media (min-width:1200px){.container{width:1140px}}.container-fluid{margin-right:auto;margin-left:auto;padding-left:0;padding-right:0}.row{margin-left:0;margin-right:0}.col-lg-1,.col-lg-10,.col-lg-11,.col-lg-12,.col-lg-2,.col-lg-3,.col-lg-4,.col-lg-5,.col-lg-6,.col-lg-7,.col-lg-8,.col-lg-9,.col-md-1,.col-md-10,.col-md-11,.col-md-12,.col-md-2,.col-md-3,.col-md-4,.col-md-5,.col-md-6,.col-md-7,.col-md-8,.col-md-9,.col-sm-1,.col-sm-10,.col-sm-11,.col-sm-12,.col-sm-2,.col-sm-3,.col-sm-4,.col-sm-5,.col-sm-6,.col-sm-7,.col-sm-8,.col-sm-9,.col-xs-1,.col-xs-10,.col-xs-11,.col-xs-12,.col-xs-2,.col-xs-3,.col-xs-4,.col-xs-5,.col-xs-6,.col-xs-7,.col-xs-8,.col-xs-9{position:relative;min-height:1px;padding-left:0;padding-right:0}.col-xs-1,.col-xs-10,.col-xs-11,.col-xs-12,.col-xs-2,.col-xs-3,.col-xs-4,.col-xs-5,.col-xs-6,.col-xs-7,.col-xs-8,.col-xs-9{float:left}.col-xs-12{width:100%}.col-xs-11{width:91.66666667%}.col-xs-10{width:83.33333333%}.col-xs-9{width:75%}.col-xs-8{width:66.66666667%}.col-xs-7{width:58.33333333%}.col-xs-6{width:50%}.col-xs-5{width:41.66666667%}.col-xs-4{width:33.33333333%}.col-xs-3{width:25%}.col-xs-2{width:16.66666667%}.col-xs-1{width:8.33333333%}.col-xs-pull-12{right:100%}.col-xs-pull-11{right:91.66666667%}.col-xs-pull-10{right:83.33333333%}.col-xs-pull-9{right:75%}.col-xs-pull-8{right:66.66666667%}.col-xs-pull-7{right:58.33333333%}.col-xs-pull-6{right:50%}.col-xs-pull-5{right:41.66666667%}.col-xs-pull-4{right:33.33333333%}.col-xs-pull-3{right:25%}.col-xs-pull-2{right:16.66666667%}.col-xs-pull-1{right:8.33333333%}.col-xs-pull-0{right:auto}.col-xs-push-12{left:100%}.col-xs-push-11{left:91.66666667%}.col-xs-push-10{left:83.33333333%}.col-xs-push-9{left:75%}.col-xs-push-8{left:66.66666667%}.col-xs-push-7{left:58.33333333%}.col-xs-push-6{left:50%}.col-xs-push-5{left:41.66666667%}.col-xs-push-4{left:33.33333333%}.col-xs-push-3{left:25%}.col-xs-push-2{left:16.66666667%}.col-xs-push-1{left:8.33333333%}.col-xs-push-0{left:auto}.col-xs-offset-12{margin-left:100%}.col-xs-offset-11{margin-left:91.66666667%}.col-xs-offset-10{margin-left:83.33333333%}.col-xs-offset-9{margin-left:75%}.col-xs-offset-8{margin-left:66.66666667%}.col-xs-offset-7{margin-left:58.33333333%}.col-xs-offset-6{margin-left:50%}.col-xs-offset-5{margin-left:41.66666667%}.col-xs-offset-4{margin-left:33.33333333%}.col-xs-offset-3{margin-left:25%}.col-xs-offset-2{margin-left:16.66666667%}.col-xs-offset-1{margin-left:8.33333333%}.col-xs-offset-0{margin-left:0}@media (min-width:768px){.col-sm-1,.col-sm-10,.col-sm-11,.col-sm-12,.col-sm-2,.col-sm-3,.col-sm-4,.col-sm-5,.col-sm-6,.col-sm-7,.col-sm-8,.col-sm-9{float:left}.col-sm-12{width:100%}.col-sm-11{width:91.66666667%}.col-sm-10{width:83.33333333%}.col-sm-9{width:75%}.col-sm-8{width:66.66666667%}.col-sm-7{width:58.33333333%}.col-sm-6{width:50%}.col-sm-5{width:41.66666667%}.col-sm-4{width:33.33333333%}.col-sm-3{width:25%}.col-sm-2{width:16.66666667%}.col-sm-1{width:8.33333333%}.col-sm-pull-12{right:100%}.col-sm-pull-11{right:91.66666667%}.col-sm-pull-10{right:83.33333333%}.col-sm-pull-9{right:75%}.col-sm-pull-8{right:66.66666667%}.col-sm-pull-7{right:58.33333333%}.col-sm-pull-6{right:50%}.col-sm-pull-5{right:41.66666667%}.col-sm-pull-4{right:33.33333333%}.col-sm-pull-3{right:25%}.col-sm-pull-2{right:16.66666667%}.col-sm-pull-1{right:8.33333333%}.col-sm-pull-0{right:auto}.col-sm-push-12{left:100%}.col-sm-push-11{left:91.66666667%}.col-sm-push-10{left:83.33333333%}.col-sm-push-9{left:75%}.col-sm-push-8{left:66.66666667%}.col-sm-push-7{left:58.33333333%}.col-sm-push-6{left:50%}.col-sm-push-5{left:41.66666667%}.col-sm-push-4{left:33.33333333%}.col-sm-push-3{left:25%}.col-sm-push-2{left:16.66666667%}.col-sm-push-1{left:8.33333333%}.col-sm-push-0{left:auto}.col-sm-offset-12{margin-left:100%}.col-sm-offset-11{margin-left:91.66666667%}.col-sm-offset-10{margin-left:83.33333333%}.col-sm-offset-9{margin-left:75%}.col-sm-offset-8{margin-left:66.66666667%}.col-sm-offset-7{margin-left:58.33333333%}.col-sm-offset-6{margin-left:50%}.col-sm-offset-5{margin-left:41.66666667%}.col-sm-offset-4{margin-left:33.33333333%}.col-sm-offset-3{margin-left:25%}.col-sm-offset-2{margin-left:16.66666667%}.col-sm-offset-1{margin-left:8.33333333%}.col-sm-offset-0{margin-left:0}}@media (min-width:992px){.col-md-1,.col-md-10,.col-md-11,.col-md-12,.col-md-2,.col-md-3,.col-md-4,.col-md-5,.col-md-6,.col-md-7,.col-md-8,.col-md-9{float:left}.col-md-12{width:100%}.col-md-11{width:91.66666667%}.col-md-10{width:83.33333333%}.col-md-9{width:75%}.col-md-8{width:66.66666667%}.col-md-7{width:58.33333333%}.col-md-6{width:50%}.col-md-5{width:41.66666667%}.col-md-4{width:33.33333333%}.col-md-3{width:25%}.col-md-2{width:16.66666667%}.col-md-1{width:8.33333333%}.col-md-pull-12{right:100%}.col-md-pull-11{right:91.66666667%}.col-md-pull-10{right:83.33333333%}.col-md-pull-9{right:75%}.col-md-pull-8{right:66.66666667%}.col-md-pull-7{right:58.33333333%}.col-md-pull-6{right:50%}.col-md-pull-5{right:41.66666667%}.col-md-pull-4{right:33.33333333%}.col-md-pull-3{right:25%}.col-md-pull-2{right:16.66666667%}.col-md-pull-1{right:8.33333333%}.col-md-pull-0{right:auto}.col-md-push-12{left:100%}.col-md-push-11{left:91.66666667%}.col-md-push-10{left:83.33333333%}.col-md-push-9{left:75%}.col-md-push-8{left:66.66666667%}.col-md-push-7{left:58.33333333%}.col-md-push-6{left:50%}.col-md-push-5{left:41.66666667%}.col-md-push-4{left:33.33333333%}.col-md-push-3{left:25%}.col-md-push-2{left:16.66666667%}.col-md-push-1{left:8.33333333%}.col-md-push-0{left:auto}.col-md-offset-12{margin-left:100%}.col-md-offset-11{margin-left:91.66666667%}.col-md-offset-10{margin-left:83.33333333%}.col-md-offset-9{margin-left:75%}.col-md-offset-8{margin-left:66.66666667%}.col-md-offset-7{margin-left:58.33333333%}.col-md-offset-6{margin-left:50%}.col-md-offset-5{margin-left:41.66666667%}.col-md-offset-4{margin-left:33.33333333%}.col-md-offset-3{margin-left:25%}.col-md-offset-2{margin-left:16.66666667%}.col-md-offset-1{margin-left:8.33333333%}.col-md-offset-0{margin-left:0}}@media (min-width:1200px){.col-lg-1,.col-lg-10,.col-lg-11,.col-lg-12,.col-lg-2,.col-lg-3,.col-lg-4,.col-lg-5,.col-lg-6,.col-lg-7,.col-lg-8,.col-lg-9{float:left}.col-lg-12{width:100%}.col-lg-11{width:91.66666667%}.col-lg-10{width:83.33333333%}.col-lg-9{width:75%}.col-lg-8{width:66.66666667%}.col-lg-7{width:58.33333333%}.col-lg-6{width:50%}.col-lg-5{width:41.66666667%}.col-lg-4{width:33.33333333%}.col-lg-3{width:25%}.col-lg-2{width:16.66666667%}.col-lg-1{width:8.33333333%}.col-lg-pull-12{right:100%}.col-lg-pull-11{right:91.66666667%}.col-lg-pull-10{right:83.33333333%}.col-lg-pull-9{right:75%}.col-lg-pull-8{right:66.66666667%}.col-lg-pull-7{right:58.33333333%}.col-lg-pull-6{right:50%}.col-lg-pull-5{right:41.66666667%}.col-lg-pull-4{right:33.33333333%}.col-lg-pull-3{right:25%}.col-lg-pull-2{right:16.66666667%}.col-lg-pull-1{right:8.33333333%}.col-lg-pull-0{right:auto}.col-lg-push-12{left:100%}.col-lg-push-11{left:91.66666667%}.col-lg-push-10{left:83.33333333%}.col-lg-push-9{left:75%}.col-lg-push-8{left:66.66666667%}.col-lg-push-7{left:58.33333333%}.col-lg-push-6{left:50%}.col-lg-push-5{left:41.66666667%}.col-lg-push-4{left:33.33333333%}.col-lg-push-3{left:25%}.col-lg-push-2{left:16.66666667%}.col-lg-push-1{left:8.33333333%}.col-lg-push-0{left:auto}.col-lg-offset-12{margin-left:100%}.col-lg-offset-11{margin-left:91.66666667%}.col-lg-offset-10{margin-left:83.33333333%}.col-lg-offset-9{margin-left:75%}.col-lg-offset-8{margin-left:66.66666667%}.col-lg-offset-7{margin-left:58.33333333%}.col-lg-offset-6{margin-left:50%}.col-lg-offset-5{margin-left:41.66666667%}.col-lg-offset-4{margin-left:33.33333333%}.col-lg-offset-3{margin-left:25%}.col-lg-offset-2{margin-left:16.66666667%}.col-lg-offset-1{margin-left:8.33333333%}.col-lg-offset-0{margin-left:0}}table{background-color:transparent}caption{padding-top:8px;padding-bottom:8px;color:#777;text-align:left}th{text-align:left}.table{width:100%;max-width:100%;margin-bottom:18px}.table>tbody>tr>td,.table>tbody>tr>th,.table>tfoot>tr>td,.table>tfoot>tr>th,.table>thead>tr>td,.table>thead>tr>th{padding:8px;line-height:1.42857143;vertical-align:top;border-top:1px solid #ddd}.table>thead>tr>th{vertical-align:bottom;border-bottom:2px solid #ddd}.table>caption+thead>tr:first-child>td,.table>caption+thead>tr:first-child>th,.table>colgroup+thead>tr:first-child>td,.table>colgroup+thead>tr:first-child>th,.table>thead:first-child>tr:first-child>td,.table>thead:first-child>tr:first-child>th{border-top:0}.table>tbody+tbody{border-top:2px solid #ddd}.table .table{background-color:#fff}.table-condensed>tbody>tr>td,.table-condensed>tbody>tr>th,.table-condensed>tfoot>tr>td,.table-condensed>tfoot>tr>th,.table-condensed>thead>tr>td,.table-condensed>thead>tr>th{padding:5px}.table-bordered,.table-bordered>tbody>tr>td,.table-bordered>tbody>tr>th,.table-bordered>tfoot>tr>td,.table-bordered>tfoot>tr>th,.table-bordered>thead>tr>td,.table-bordered>thead>tr>th{border:1px solid #ddd}.table-bordered>thead>tr>td,.table-bordered>thead>tr>th{border-bottom-width:2px}.table-striped>tbody>tr:nth-of-type(odd){background-color:#f9f9f9}.table-hover>tbody>tr:hover{background-color:#f5f5f5}table col[class*=col-]{position:static;float:none;display:table-column}table td[class*=col-],table th[class*=col-]{position:static;float:none;display:table-cell}.table>tbody>tr.active>td,.table>tbody>tr.active>th,.table>tbody>tr>td.active,.table>tbody>tr>th.active,.table>tfoot>tr.active>td,.table>tfoot>tr.active>th,.table>tfoot>tr>td.active,.table>tfoot>tr>th.active,.table>thead>tr.active>td,.table>thead>tr.active>th,.table>thead>tr>td.active,.table>thead>tr>th.active{background-color:#f5f5f5}.table-hover>tbody>tr.active:hover>td,.table-hover>tbody>tr.active:hover>th,.table-hover>tbody>tr:hover>.active,.table-hover>tbody>tr>td.active:hover,.table-hover>tbody>tr>th.active:hover{background-color:#e8e8e8}.table>tbody>tr.success>td,.table>tbody>tr.success>th,.table>tbody>tr>td.success,.table>tbody>tr>th.success,.table>tfoot>tr.success>td,.table>tfoot>tr.success>th,.table>tfoot>tr>td.success,.table>tfoot>tr>th.success,.table>thead>tr.success>td,.table>thead>tr.success>th,.table>thead>tr>td.success,.table>thead>tr>th.success{background-color:#dff0d8}.table-hover>tbody>tr.success:hover>td,.table-hover>tbody>tr.success:hover>th,.table-hover>tbody>tr:hover>.success,.table-hover>tbody>tr>td.success:hover,.table-hover>tbody>tr>th.success:hover{background-color:#d0e9c6}.table>tbody>tr.info>td,.table>tbody>tr.info>th,.table>tbody>tr>td.info,.table>tbody>tr>th.info,.table>tfoot>tr.info>td,.table>tfoot>tr.info>th,.table>tfoot>tr>td.info,.table>tfoot>tr>th.info,.table>thead>tr.info>td,.table>thead>tr.info>th,.table>thead>tr>td.info,.table>thead>tr>th.info{background-color:#d9edf7}.table-hover>tbody>tr.info:hover>td,.table-hover>tbody>tr.info:hover>th,.table-hover>tbody>tr:hover>.info,.table-hover>tbody>tr>td.info:hover,.table-hover>tbody>tr>th.info:hover{background-color:#c4e3f3}.table>tbody>tr.warning>td,.table>tbody>tr.warning>th,.table>tbody>tr>td.warning,.table>tbody>tr>th.warning,.table>tfoot>tr.warning>td,.table>tfoot>tr.warning>th,.table>tfoot>tr>td.warning,.table>tfoot>tr>th.warning,.table>thead>tr.warning>td,.table>thead>tr.warning>th,.table>thead>tr>td.warning,.table>thead>tr>th.warning{background-color:#fcf8e3}.table-hover>tbody>tr.warning:hover>td,.table-hover>tbody>tr.warning:hover>th,.table-hover>tbody>tr:hover>.warning,.table-hover>tbody>tr>td.warning:hover,.table-hover>tbody>tr>th.warning:hover{background-color:#faf2cc}.table>tbody>tr.danger>td,.table>tbody>tr.danger>th,.table>tbody>tr>td.danger,.table>tbody>tr>th.danger,.table>tfoot>tr.danger>td,.table>tfoot>tr.danger>th,.table>tfoot>tr>td.danger,.table>tfoot>tr>th.danger,.table>thead>tr.danger>td,.table>thead>tr.danger>th,.table>thead>tr>td.danger,.table>thead>tr>th.danger{background-color:#f2dede}.table-hover>tbody>tr.danger:hover>td,.table-hover>tbody>tr.danger:hover>th,.table-hover>tbody>tr:hover>.danger,.table-hover>tbody>tr>td.danger:hover,.table-hover>tbody>tr>th.danger:hover{background-color:#ebcccc}.table-responsive{overflow-x:auto;min-height:.01%}@media screen and (max-width:767px){.table-responsive{width:100%;margin-bottom:13.5px;overflow-y:hidden;-ms-overflow-style:-ms-autohiding-scrollbar;border:1px solid #ddd}.table-responsive>.table{margin-bottom:0}.table-responsive>.table>tbody>tr>td,.table-responsive>.table>tbody>tr>th,.table-responsive>.table>tfoot>tr>td,.table-responsive>.table>tfoot>tr>th,.table-responsive>.table>thead>tr>td,.table-responsive>.table>thead>tr>th{white-space:nowrap}.table-responsive>.table-bordered{border:0}.table-responsive>.table-bordered>tbody>tr>td:first-child,.table-responsive>.table-bordered>tbody>tr>th:first-child,.table-responsive>.table-bordered>tfoot>tr>td:first-child,.table-responsive>.table-bordered>tfoot>tr>th:first-child,.table-responsive>.table-bordered>thead>tr>td:first-child,.table-responsive>.table-bordered>thead>tr>th:first-child{border-left:0}.table-responsive>.table-bordered>tbody>tr>td:last-child,.table-responsive>.table-bordered>tbody>tr>th:last-child,.table-responsive>.table-bordered>tfoot>tr>td:last-child,.table-responsive>.table-bordered>tfoot>tr>th:last-child,.table-responsive>.table-bordered>thead>tr>td:last-child,.table-responsive>.table-bordered>thead>tr>th:last-child{border-right:0}.table-responsive>.table-bordered>tbody>tr:last-child>td,.table-responsive>.table-bordered>tbody>tr:last-child>th,.table-responsive>.table-bordered>tfoot>tr:last-child>td,.table-responsive>.table-bordered>tfoot>tr:last-child>th{border-bottom:0}}fieldset{padding:0;margin:0;border:0;min-width:0}legend{display:block;width:100%;padding:0;margin-bottom:18px;font-size:19.5px;line-height:inherit;color:#333;border:0;border-bottom:1px solid #e5e5e5}label{display:inline-block;max-width:100%;margin-bottom:5px}input[type=search]{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;-webkit-appearance:none}input[type=checkbox],input[type=radio]{margin:4px 0 0;margin-top:1px \9;line-height:normal}input[type=file]{display:block}input[type=range]{display:block;width:100%}select[multiple],select[size]{height:auto}input[type=file]:focus,input[type=checkbox]:focus,input[type=radio]:focus{outline:dotted thin;outline:-webkit-focus-ring-color auto 5px;outline-offset:-2px}output{display:block;padding-top:7px;font-size:13px;line-height:1.42857143;color:#555}.form-control{display:block;width:100%;height:32px;padding:6px 12px;font-size:13px;line-height:1.42857143;color:#555;background-color:#fff;background-image:none;border:1px solid #ccc;border-radius:2px;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-webkit-transition:border-color ease-in-out .15s,box-shadow ease-in-out .15s;-o-transition:border-color ease-in-out .15s,box-shadow ease-in-out .15s;transition:border-color ease-in-out .15s,box-shadow ease-in-out .15s}.form-control:focus{border-color:#66afe9;outline:0;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 8px rgba(102,175,233,.6);box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 8px rgba(102,175,233,.6)}.form-control::-moz-placeholder{color:#999;opacity:1}.form-control:-ms-input-placeholder{color:#999}.form-control::-webkit-input-placeholder{color:#999}.form-control[disabled],.form-control[readonly],fieldset[disabled] .form-control{background-color:#eee;opacity:1}.form-control[disabled],fieldset[disabled] .form-control{cursor:not-allowed}textarea.form-control{height:auto}@media screen and (-webkit-min-device-pixel-ratio:0){input[type=date],input[type=time],input[type=datetime-local],input[type=month]{line-height:32px}.input-group-sm input[type=date],.input-group-sm input[type=time],.input-group-sm input[type=datetime-local],.input-group-sm input[type=month],input[type=date].input-sm,input[type=time].input-sm,input[type=datetime-local].input-sm,input[type=month].input-sm{line-height:30px}.input-group-lg input[type=date],.input-group-lg input[type=time],.input-group-lg input[type=datetime-local],.input-group-lg input[type=month],input[type=date].input-lg,input[type=time].input-lg,input[type=datetime-local].input-lg,input[type=month].input-lg{line-height:45px}}.form-group{margin-bottom:15px}.checkbox,.radio{position:relative;display:block;margin-top:10px;margin-bottom:10px}.checkbox label,.radio label{min-height:18px;padding-left:20px;margin-bottom:0;font-weight:400;cursor:pointer}.checkbox input[type=checkbox],.checkbox-inline input[type=checkbox],.radio input[type=radio],.radio-inline input[type=radio]{position:absolute;margin-left:-20px;margin-top:4px \9}.checkbox+.checkbox,.radio+.radio{margin-top:-5px}.checkbox-inline,.radio-inline{position:relative;display:inline-block;padding-left:20px;margin-bottom:0;vertical-align:middle;font-weight:400;cursor:pointer}.checkbox-inline+.checkbox-inline,.radio-inline+.radio-inline{margin-top:0;margin-left:10px}.checkbox-inline.disabled,.checkbox.disabled label,.radio-inline.disabled,.radio.disabled label,fieldset[disabled] .checkbox label,fieldset[disabled] .checkbox-inline,fieldset[disabled] .radio label,fieldset[disabled] .radio-inline,fieldset[disabled] input[type=checkbox],fieldset[disabled] input[type=radio],input[type=checkbox].disabled,input[type=checkbox][disabled],input[type=radio].disabled,input[type=radio][disabled]{cursor:not-allowed}.form-control-static{padding-top:7px;padding-bottom:7px;margin-bottom:0;min-height:31px}.form-control-static.input-lg,.form-control-static.input-sm{padding-left:0;padding-right:0}.input-sm{height:30px;padding:5px 10px;font-size:12px;line-height:1.5;border-radius:1px}select.input-sm{height:30px;line-height:30px}select[multiple].input-sm,textarea.input-sm{height:auto}.form-group-sm .form-control{height:30px;padding:5px 10px;font-size:12px;line-height:1.5;border-radius:1px}select.form-group-sm .form-control{height:30px;line-height:30px}select[multiple].form-group-sm .form-control,textarea.form-group-sm .form-control{height:auto}.form-group-sm .form-control-static{height:30px;padding:5px 10px;font-size:12px;line-height:1.5;min-height:30px}.input-lg{height:45px;padding:10px 16px;font-size:17px;line-height:1.3333333;border-radius:3px}select.input-lg{height:45px;line-height:45px}select[multiple].input-lg,textarea.input-lg{height:auto}.form-group-lg .form-control{height:45px;padding:10px 16px;font-size:17px;line-height:1.3333333;border-radius:3px}select.form-group-lg .form-control{height:45px;line-height:45px}select[multiple].form-group-lg .form-control,textarea.form-group-lg .form-control{height:auto}.form-group-lg .form-control-static{height:45px;padding:10px 16px;font-size:17px;line-height:1.3333333;min-height:35px}.has-feedback{position:relative}.has-feedback .form-control{padding-right:40px}.form-control-feedback{position:absolute;top:0;right:0;z-index:2;display:block;width:32px;height:32px;line-height:32px;text-align:center;pointer-events:none}.input-lg+.form-control-feedback{width:45px;height:45px;line-height:45px}.input-sm+.form-control-feedback{width:30px;height:30px;line-height:30px}.has-success .checkbox,.has-success .checkbox-inline,.has-success .control-label,.has-success .help-block,.has-success .radio,.has-success .radio-inline,.has-success.checkbox label,.has-success.checkbox-inline label,.has-success.radio label,.has-success.radio-inline label{color:#3c763d}.has-success .form-control{border-color:#3c763d;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075)}.has-success .form-control:focus{border-color:#2b542c;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 6px #67b168;box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 6px #67b168}.has-success .input-group-addon{color:#3c763d;border-color:#3c763d;background-color:#dff0d8}.has-success .form-control-feedback{color:#3c763d}.has-warning .checkbox,.has-warning .checkbox-inline,.has-warning .control-label,.has-warning .help-block,.has-warning .radio,.has-warning .radio-inline,.has-warning.checkbox label,.has-warning.checkbox-inline label,.has-warning.radio label,.has-warning.radio-inline label{color:#8a6d3b}.has-warning .form-control{border-color:#8a6d3b;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075)}.has-warning .form-control:focus{border-color:#66512c;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 6px #c0a16b;box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 6px #c0a16b}.has-warning .input-group-addon{color:#8a6d3b;border-color:#8a6d3b;background-color:#fcf8e3}.has-warning .form-control-feedback{color:#8a6d3b}.has-error .checkbox,.has-error .checkbox-inline,.has-error .control-label,.has-error .help-block,.has-error .radio,.has-error .radio-inline,.has-error.checkbox label,.has-error.checkbox-inline label,.has-error.radio label,.has-error.radio-inline label{color:#a94442}.has-error .form-control{border-color:#a94442;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075)}.has-error .form-control:focus{border-color:#843534;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 6px #ce8483;box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 6px #ce8483}.has-error .input-group-addon{color:#a94442;border-color:#a94442;background-color:#f2dede}.has-error .form-control-feedback{color:#a94442}.has-feedback label~.form-control-feedback{top:23px}.has-feedback label.sr-only~.form-control-feedback{top:0}.help-block{display:block;margin-top:5px;margin-bottom:10px;color:#404040}.form-horizontal .checkbox,.form-horizontal .checkbox-inline,.form-horizontal .radio,.form-horizontal .radio-inline{margin-top:0;margin-bottom:0;padding-top:7px}.form-horizontal .checkbox,.form-horizontal .radio{min-height:25px}.form-horizontal .form-group{margin-left:0;margin-right:0}.form-horizontal .has-feedback .form-control-feedback{right:0}@media (min-width:768px){.form-inline .form-group{display:inline-block;margin-bottom:0;vertical-align:middle}.form-inline .form-control{display:inline-block;width:auto;vertical-align:middle}.form-inline .form-control-static{display:inline-block}.form-inline .input-group{display:inline-table;vertical-align:middle}.form-inline .input-group .form-control,.form-inline .input-group .input-group-addon,.form-inline .input-group .input-group-btn{width:auto}.form-inline .input-group>.form-control{width:100%}.form-inline .control-label{margin-bottom:0;vertical-align:middle}.form-inline .checkbox,.form-inline .radio{display:inline-block;margin-top:0;margin-bottom:0;vertical-align:middle}.form-inline .checkbox label,.form-inline .radio label{padding-left:0}.form-inline .checkbox input[type=checkbox],.form-inline .radio input[type=radio]{position:relative;margin-left:0}.form-inline .has-feedback .form-control-feedback{top:0}.form-horizontal .control-label{text-align:right;margin-bottom:0;padding-top:7px}.form-horizontal .form-group-lg .control-label{padding-top:14.33px}.form-horizontal .form-group-sm .control-label{padding-top:6px}}.btn{display:inline-block;margin-bottom:0;font-weight:400;text-align:center;vertical-align:middle;touch-action:manipulation;cursor:pointer;background-image:none;border:1px solid transparent;white-space:nowrap;padding:6px 12px;font-size:13px;line-height:1.42857143;border-radius:2px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.btn.active.focus,.btn.active:focus,.btn.focus,.btn:active.focus,.btn:active:focus,.btn:focus{outline:dotted thin;outline:-webkit-focus-ring-color auto 5px;outline-offset:-2px}.btn.focus,.btn:focus,.btn:hover{color:#333;text-decoration:none}.btn.active,.btn:active{outline:0;background-image:none;-webkit-box-shadow:inset 0 3px 5px rgba(0,0,0,.125);box-shadow:inset 0 3px 5px rgba(0,0,0,.125)}.btn.disabled,.btn[disabled],fieldset[disabled] .btn{cursor:not-allowed;pointer-events:none;opacity:.65;filter:alpha(opacity=65);-webkit-box-shadow:none;box-shadow:none}.btn-default{color:#333;background-color:#fff;border-color:#ccc}.btn-default.active,.btn-default.focus,.btn-default:active,.btn-default:focus,.btn-default:hover,.open>.dropdown-toggle.btn-default{color:#333;background-color:#e6e6e6;border-color:#adadad}.btn-default.active,.btn-default:active,.open>.dropdown-toggle.btn-default{background-image:none}.btn-default.disabled,.btn-default.disabled.active,.btn-default.disabled.focus,.btn-default.disabled:active,.btn-default.disabled:focus,.btn-default.disabled:hover,.btn-default[disabled],.btn-default[disabled].active,.btn-default[disabled].focus,.btn-default[disabled]:active,.btn-default[disabled]:focus,.btn-default[disabled]:hover,fieldset[disabled] .btn-default,fieldset[disabled] .btn-default.active,fieldset[disabled] .btn-default.focus,fieldset[disabled] .btn-default:active,fieldset[disabled] .btn-default:focus,fieldset[disabled] .btn-default:hover{background-color:#fff;border-color:#ccc}.btn-default .badge{color:#fff;background-color:#333}.btn-primary{color:#fff;background-color:#337ab7;border-color:#2e6da4}.btn-primary.active,.btn-primary.focus,.btn-primary:active,.btn-primary:focus,.btn-primary:hover,.open>.dropdown-toggle.btn-primary{color:#fff;background-color:#286090;border-color:#204d74}.btn-primary.active,.btn-primary:active,.open>.dropdown-toggle.btn-primary{background-image:none}.btn-primary.disabled,.btn-primary.disabled.active,.btn-primary.disabled.focus,.btn-primary.disabled:active,.btn-primary.disabled:focus,.btn-primary.disabled:hover,.btn-primary[disabled],.btn-primary[disabled].active,.btn-primary[disabled].focus,.btn-primary[disabled]:active,.btn-primary[disabled]:focus,.btn-primary[disabled]:hover,fieldset[disabled] .btn-primary,fieldset[disabled] .btn-primary.active,fieldset[disabled] .btn-primary.focus,fieldset[disabled] .btn-primary:active,fieldset[disabled] .btn-primary:focus,fieldset[disabled] .btn-primary:hover{background-color:#337ab7;border-color:#2e6da4}.btn-primary .badge{color:#337ab7;background-color:#fff}.btn-success{color:#fff;background-color:#5cb85c;border-color:#4cae4c}.btn-success.active,.btn-success.focus,.btn-success:active,.btn-success:focus,.btn-success:hover,.open>.dropdown-toggle.btn-success{color:#fff;background-color:#449d44;border-color:#398439}.btn-success.active,.btn-success:active,.open>.dropdown-toggle.btn-success{background-image:none}.btn-success.disabled,.btn-success.disabled.active,.btn-success.disabled.focus,.btn-success.disabled:active,.btn-success.disabled:focus,.btn-success.disabled:hover,.btn-success[disabled],.btn-success[disabled].active,.btn-success[disabled].focus,.btn-success[disabled]:active,.btn-success[disabled]:focus,.btn-success[disabled]:hover,fieldset[disabled] .btn-success,fieldset[disabled] .btn-success.active,fieldset[disabled] .btn-success.focus,fieldset[disabled] .btn-success:active,fieldset[disabled] .btn-success:focus,fieldset[disabled] .btn-success:hover{background-color:#5cb85c;border-color:#4cae4c}.btn-success .badge{color:#5cb85c;background-color:#fff}.btn-info{color:#fff;background-color:#5bc0de;border-color:#46b8da}.btn-info.active,.btn-info.focus,.btn-info:active,.btn-info:focus,.btn-info:hover,.open>.dropdown-toggle.btn-info{color:#fff;background-color:#31b0d5;border-color:#269abc}.btn-info.active,.btn-info:active,.open>.dropdown-toggle.btn-info{background-image:none}.btn-info.disabled,.btn-info.disabled.active,.btn-info.disabled.focus,.btn-info.disabled:active,.btn-info.disabled:focus,.btn-info.disabled:hover,.btn-info[disabled],.btn-info[disabled].active,.btn-info[disabled].focus,.btn-info[disabled]:active,.btn-info[disabled]:focus,.btn-info[disabled]:hover,fieldset[disabled] .btn-info,fieldset[disabled] .btn-info.active,fieldset[disabled] .btn-info.focus,fieldset[disabled] .btn-info:active,fieldset[disabled] .btn-info:focus,fieldset[disabled] .btn-info:hover{background-color:#5bc0de;border-color:#46b8da}.btn-info .badge{color:#5bc0de;background-color:#fff}.btn-warning{color:#fff;background-color:#f0ad4e;border-color:#eea236}.btn-warning.active,.btn-warning.focus,.btn-warning:active,.btn-warning:focus,.btn-warning:hover,.open>.dropdown-toggle.btn-warning{color:#fff;background-color:#ec971f;border-color:#d58512}.btn-warning.active,.btn-warning:active,.open>.dropdown-toggle.btn-warning{background-image:none}.btn-warning.disabled,.btn-warning.disabled.active,.btn-warning.disabled.focus,.btn-warning.disabled:active,.btn-warning.disabled:focus,.btn-warning.disabled:hover,.btn-warning[disabled],.btn-warning[disabled].active,.btn-warning[disabled].focus,.btn-warning[disabled]:active,.btn-warning[disabled]:focus,.btn-warning[disabled]:hover,fieldset[disabled] .btn-warning,fieldset[disabled] .btn-warning.active,fieldset[disabled] .btn-warning.focus,fieldset[disabled] .btn-warning:active,fieldset[disabled] .btn-warning:focus,fieldset[disabled] .btn-warning:hover{background-color:#f0ad4e;border-color:#eea236}.btn-warning .badge{color:#f0ad4e;background-color:#fff}.btn-danger{color:#fff;background-color:#d9534f;border-color:#d43f3a}.btn-danger.active,.btn-danger.focus,.btn-danger:active,.btn-danger:focus,.btn-danger:hover,.open>.dropdown-toggle.btn-danger{color:#fff;background-color:#c9302c;border-color:#ac2925}.btn-danger.active,.btn-danger:active,.open>.dropdown-toggle.btn-danger{background-image:none}.btn-danger.disabled,.btn-danger.disabled.active,.btn-danger.disabled.focus,.btn-danger.disabled:active,.btn-danger.disabled:focus,.btn-danger.disabled:hover,.btn-danger[disabled],.btn-danger[disabled].active,.btn-danger[disabled].focus,.btn-danger[disabled]:active,.btn-danger[disabled]:focus,.btn-danger[disabled]:hover,fieldset[disabled] .btn-danger,fieldset[disabled] .btn-danger.active,fieldset[disabled] .btn-danger.focus,fieldset[disabled] .btn-danger:active,fieldset[disabled] .btn-danger:focus,fieldset[disabled] .btn-danger:hover{background-color:#d9534f;border-color:#d43f3a}.btn-danger .badge{color:#d9534f;background-color:#fff}.btn-link{color:#337ab7;font-weight:400;border-radius:0}.btn-link,.btn-link.active,.btn-link:active,.btn-link[disabled],fieldset[disabled] .btn-link{background-color:transparent;-webkit-box-shadow:none;box-shadow:none}.btn-link,.btn-link:active,.btn-link:focus,.btn-link:hover{border-color:transparent}.btn-link:focus,.btn-link:hover{color:#23527c;text-decoration:underline;background-color:transparent}.btn-link[disabled]:focus,.btn-link[disabled]:hover,fieldset[disabled] .btn-link:focus,fieldset[disabled] .btn-link:hover{color:#777;text-decoration:none}.btn-group-lg>.btn,.btn-lg{padding:10px 16px;font-size:17px;line-height:1.3333333;border-radius:3px}.btn-group-sm>.btn,.btn-sm{padding:5px 10px;font-size:12px;line-height:1.5;border-radius:1px}.btn-group-xs>.btn,.btn-xs{padding:1px 5px;font-size:12px;line-height:1.5;border-radius:1px}.btn-block{display:block;width:100%}.btn-block+.btn-block{margin-top:5px}input[type=button].btn-block,input[type=reset].btn-block,input[type=submit].btn-block{width:100%}.fade{opacity:0;-webkit-transition:opacity .15s linear;-o-transition:opacity .15s linear;transition:opacity .15s linear}.fade.in{opacity:1}.collapse{display:none}.collapse.in{display:block}tr.collapse.in{display:table-row}tbody.collapse.in{display:table-row-group}.collapsing{position:relative;height:0;overflow:hidden;-webkit-transition-property:height,visibility;transition-property:height,visibility;-webkit-transition-duration:.35s;transition-duration:.35s;-webkit-transition-timing-function:ease;transition-timing-function:ease}.caret{display:inline-block;width:0;height:0;margin-left:2px;vertical-align:middle;border-top:4px dashed;border-right:4px solid transparent;border-left:4px solid transparent}.dropdown,.dropup{position:relative}.dropdown-toggle:focus{outline:0}.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;display:none;float:left;min-width:160px;padding:5px 0;margin:2px 0 0;list-style:none;font-size:13px;text-align:left;background-color:#fff;border:1px solid #ccc;border:1px solid rgba(0,0,0,.15);border-radius:2px;-webkit-box-shadow:0 6px 12px rgba(0,0,0,.175);box-shadow:0 6px 12px rgba(0,0,0,.175);background-clip:padding-box}.dropdown-menu.pull-right{right:0;left:auto}.dropdown-menu .divider{height:1px;margin:8px 0;overflow:hidden;background-color:#e5e5e5}.dropdown-menu>li>a{display:block;padding:3px 20px;clear:both;font-weight:400;line-height:1.42857143;color:#333;white-space:nowrap}.dropdown-menu>li>a:focus,.dropdown-menu>li>a:hover{text-decoration:none;color:#262626;background-color:#f5f5f5}.dropdown-menu>.active>a,.dropdown-menu>.active>a:focus,.dropdown-menu>.active>a:hover{color:#fff;text-decoration:none;outline:0;background-color:#337ab7}.dropdown-menu>.disabled>a,.dropdown-menu>.disabled>a:focus,.dropdown-menu>.disabled>a:hover{color:#777}.dropdown-menu>.disabled>a:focus,.dropdown-menu>.disabled>a:hover{text-decoration:none;background-color:transparent;background-image:none;filter:progid:DXImageTransform.Microsoft.gradient(enabled=false);cursor:not-allowed}.open>.dropdown-menu{display:block}.open>a{outline:0}.dropdown-menu-right{left:auto;right:0}.dropdown-menu-left{left:0;right:auto}.dropdown-header{display:block;padding:3px 20px;font-size:12px;line-height:1.42857143;color:#777;white-space:nowrap}.dropdown-backdrop{position:fixed;left:0;right:0;bottom:0;top:0;z-index:990}.pull-right>.dropdown-menu{right:0;left:auto}.dropup .caret,.navbar-fixed-bottom .dropdown .caret{border-top:0;border-bottom:4px solid;content:""}.dropup .dropdown-menu,.navbar-fixed-bottom .dropdown .dropdown-menu{top:auto;bottom:100%;margin-bottom:2px}@media (min-width:541px){.navbar-right .dropdown-menu{left:auto;right:0}.navbar-right .dropdown-menu-left{left:0;right:auto}}.btn-group,.btn-group-vertical{position:relative;display:inline-block;vertical-align:middle}.btn-group-vertical>.btn,.btn-group>.btn{position:relative;float:left}.btn-group-vertical>.btn.active,.btn-group-vertical>.btn:active,.btn-group-vertical>.btn:focus,.btn-group-vertical>.btn:hover,.btn-group>.btn.active,.btn-group>.btn:active,.btn-group>.btn:focus,.btn-group>.btn:hover{z-index:2}.btn-group .btn+.btn,.btn-group .btn+.btn-group,.btn-group .btn-group+.btn,.btn-group .btn-group+.btn-group{margin-left:-1px}.btn-toolbar{margin-left:-5px}.btn-toolbar .btn-group,.btn-toolbar .input-group{float:left}.btn-toolbar>.btn,.btn-toolbar>.btn-group,.btn-toolbar>.input-group{margin-left:5px}.btn-group>.btn:not(:first-child):not(:last-child):not(.dropdown-toggle){border-radius:0}.btn-group>.btn:first-child{margin-left:0}.btn-group>.btn:first-child:not(:last-child):not(.dropdown-toggle){border-bottom-right-radius:0;border-top-right-radius:0}.btn-group>.btn:last-child:not(:first-child),.btn-group>.dropdown-toggle:not(:first-child){border-bottom-left-radius:0;border-top-left-radius:0}.btn-group>.btn-group{float:left}.btn-group>.btn-group:not(:first-child):not(:last-child)>.btn{border-radius:0}.btn-group>.btn-group:first-child:not(:last-child)>.btn:last-child,.btn-group>.btn-group:first-child:not(:last-child)>.dropdown-toggle{border-bottom-right-radius:0;border-top-right-radius:0}.btn-group>.btn-group:last-child:not(:first-child)>.btn:first-child{border-bottom-left-radius:0;border-top-left-radius:0}.btn-group .dropdown-toggle:active,.btn-group.open .dropdown-toggle{outline:0}.btn-group>.btn+.dropdown-toggle{padding-left:8px;padding-right:8px}.btn-group>.btn-lg+.dropdown-toggle{padding-left:12px;padding-right:12px}.btn-group.open .dropdown-toggle{-webkit-box-shadow:inset 0 3px 5px rgba(0,0,0,.125);box-shadow:inset 0 3px 5px rgba(0,0,0,.125)}.btn-group.open .dropdown-toggle.btn-link{-webkit-box-shadow:none;box-shadow:none}.btn .caret{margin-left:0}.btn-lg .caret{border-width:5px 5px 0}.dropup .btn-lg .caret{border-width:0 5px 5px}.btn-group-vertical>.btn,.btn-group-vertical>.btn-group,.btn-group-vertical>.btn-group>.btn{display:block;float:none;width:100%;max-width:100%}.btn-group-vertical>.btn-group>.btn{float:none}.btn-group-vertical>.btn+.btn,.btn-group-vertical>.btn+.btn-group,.btn-group-vertical>.btn-group+.btn,.btn-group-vertical>.btn-group+.btn-group{margin-top:-1px;margin-left:0}.btn-group-vertical>.btn:not(:first-child):not(:last-child){border-radius:0}.btn-group-vertical>.btn:first-child:not(:last-child){border-top-right-radius:2px;border-bottom-right-radius:0;border-bottom-left-radius:0}.btn-group-vertical>.btn:last-child:not(:first-child){border-bottom-left-radius:2px;border-top-right-radius:0;border-top-left-radius:0}.btn-group-vertical>.btn-group:not(:first-child):not(:last-child)>.btn{border-radius:0}.btn-group-vertical>.btn-group:first-child:not(:last-child)>.btn:last-child,.btn-group-vertical>.btn-group:first-child:not(:last-child)>.dropdown-toggle{border-bottom-right-radius:0;border-bottom-left-radius:0}.btn-group-vertical>.btn-group:last-child:not(:first-child)>.btn:first-child{border-top-right-radius:0;border-top-left-radius:0}.btn-group-justified{display:table;width:100%;table-layout:fixed;border-collapse:separate}.btn-group-justified>.btn,.btn-group-justified>.btn-group{float:none;display:table-cell;width:1%}.btn-group-justified>.btn-group .btn{width:100%}.btn-group-justified>.btn-group .dropdown-menu{left:auto}[data-toggle=buttons]>.btn input[type=checkbox],[data-toggle=buttons]>.btn input[type=radio],[data-toggle=buttons]>.btn-group>.btn input[type=checkbox],[data-toggle=buttons]>.btn-group>.btn input[type=radio]{position:absolute;clip:rect(0,0,0,0);pointer-events:none}.input-group{position:relative;display:table;border-collapse:separate}.input-group[class*=col-]{float:none;padding-left:0;padding-right:0}.input-group .form-control{position:relative;z-index:2;float:left;width:100%;margin-bottom:0}.input-group-lg>.form-control,.input-group-lg>.input-group-addon,.input-group-lg>.input-group-btn>.btn{height:45px;padding:10px 16px;font-size:17px;line-height:1.3333333;border-radius:3px}select.input-group-lg>.form-control,select.input-group-lg>.input-group-addon,select.input-group-lg>.input-group-btn>.btn{height:45px;line-height:45px}select[multiple].input-group-lg>.form-control,select[multiple].input-group-lg>.input-group-addon,select[multiple].input-group-lg>.input-group-btn>.btn,textarea.input-group-lg>.form-control,textarea.input-group-lg>.input-group-addon,textarea.input-group-lg>.input-group-btn>.btn{height:auto}.input-group-sm>.form-control,.input-group-sm>.input-group-addon,.input-group-sm>.input-group-btn>.btn{height:30px;padding:5px 10px;font-size:12px;line-height:1.5;border-radius:1px}select.input-group-sm>.form-control,select.input-group-sm>.input-group-addon,select.input-group-sm>.input-group-btn>.btn{height:30px;line-height:30px}select[multiple].input-group-sm>.form-control,select[multiple].input-group-sm>.input-group-addon,select[multiple].input-group-sm>.input-group-btn>.btn,textarea.input-group-sm>.form-control,textarea.input-group-sm>.input-group-addon,textarea.input-group-sm>.input-group-btn>.btn{height:auto}.input-group .form-control,.input-group-addon,.input-group-btn{display:table-cell}.input-group .form-control:not(:first-child):not(:last-child),.input-group-addon:not(:first-child):not(:last-child),.input-group-btn:not(:first-child):not(:last-child){border-radius:0}.input-group-addon,.input-group-btn{width:1%;white-space:nowrap;vertical-align:middle}.input-group-addon{padding:6px 12px;font-size:13px;font-weight:400;line-height:1;color:#555;text-align:center;background-color:#eee;border:1px solid #ccc;border-radius:2px}.input-group-addon.input-sm{padding:5px 10px;font-size:12px;border-radius:1px}.input-group-addon.input-lg{padding:10px 16px;font-size:17px;border-radius:3px}.input-group-addon input[type=checkbox],.input-group-addon input[type=radio]{margin-top:0}.input-group .form-control:first-child,.input-group-addon:first-child,.input-group-btn:first-child>.btn,.input-group-btn:first-child>.btn-group>.btn,.input-group-btn:first-child>.dropdown-toggle,.input-group-btn:last-child>.btn-group:not(:last-child)>.btn,.input-group-btn:last-child>.btn:not(:last-child):not(.dropdown-toggle){border-bottom-right-radius:0;border-top-right-radius:0}.input-group-addon:first-child{border-right:0}.input-group .form-control:last-child,.input-group-addon:last-child,.input-group-btn:first-child>.btn-group:not(:first-child)>.btn,.input-group-btn:first-child>.btn:not(:first-child),.input-group-btn:last-child>.btn,.input-group-btn:last-child>.btn-group>.btn,.input-group-btn:last-child>.dropdown-toggle{border-bottom-left-radius:0;border-top-left-radius:0}.input-group-addon:last-child{border-left:0}.input-group-btn{position:relative;font-size:0;white-space:nowrap}.input-group-btn>.btn{position:relative}.input-group-btn>.btn+.btn{margin-left:-1px}.input-group-btn>.btn:active,.input-group-btn>.btn:focus,.input-group-btn>.btn:hover{z-index:2}.input-group-btn:first-child>.btn,.input-group-btn:first-child>.btn-group{margin-right:-1px}.input-group-btn:last-child>.btn,.input-group-btn:last-child>.btn-group{margin-left:-1px}.nav{margin-bottom:0;padding-left:0;list-style:none}.nav>li{position:relative;display:block}.nav>li>a{position:relative;display:block;padding:10px 15px}.nav>li>a:focus,.nav>li>a:hover{text-decoration:none;background-color:#eee}.nav>li.disabled>a{color:#777}.nav>li.disabled>a:focus,.nav>li.disabled>a:hover{color:#777;text-decoration:none;background-color:transparent;cursor:not-allowed}.nav .open>a,.nav .open>a:focus,.nav .open>a:hover{background-color:#eee;border-color:#337ab7}.nav .nav-divider{height:1px;margin:8px 0;overflow:hidden;background-color:#e5e5e5}.nav>li>a>img{max-width:none}.nav-tabs{border-bottom:1px solid #ddd}.nav-tabs>li{float:left;margin-bottom:-1px}.nav-tabs>li>a{margin-right:2px;line-height:1.42857143;border:1px solid transparent;border-radius:2px 2px 0 0}.nav-tabs>li>a:hover{border-color:#eee #eee #ddd}.nav-tabs>li.active>a,.nav-tabs>li.active>a:focus,.nav-tabs>li.active>a:hover{color:#555;background-color:#fff;border:1px solid #ddd;border-bottom-color:transparent;cursor:default}.nav-tabs.nav-justified{width:100%;border-bottom:0}.nav-tabs.nav-justified>li{float:none}.nav-tabs.nav-justified>li>a{text-align:center;margin-bottom:5px;margin-right:0;border-radius:2px}.nav-tabs.nav-justified>.dropdown .dropdown-menu{top:auto;left:auto}.nav-tabs.nav-justified>.active>a,.nav-tabs.nav-justified>.active>a:focus,.nav-tabs.nav-justified>.active>a:hover{border:1px solid #ddd}@media (min-width:768px){.nav-tabs.nav-justified>li{display:table-cell;width:1%}.nav-tabs.nav-justified>li>a{margin-bottom:0;border-bottom:1px solid #ddd;border-radius:2px 2px 0 0}.nav-tabs.nav-justified>.active>a,.nav-tabs.nav-justified>.active>a:focus,.nav-tabs.nav-justified>.active>a:hover{border-bottom-color:#fff}}.nav-pills>li{float:left}.nav-pills>li>a{border-radius:2px}.nav-pills>li+li{margin-left:2px}.nav-pills>li.active>a,.nav-pills>li.active>a:focus,.nav-pills>li.active>a:hover{color:#fff;background-color:#337ab7}.nav-stacked>li{float:none}.nav-stacked>li+li{margin-top:2px;margin-left:0}.nav-justified{width:100%}.nav-justified>li{float:none}.nav-justified>li>a{text-align:center;margin-bottom:5px}.nav-justified>.dropdown .dropdown-menu{top:auto;left:auto}.nav-tabs-justified{border-bottom:0}.nav-tabs-justified>li>a{margin-right:0;border-radius:2px}.nav-tabs-justified>.active>a,.nav-tabs-justified>.active>a:focus,.nav-tabs-justified>.active>a:hover{border:1px solid #ddd}@media (min-width:768px){.nav-justified>li{display:table-cell;width:1%}.nav-justified>li>a{margin-bottom:0}.nav-tabs-justified>li>a{border-bottom:1px solid #ddd;border-radius:2px 2px 0 0}.nav-tabs-justified>.active>a,.nav-tabs-justified>.active>a:focus,.nav-tabs-justified>.active>a:hover{border-bottom-color:#fff}}.tab-content>.tab-pane{display:none}.tab-content>.active{display:block}.nav-tabs .dropdown-menu{margin-top:-1px;border-top-right-radius:0;border-top-left-radius:0}.navbar{position:relative;min-height:30px;margin-bottom:18px;border:1px solid transparent}.navbar-collapse{overflow-x:visible;padding-right:0;padding-left:0;border-top:1px solid transparent;box-shadow:inset 0 1px 0 rgba(255,255,255,.1);-webkit-overflow-scrolling:touch}.navbar-collapse.in{overflow-y:auto}.navbar-fixed-bottom .navbar-collapse,.navbar-fixed-top .navbar-collapse{max-height:340px}@media (max-device-width:540px)and (orientation:landscape){.navbar-fixed-bottom .navbar-collapse,.navbar-fixed-top .navbar-collapse{max-height:200px}}.container-fluid>.navbar-collapse,.container-fluid>.navbar-header,.container>.navbar-collapse,.container>.navbar-header{margin-right:0;margin-left:0}.navbar-static-top{z-index:1000;border-width:0 0 1px}.navbar-fixed-bottom,.navbar-fixed-top{position:fixed;right:0;left:0;z-index:1030}@media (min-width:541px){.navbar{border-radius:2px}.navbar-header{float:left}.navbar-collapse{width:auto;border-top:0;box-shadow:none}.navbar-collapse.collapse{display:block!important;height:auto!important;padding-bottom:0;overflow:visible!important}.navbar-collapse.in{overflow-y:visible}.navbar-fixed-bottom .navbar-collapse,.navbar-fixed-top .navbar-collapse,.navbar-static-top .navbar-collapse{padding-left:0;padding-right:0}.container-fluid>.navbar-collapse,.container-fluid>.navbar-header,.container>.navbar-collapse,.container>.navbar-header{margin-right:0;margin-left:0}.navbar-fixed-bottom,.navbar-fixed-top,.navbar-static-top{border-radius:0}}.navbar-fixed-top{top:0;border-width:0 0 1px}.navbar-fixed-bottom{bottom:0;margin-bottom:0;border-width:1px 0 0}.navbar-brand{float:left;padding:6px 0;font-size:17px;line-height:18px;height:30px}.navbar-brand:focus,.navbar-brand:hover{text-decoration:none}.navbar-brand>img{display:block}.navbar-toggle{position:relative;float:right;margin-right:0;padding:9px 10px;margin-top:-2px;margin-bottom:-2px;background-color:transparent;background-image:none;border:1px solid transparent;border-radius:2px}.navbar-toggle:focus{outline:0}.navbar-toggle .icon-bar{display:block;width:22px;height:2px;border-radius:1px}.navbar-toggle .icon-bar+.icon-bar{margin-top:4px}@media (min-width:541px){.navbar>.container .navbar-brand,.navbar>.container-fluid .navbar-brand{margin-left:0}.navbar-toggle{display:none}}.navbar-nav{margin:3px 0}.navbar-nav>li>a{padding-top:10px;padding-bottom:10px;line-height:18px}@media (max-width:540px){.navbar-nav .open .dropdown-menu{position:static;float:none;width:auto;margin-top:0;background-color:transparent;border:0;box-shadow:none}.navbar-nav .open .dropdown-menu .dropdown-header,.navbar-nav .open .dropdown-menu>li>a{padding:5px 15px 5px 25px}.navbar-nav .open .dropdown-menu>li>a{line-height:18px}.navbar-nav .open .dropdown-menu>li>a:focus,.navbar-nav .open .dropdown-menu>li>a:hover{background-image:none}}@media (min-width:541px){.navbar-nav{float:left;margin:0}.navbar-nav>li{float:left}.navbar-nav>li>a{padding-top:6px;padding-bottom:6px}}.navbar-form{padding:10px 0;border-top:1px solid transparent;border-bottom:1px solid transparent;-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,.1),0 1px 0 rgba(255,255,255,.1);box-shadow:inset 0 1px 0 rgba(255,255,255,.1),0 1px 0 rgba(255,255,255,.1);margin:-1px 0}@media (min-width:768px){.navbar-form .form-group{display:inline-block;margin-bottom:0;vertical-align:middle}.navbar-form .form-control{display:inline-block;width:auto;vertical-align:middle}.navbar-form .form-control-static{display:inline-block}.navbar-form .input-group{display:inline-table;vertical-align:middle}.navbar-form .input-group .form-control,.navbar-form .input-group .input-group-addon,.navbar-form .input-group .input-group-btn{width:auto}.navbar-form .input-group>.form-control{width:100%}.navbar-form .control-label{margin-bottom:0;vertical-align:middle}.navbar-form .checkbox,.navbar-form .radio{display:inline-block;margin-top:0;margin-bottom:0;vertical-align:middle}.navbar-form .checkbox label,.navbar-form .radio label{padding-left:0}.navbar-form .checkbox input[type=checkbox],.navbar-form .radio input[type=radio]{position:relative;margin-left:0}.navbar-form .has-feedback .form-control-feedback{top:0}}@media (max-width:540px){.navbar-form .form-group{margin-bottom:5px}.navbar-form .form-group:last-child{margin-bottom:0}}.navbar-nav>li>.dropdown-menu{margin-top:0;border-top-right-radius:0;border-top-left-radius:0}.navbar-fixed-bottom .navbar-nav>li>.dropdown-menu{margin-bottom:0;border-radius:2px 2px 0 0}.navbar-btn{margin-top:-1px;margin-bottom:-1px}.navbar-btn.btn-sm{margin-top:0;margin-bottom:0}.navbar-btn.btn-xs{margin-top:4px;margin-bottom:4px}.navbar-text{margin-top:6px;margin-bottom:6px}@media (min-width:541px){.navbar-form{width:auto;border:0;margin-left:0;margin-right:0;padding-top:0;padding-bottom:0;-webkit-box-shadow:none;box-shadow:none}.navbar-text{float:left;margin-left:0;margin-right:0}.navbar-left{float:left!important;float:left}.navbar-right{float:right!important;float:right;margin-right:0}.navbar-right~.navbar-right{margin-right:0}}.navbar-default{background-color:#f8f8f8;border-color:#e7e7e7}.navbar-default .navbar-brand{color:#777}.navbar-default .navbar-brand:focus,.navbar-default .navbar-brand:hover{color:#5e5e5e;background-color:transparent}.navbar-default .navbar-nav>li>a,.navbar-default .navbar-text{color:#777}.navbar-default .navbar-nav>li>a:focus,.navbar-default .navbar-nav>li>a:hover{color:#333;background-color:transparent}.navbar-default .navbar-nav>.active>a,.navbar-default .navbar-nav>.active>a:focus,.navbar-default .navbar-nav>.active>a:hover{color:#555;background-color:#e7e7e7}.navbar-default .navbar-nav>.disabled>a,.navbar-default .navbar-nav>.disabled>a:focus,.navbar-default .navbar-nav>.disabled>a:hover{color:#ccc;background-color:transparent}.navbar-default .navbar-toggle{border-color:#ddd}.navbar-default .navbar-toggle:focus,.navbar-default .navbar-toggle:hover{background-color:#ddd}.navbar-default .navbar-toggle .icon-bar{background-color:#888}.navbar-default .navbar-collapse,.navbar-default .navbar-form{border-color:#e7e7e7}.navbar-default .navbar-nav>.open>a,.navbar-default .navbar-nav>.open>a:focus,.navbar-default .navbar-nav>.open>a:hover{background-color:#e7e7e7;color:#555}@media (max-width:540px){.navbar-default .navbar-nav .open .dropdown-menu>li>a{color:#777}.navbar-default .navbar-nav .open .dropdown-menu>li>a:focus,.navbar-default .navbar-nav .open .dropdown-menu>li>a:hover{color:#333;background-color:transparent}.navbar-default .navbar-nav .open .dropdown-menu>.active>a,.navbar-default .navbar-nav .open .dropdown-menu>.active>a:focus,.navbar-default .navbar-nav .open .dropdown-menu>.active>a:hover{color:#555;background-color:#e7e7e7}.navbar-default .navbar-nav .open .dropdown-menu>.disabled>a,.navbar-default .navbar-nav .open .dropdown-menu>.disabled>a:focus,.navbar-default .navbar-nav .open .dropdown-menu>.disabled>a:hover{color:#ccc;background-color:transparent}}.navbar-default .navbar-link{color:#777}.navbar-default .navbar-link:hover{color:#333}.navbar-default .btn-link{color:#777}.navbar-default .btn-link:focus,.navbar-default .btn-link:hover{color:#333}.navbar-default .btn-link[disabled]:focus,.navbar-default .btn-link[disabled]:hover,fieldset[disabled] .navbar-default .btn-link:focus,fieldset[disabled] .navbar-default .btn-link:hover{color:#ccc}.navbar-inverse{background-color:#222;border-color:#080808}.navbar-inverse .navbar-brand{color:#9d9d9d}.navbar-inverse .navbar-brand:focus,.navbar-inverse .navbar-brand:hover{color:#fff;background-color:transparent}.navbar-inverse .navbar-nav>li>a,.navbar-inverse .navbar-text{color:#9d9d9d}.navbar-inverse .navbar-nav>li>a:focus,.navbar-inverse .navbar-nav>li>a:hover{color:#fff;background-color:transparent}.navbar-inverse .navbar-nav>.active>a,.navbar-inverse .navbar-nav>.active>a:focus,.navbar-inverse .navbar-nav>.active>a:hover{color:#fff;background-color:#080808}.navbar-inverse .navbar-nav>.disabled>a,.navbar-inverse .navbar-nav>.disabled>a:focus,.navbar-inverse .navbar-nav>.disabled>a:hover{color:#444;background-color:transparent}.navbar-inverse .navbar-toggle{border-color:#333}.navbar-inverse .navbar-toggle:focus,.navbar-inverse .navbar-toggle:hover{background-color:#333}.navbar-inverse .navbar-toggle .icon-bar{background-color:#fff}.navbar-inverse .navbar-collapse,.navbar-inverse .navbar-form{border-color:#101010}.navbar-inverse .navbar-nav>.open>a,.navbar-inverse .navbar-nav>.open>a:focus,.navbar-inverse .navbar-nav>.open>a:hover{background-color:#080808;color:#fff}@media (max-width:540px){.navbar-inverse .navbar-nav .open .dropdown-menu>.dropdown-header{border-color:#080808}.navbar-inverse .navbar-nav .open .dropdown-menu .divider{background-color:#080808}.navbar-inverse .navbar-nav .open .dropdown-menu>li>a{color:#9d9d9d}.navbar-inverse .navbar-nav .open .dropdown-menu>li>a:focus,.navbar-inverse .navbar-nav .open .dropdown-menu>li>a:hover{color:#fff;background-color:transparent}.navbar-inverse .navbar-nav .open .dropdown-menu>.active>a,.navbar-inverse .navbar-nav .open .dropdown-menu>.active>a:focus,.navbar-inverse .navbar-nav .open .dropdown-menu>.active>a:hover{color:#fff;background-color:#080808}.navbar-inverse .navbar-nav .open .dropdown-menu>.disabled>a,.navbar-inverse .navbar-nav .open .dropdown-menu>.disabled>a:focus,.navbar-inverse .navbar-nav .open .dropdown-menu>.disabled>a:hover{color:#444;background-color:transparent}}.navbar-inverse .navbar-link{color:#9d9d9d}.navbar-inverse .navbar-link:hover{color:#fff}.navbar-inverse .btn-link{color:#9d9d9d}.navbar-inverse .btn-link:focus,.navbar-inverse .btn-link:hover{color:#fff}.navbar-inverse .btn-link[disabled]:focus,.navbar-inverse .btn-link[disabled]:hover,fieldset[disabled] .navbar-inverse .btn-link:focus,fieldset[disabled] .navbar-inverse .btn-link:hover{color:#444}.breadcrumb{padding:8px 15px;margin-bottom:18px;list-style:none;background-color:#f5f5f5;border-radius:2px}.breadcrumb>li{display:inline-block}.breadcrumb>li+li:before{content:"/\00a0";padding:0 5px;color:#5e5e5e}.breadcrumb>.active{color:#777}.pagination{display:inline-block;padding-left:0;margin:18px 0;border-radius:2px}.pagination>li{display:inline}.pagination>li>a,.pagination>li>span{position:relative;float:left;padding:6px 12px;line-height:1.42857143;text-decoration:none;color:#337ab7;background-color:#fff;border:1px solid #ddd;margin-left:-1px}.pagination>li:first-child>a,.pagination>li:first-child>span{margin-left:0;border-bottom-left-radius:2px;border-top-left-radius:2px}.pagination>li:last-child>a,.pagination>li:last-child>span{border-bottom-right-radius:2px;border-top-right-radius:2px}.pagination>li>a:focus,.pagination>li>a:hover,.pagination>li>span:focus,.pagination>li>span:hover{color:#23527c;background-color:#eee;border-color:#ddd}.pagination>.active>a,.pagination>.active>a:focus,.pagination>.active>a:hover,.pagination>.active>span,.pagination>.active>span:focus,.pagination>.active>span:hover{z-index:2;color:#fff;background-color:#337ab7;border-color:#337ab7;cursor:default}.pagination>.disabled>a,.pagination>.disabled>a:focus,.pagination>.disabled>a:hover,.pagination>.disabled>span,.pagination>.disabled>span:focus,.pagination>.disabled>span:hover{color:#777;background-color:#fff;border-color:#ddd;cursor:not-allowed}.pagination-lg>li>a,.pagination-lg>li>span{padding:10px 16px;font-size:17px}.pagination-lg>li:first-child>a,.pagination-lg>li:first-child>span{border-bottom-left-radius:3px;border-top-left-radius:3px}.pagination-lg>li:last-child>a,.pagination-lg>li:last-child>span{border-bottom-right-radius:3px;border-top-right-radius:3px}.pagination-sm>li>a,.pagination-sm>li>span{padding:5px 10px;font-size:12px}.pagination-sm>li:first-child>a,.pagination-sm>li:first-child>span{border-bottom-left-radius:1px;border-top-left-radius:1px}.pagination-sm>li:last-child>a,.pagination-sm>li:last-child>span{border-bottom-right-radius:1px;border-top-right-radius:1px}.pager{padding-left:0;margin:18px 0;list-style:none;text-align:center}.pager li{display:inline}.pager li>a,.pager li>span{display:inline-block;padding:5px 14px;background-color:#fff;border:1px solid #ddd;border-radius:15px}.pager li>a:focus,.pager li>a:hover{text-decoration:none;background-color:#eee}.pager .next>a,.pager .next>span{float:right}.pager .previous>a,.pager .previous>span{float:left}.pager .disabled>a,.pager .disabled>a:focus,.pager .disabled>a:hover,.pager .disabled>span{color:#777;background-color:#fff;cursor:not-allowed}.label{display:inline;padding:.2em .6em .3em;font-size:75%;font-weight:700;line-height:1;color:#fff;text-align:center;white-space:nowrap;vertical-align:baseline;border-radius:.25em}a.label:focus,a.label:hover{color:#fff;text-decoration:none;cursor:pointer}.label:empty{display:none}.btn .label{position:relative;top:-1px}.label-default{background-color:#777}.label-default[href]:focus,.label-default[href]:hover{background-color:#5e5e5e}.label-primary{background-color:#337ab7}.label-primary[href]:focus,.label-primary[href]:hover{background-color:#286090}.label-success{background-color:#5cb85c}.label-success[href]:focus,.label-success[href]:hover{background-color:#449d44}.label-info{background-color:#5bc0de}.label-info[href]:focus,.label-info[href]:hover{background-color:#31b0d5}.label-warning{background-color:#f0ad4e}.label-warning[href]:focus,.label-warning[href]:hover{background-color:#ec971f}.label-danger{background-color:#d9534f}.label-danger[href]:focus,.label-danger[href]:hover{background-color:#c9302c}.badge{display:inline-block;min-width:10px;padding:3px 7px;font-size:12px;font-weight:700;color:#fff;line-height:1;vertical-align:baseline;white-space:nowrap;text-align:center;background-color:#777;border-radius:10px}.badge:empty{display:none}.btn .badge{position:relative;top:-1px}.btn-group-xs>.btn .badge,.btn-xs .badge{top:0;padding:1px 5px}a.badge:focus,a.badge:hover{color:#fff;text-decoration:none;cursor:pointer}.list-group-item.active>.badge,.nav-pills>.active>a>.badge{color:#337ab7;background-color:#fff}.list-group-item>.badge{float:right}.list-group-item>.badge+.badge{margin-right:5px}.nav-pills>li>a>.badge{margin-left:3px}.jumbotron{padding:30px 15px;margin-bottom:30px;color:inherit;background-color:#eee}.jumbotron .h1,.jumbotron h1{color:inherit}.jumbotron p{margin-bottom:15px;font-size:20px;font-weight:200}.jumbotron>hr{border-top-color:#d5d5d5}.container .jumbotron,.container-fluid .jumbotron{border-radius:3px}.jumbotron .container{max-width:100%}@media screen and (min-width:768px){.jumbotron{padding:48px 0}.container .jumbotron,.container-fluid .jumbotron{padding-left:60px;padding-right:60px}.jumbotron .h1,.jumbotron h1{font-size:58.5px}}.thumbnail{display:block;padding:4px;margin-bottom:18px;line-height:1.42857143;background-color:#fff;border:1px solid #ddd;border-radius:2px;-webkit-transition:border .2s ease-in-out;-o-transition:border .2s ease-in-out;transition:border .2s ease-in-out}.thumbnail a>img,.thumbnail>img{margin-left:auto;margin-right:auto}a.thumbnail.active,a.thumbnail:focus,a.thumbnail:hover{border-color:#337ab7}.thumbnail .caption{padding:9px;color:#000}.alert{padding:15px;margin-bottom:18px;border:1px solid transparent;border-radius:2px}.alert h4{margin-top:0;color:inherit}.alert .alert-link{font-weight:700}.alert>p,.alert>ul{margin-bottom:0}.alert>p+p{margin-top:5px}.alert-dismissable,.alert-dismissible{padding-right:35px}.alert-dismissable .close,.alert-dismissible .close{position:relative;top:-2px;right:-21px;color:inherit}.alert-success{background-color:#dff0d8;border-color:#d6e9c6;color:#3c763d}.alert-success hr{border-top-color:#c9e2b3}.alert-success .alert-link{color:#2b542c}.alert-info{background-color:#d9edf7;border-color:#bce8f1;color:#31708f}.alert-info hr{border-top-color:#a6e1ec}.alert-info .alert-link{color:#245269}.alert-warning{background-color:#fcf8e3;border-color:#faebcc;color:#8a6d3b}.alert-warning hr{border-top-color:#f7e1b5}.alert-warning .alert-link{color:#66512c}.alert-danger{background-color:#f2dede;border-color:#ebccd1;color:#a94442}.alert-danger hr{border-top-color:#e4b9c0}.alert-danger .alert-link{color:#843534}@-webkit-keyframes progress-bar-stripes{from{background-position:40px 0}to{background-position:0 0}}@keyframes progress-bar-stripes{from{background-position:40px 0}to{background-position:0 0}}.progress{overflow:hidden;height:18px;margin-bottom:18px;background-color:#f5f5f5;border-radius:2px;-webkit-box-shadow:inset 0 1px 2px rgba(0,0,0,.1);box-shadow:inset 0 1px 2px rgba(0,0,0,.1)}.progress-bar{float:left;width:0;height:100%;font-size:12px;line-height:18px;color:#fff;text-align:center;background-color:#337ab7;-webkit-box-shadow:inset 0 -1px 0 rgba(0,0,0,.15);box-shadow:inset 0 -1px 0 rgba(0,0,0,.15);-webkit-transition:width .6s ease;-o-transition:width .6s ease;transition:width .6s ease}.progress-bar-striped,.progress-striped .progress-bar{background-image:-webkit-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:-o-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-size:40px 40px}.progress-bar.active,.progress.active .progress-bar{-webkit-animation:progress-bar-stripes 2s linear infinite;-o-animation:progress-bar-stripes 2s linear infinite;animation:progress-bar-stripes 2s linear infinite}.progress-bar-success{background-color:#5cb85c}.progress-striped .progress-bar-success{background-image:-webkit-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:-o-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent)}.progress-bar-info{background-color:#5bc0de}.progress-striped .progress-bar-info{background-image:-webkit-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:-o-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent)}.progress-bar-warning{background-color:#f0ad4e}.progress-striped .progress-bar-warning{background-image:-webkit-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:-o-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent)}.progress-bar-danger{background-color:#d9534f}.progress-striped .progress-bar-danger{background-image:-webkit-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:-o-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent)}.media{margin-top:15px}.media:first-child{margin-top:0}.media,.media-body{zoom:1;overflow:hidden}.media-body{width:10000px}.media-object{display:block}.media-right,.media>.pull-right{padding-left:10px}.media-left,.media>.pull-left{padding-right:10px}.media-body,.media-left,.media-right{display:table-cell;vertical-align:top}.media-middle{vertical-align:middle}.media-bottom{vertical-align:bottom}.media-heading{margin-top:0;margin-bottom:5px}.media-list{padding-left:0;list-style:none}.list-group{margin-bottom:20px;padding-left:0}.list-group-item{position:relative;display:block;padding:10px 15px;margin-bottom:-1px;background-color:#fff;border:1px solid #ddd}.list-group-item:first-child{border-top-right-radius:2px;border-top-left-radius:2px}.list-group-item:last-child{margin-bottom:0;border-bottom-right-radius:2px;border-bottom-left-radius:2px}a.list-group-item{color:#555}a.list-group-item .list-group-item-heading{color:#333}a.list-group-item:focus,a.list-group-item:hover{text-decoration:none;color:#555;background-color:#f5f5f5}.list-group-item.disabled,.list-group-item.disabled:focus,.list-group-item.disabled:hover{background-color:#eee;color:#777;cursor:not-allowed}.list-group-item.disabled .list-group-item-heading,.list-group-item.disabled:focus .list-group-item-heading,.list-group-item.disabled:hover .list-group-item-heading{color:inherit}.list-group-item.disabled .list-group-item-text,.list-group-item.disabled:focus .list-group-item-text,.list-group-item.disabled:hover .list-group-item-text{color:#777}.list-group-item.active,.list-group-item.active:focus,.list-group-item.active:hover{z-index:2;color:#fff;background-color:#337ab7;border-color:#337ab7}.list-group-item.active .list-group-item-heading,.list-group-item.active .list-group-item-heading>.small,.list-group-item.active .list-group-item-heading>small,.list-group-item.active:focus .list-group-item-heading,.list-group-item.active:focus .list-group-item-heading>.small,.list-group-item.active:focus .list-group-item-heading>small,.list-group-item.active:hover .list-group-item-heading,.list-group-item.active:hover .list-group-item-heading>.small,.list-group-item.active:hover .list-group-item-heading>small{color:inherit}.list-group-item.active .list-group-item-text,.list-group-item.active:focus .list-group-item-text,.list-group-item.active:hover .list-group-item-text{color:#c7ddef}.list-group-item-success{color:#3c763d;background-color:#dff0d8}a.list-group-item-success{color:#3c763d}a.list-group-item-success .list-group-item-heading{color:inherit}a.list-group-item-success:focus,a.list-group-item-success:hover{color:#3c763d;background-color:#d0e9c6}a.list-group-item-success.active,a.list-group-item-success.active:focus,a.list-group-item-success.active:hover{color:#fff;background-color:#3c763d;border-color:#3c763d}.list-group-item-info{color:#31708f;background-color:#d9edf7}a.list-group-item-info{color:#31708f}a.list-group-item-info .list-group-item-heading{color:inherit}a.list-group-item-info:focus,a.list-group-item-info:hover{color:#31708f;background-color:#c4e3f3}a.list-group-item-info.active,a.list-group-item-info.active:focus,a.list-group-item-info.active:hover{color:#fff;background-color:#31708f;border-color:#31708f}.list-group-item-warning{color:#8a6d3b;background-color:#fcf8e3}a.list-group-item-warning{color:#8a6d3b}a.list-group-item-warning .list-group-item-heading{color:inherit}a.list-group-item-warning:focus,a.list-group-item-warning:hover{color:#8a6d3b;background-color:#faf2cc}a.list-group-item-warning.active,a.list-group-item-warning.active:focus,a.list-group-item-warning.active:hover{color:#fff;background-color:#8a6d3b;border-color:#8a6d3b}.list-group-item-danger{color:#a94442;background-color:#f2dede}a.list-group-item-danger{color:#a94442}a.list-group-item-danger .list-group-item-heading{color:inherit}a.list-group-item-danger:focus,a.list-group-item-danger:hover{color:#a94442;background-color:#ebcccc}a.list-group-item-danger.active,a.list-group-item-danger.active:focus,a.list-group-item-danger.active:hover{color:#fff;background-color:#a94442;border-color:#a94442}.list-group-item-heading{margin-top:0;margin-bottom:5px}.list-group-item-text{margin-bottom:0;line-height:1.3}.panel{margin-bottom:18px;background-color:#fff;border:1px solid transparent;border-radius:2px;-webkit-box-shadow:0 1px 1px rgba(0,0,0,.05);box-shadow:0 1px 1px rgba(0,0,0,.05)}.panel-body{padding:15px}.panel-heading{padding:10px 15px;border-bottom:1px solid transparent;border-top-right-radius:1px;border-top-left-radius:1px}.panel-heading>.dropdown .dropdown-toggle{color:inherit}.panel-title{margin-top:0;margin-bottom:0;font-size:15px;color:inherit}.panel-title>.small,.panel-title>.small>a,.panel-title>a,.panel-title>small,.panel-title>small>a{color:inherit}.panel-footer{padding:10px 15px;background-color:#f5f5f5;border-top:1px solid #ddd;border-bottom-right-radius:1px;border-bottom-left-radius:1px}.panel>.list-group,.panel>.panel-collapse>.list-group{margin-bottom:0}.panel>.list-group .list-group-item,.panel>.panel-collapse>.list-group .list-group-item{border-width:1px 0;border-radius:0}.panel>.list-group:first-child .list-group-item:first-child,.panel>.panel-collapse>.list-group:first-child .list-group-item:first-child{border-top:0;border-top-right-radius:1px;border-top-left-radius:1px}.panel>.list-group:last-child .list-group-item:last-child,.panel>.panel-collapse>.list-group:last-child .list-group-item:last-child{border-bottom:0;border-bottom-right-radius:1px;border-bottom-left-radius:1px}.list-group+.panel-footer,.panel-heading+.list-group .list-group-item:first-child{border-top-width:0}.panel>.panel-collapse>.table,.panel>.table,.panel>.table-responsive>.table{margin-bottom:0}.panel>.panel-collapse>.table caption,.panel>.table caption,.panel>.table-responsive>.table caption{padding-left:15px;padding-right:15px}.panel>.table-responsive:first-child>.table:first-child,.panel>.table:first-child{border-top-right-radius:1px;border-top-left-radius:1px}.panel>.table-responsive:first-child>.table:first-child>tbody:first-child>tr:first-child,.panel>.table-responsive:first-child>.table:first-child>thead:first-child>tr:first-child,.panel>.table:first-child>tbody:first-child>tr:first-child,.panel>.table:first-child>thead:first-child>tr:first-child{border-top-left-radius:1px;border-top-right-radius:1px}.panel>.table-responsive:first-child>.table:first-child>tbody:first-child>tr:first-child td:first-child,.panel>.table-responsive:first-child>.table:first-child>tbody:first-child>tr:first-child th:first-child,.panel>.table-responsive:first-child>.table:first-child>thead:first-child>tr:first-child td:first-child,.panel>.table-responsive:first-child>.table:first-child>thead:first-child>tr:first-child th:first-child,.panel>.table:first-child>tbody:first-child>tr:first-child td:first-child,.panel>.table:first-child>tbody:first-child>tr:first-child th:first-child,.panel>.table:first-child>thead:first-child>tr:first-child td:first-child,.panel>.table:first-child>thead:first-child>tr:first-child th:first-child{border-top-left-radius:1px}.panel>.table-responsive:first-child>.table:first-child>tbody:first-child>tr:first-child td:last-child,.panel>.table-responsive:first-child>.table:first-child>tbody:first-child>tr:first-child th:last-child,.panel>.table-responsive:first-child>.table:first-child>thead:first-child>tr:first-child td:last-child,.panel>.table-responsive:first-child>.table:first-child>thead:first-child>tr:first-child th:last-child,.panel>.table:first-child>tbody:first-child>tr:first-child td:last-child,.panel>.table:first-child>tbody:first-child>tr:first-child th:last-child,.panel>.table:first-child>thead:first-child>tr:first-child td:last-child,.panel>.table:first-child>thead:first-child>tr:first-child th:last-child{border-top-right-radius:1px}.panel>.table-responsive:last-child>.table:last-child,.panel>.table:last-child{border-bottom-right-radius:1px;border-bottom-left-radius:1px}.panel>.table-responsive:last-child>.table:last-child>tbody:last-child>tr:last-child,.panel>.table-responsive:last-child>.table:last-child>tfoot:last-child>tr:last-child,.panel>.table:last-child>tbody:last-child>tr:last-child,.panel>.table:last-child>tfoot:last-child>tr:last-child{border-bottom-left-radius:1px;border-bottom-right-radius:1px}.panel>.table-responsive:last-child>.table:last-child>tbody:last-child>tr:last-child td:first-child,.panel>.table-responsive:last-child>.table:last-child>tbody:last-child>tr:last-child th:first-child,.panel>.table-responsive:last-child>.table:last-child>tfoot:last-child>tr:last-child td:first-child,.panel>.table-responsive:last-child>.table:last-child>tfoot:last-child>tr:last-child th:first-child,.panel>.table:last-child>tbody:last-child>tr:last-child td:first-child,.panel>.table:last-child>tbody:last-child>tr:last-child th:first-child,.panel>.table:last-child>tfoot:last-child>tr:last-child td:first-child,.panel>.table:last-child>tfoot:last-child>tr:last-child th:first-child{border-bottom-left-radius:1px}.panel>.table-responsive:last-child>.table:last-child>tbody:last-child>tr:last-child td:last-child,.panel>.table-responsive:last-child>.table:last-child>tbody:last-child>tr:last-child th:last-child,.panel>.table-responsive:last-child>.table:last-child>tfoot:last-child>tr:last-child td:last-child,.panel>.table-responsive:last-child>.table:last-child>tfoot:last-child>tr:last-child th:last-child,.panel>.table:last-child>tbody:last-child>tr:last-child td:last-child,.panel>.table:last-child>tbody:last-child>tr:last-child th:last-child,.panel>.table:last-child>tfoot:last-child>tr:last-child td:last-child,.panel>.table:last-child>tfoot:last-child>tr:last-child th:last-child{border-bottom-right-radius:1px}.panel>.panel-body+.table,.panel>.panel-body+.table-responsive,.panel>.table+.panel-body,.panel>.table-responsive+.panel-body{border-top:1px solid #ddd}.panel>.table>tbody:first-child>tr:first-child td,.panel>.table>tbody:first-child>tr:first-child th{border-top:0}.panel>.table-bordered,.panel>.table-responsive>.table-bordered{border:0}.panel>.table-bordered>tbody>tr>td:first-child,.panel>.table-bordered>tbody>tr>th:first-child,.panel>.table-bordered>tfoot>tr>td:first-child,.panel>.table-bordered>tfoot>tr>th:first-child,.panel>.table-bordered>thead>tr>td:first-child,.panel>.table-bordered>thead>tr>th:first-child,.panel>.table-responsive>.table-bordered>tbody>tr>td:first-child,.panel>.table-responsive>.table-bordered>tbody>tr>th:first-child,.panel>.table-responsive>.table-bordered>tfoot>tr>td:first-child,.panel>.table-responsive>.table-bordered>tfoot>tr>th:first-child,.panel>.table-responsive>.table-bordered>thead>tr>td:first-child,.panel>.table-responsive>.table-bordered>thead>tr>th:first-child{border-left:0}.panel>.table-bordered>tbody>tr>td:last-child,.panel>.table-bordered>tbody>tr>th:last-child,.panel>.table-bordered>tfoot>tr>td:last-child,.panel>.table-bordered>tfoot>tr>th:last-child,.panel>.table-bordered>thead>tr>td:last-child,.panel>.table-bordered>thead>tr>th:last-child,.panel>.table-responsive>.table-bordered>tbody>tr>td:last-child,.panel>.table-responsive>.table-bordered>tbody>tr>th:last-child,.panel>.table-responsive>.table-bordered>tfoot>tr>td:last-child,.panel>.table-responsive>.table-bordered>tfoot>tr>th:last-child,.panel>.table-responsive>.table-bordered>thead>tr>td:last-child,.panel>.table-responsive>.table-bordered>thead>tr>th:last-child{border-right:0}.panel>.table-bordered>tbody>tr:first-child>td,.panel>.table-bordered>tbody>tr:first-child>th,.panel>.table-bordered>tbody>tr:last-child>td,.panel>.table-bordered>tbody>tr:last-child>th,.panel>.table-bordered>tfoot>tr:last-child>td,.panel>.table-bordered>tfoot>tr:last-child>th,.panel>.table-bordered>thead>tr:first-child>td,.panel>.table-bordered>thead>tr:first-child>th,.panel>.table-responsive>.table-bordered>tbody>tr:first-child>td,.panel>.table-responsive>.table-bordered>tbody>tr:first-child>th,.panel>.table-responsive>.table-bordered>tbody>tr:last-child>td,.panel>.table-responsive>.table-bordered>tbody>tr:last-child>th,.panel>.table-responsive>.table-bordered>tfoot>tr:last-child>td,.panel>.table-responsive>.table-bordered>tfoot>tr:last-child>th,.panel>.table-responsive>.table-bordered>thead>tr:first-child>td,.panel>.table-responsive>.table-bordered>thead>tr:first-child>th{border-bottom:0}.panel>.table-responsive{border:0;margin-bottom:0}.panel-group{margin-bottom:18px}.panel-group .panel{margin-bottom:0;border-radius:2px}.panel-group .panel+.panel{margin-top:5px}.panel-group .panel-heading{border-bottom:0}.panel-group .panel-heading+.panel-collapse>.list-group,.panel-group .panel-heading+.panel-collapse>.panel-body{border-top:1px solid #ddd}.panel-group .panel-footer{border-top:0}.panel-group .panel-footer+.panel-collapse .panel-body{border-bottom:1px solid #ddd}.panel-default{border-color:#ddd}.panel-default>.panel-heading{color:#333;background-color:#f5f5f5;border-color:#ddd}.panel-default>.panel-heading+.panel-collapse>.panel-body{border-top-color:#ddd}.panel-default>.panel-heading .badge{color:#f5f5f5;background-color:#333}.panel-default>.panel-footer+.panel-collapse>.panel-body{border-bottom-color:#ddd}.panel-primary{border-color:#337ab7}.panel-primary>.panel-heading{color:#fff;background-color:#337ab7;border-color:#337ab7}.panel-primary>.panel-heading+.panel-collapse>.panel-body{border-top-color:#337ab7}.panel-primary>.panel-heading .badge{color:#337ab7;background-color:#fff}.panel-primary>.panel-footer+.panel-collapse>.panel-body{border-bottom-color:#337ab7}.panel-success{border-color:#d6e9c6}.panel-success>.panel-heading{color:#3c763d;background-color:#dff0d8;border-color:#d6e9c6}.panel-success>.panel-heading+.panel-collapse>.panel-body{border-top-color:#d6e9c6}.panel-success>.panel-heading .badge{color:#dff0d8;background-color:#3c763d}.panel-success>.panel-footer+.panel-collapse>.panel-body{border-bottom-color:#d6e9c6}.panel-info{border-color:#bce8f1}.panel-info>.panel-heading{color:#31708f;background-color:#d9edf7;border-color:#bce8f1}.panel-info>.panel-heading+.panel-collapse>.panel-body{border-top-color:#bce8f1}.panel-info>.panel-heading .badge{color:#d9edf7;background-color:#31708f}.panel-info>.panel-footer+.panel-collapse>.panel-body{border-bottom-color:#bce8f1}.panel-warning{border-color:#faebcc}.panel-warning>.panel-heading{color:#8a6d3b;background-color:#fcf8e3;border-color:#faebcc}.panel-warning>.panel-heading+.panel-collapse>.panel-body{border-top-color:#faebcc}.panel-warning>.panel-heading .badge{color:#fcf8e3;background-color:#8a6d3b}.panel-warning>.panel-footer+.panel-collapse>.panel-body{border-bottom-color:#faebcc}.panel-danger{border-color:#ebccd1}.panel-danger>.panel-heading{color:#a94442;background-color:#f2dede;border-color:#ebccd1}.panel-danger>.panel-heading+.panel-collapse>.panel-body{border-top-color:#ebccd1}.panel-danger>.panel-heading .badge{color:#f2dede;background-color:#a94442}.panel-danger>.panel-footer+.panel-collapse>.panel-body{border-bottom-color:#ebccd1}.embed-responsive{position:relative;display:block;height:0;padding:0;overflow:hidden}.embed-responsive .embed-responsive-item,.embed-responsive embed,.embed-responsive iframe,.embed-responsive object,.embed-responsive video{position:absolute;top:0;left:0;bottom:0;height:100%;width:100%;border:0}.embed-responsive-16by9{padding-bottom:56.25%}.embed-responsive-4by3{padding-bottom:75%}.well{min-height:20px;padding:19px;margin-bottom:20px;background-color:#f5f5f5;border:1px solid #e3e3e3;border-radius:2px;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.05);box-shadow:inset 0 1px 1px rgba(0,0,0,.05)}.well blockquote{border-color:#ddd;border-color:rgba(0,0,0,.15)}.well-lg{padding:24px;border-radius:3px}.well-sm{padding:9px;border-radius:1px}.close{float:right;font-size:19.5px;font-weight:700;line-height:1;color:#000;text-shadow:0 1px 0 #fff;opacity:.2;filter:alpha(opacity=20)}.close:focus,.close:hover{color:#000;text-decoration:none;cursor:pointer;opacity:.5;filter:alpha(opacity=50)}button.close{padding:0;cursor:pointer;background:0 0;border:0;-webkit-appearance:none}.modal-open{overflow:hidden}.modal{display:none;overflow:hidden;position:fixed;top:0;right:0;bottom:0;left:0;z-index:1050;-webkit-overflow-scrolling:touch;outline:0}.modal.fade .modal-dialog{-webkit-transition:-webkit-transform .3s ease-out;-moz-transition:-moz-transform .3s ease-out;-o-transition:-o-transform .3s ease-out;transition:transform .3s ease-out}.modal.in .modal-dialog{-webkit-transform:translate(0,0);-ms-transform:translate(0,0);-o-transform:translate(0,0);transform:translate(0,0)}.modal-open .modal{overflow-x:hidden;overflow-y:auto}.modal-dialog{position:relative;width:auto;margin:10px}.modal-content{position:relative;background-color:#fff;border:1px solid #999;border:1px solid rgba(0,0,0,.2);border-radius:3px;-webkit-box-shadow:0 3px 9px rgba(0,0,0,.5);box-shadow:0 3px 9px rgba(0,0,0,.5);background-clip:padding-box;outline:0}.modal-backdrop{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1040;background-color:#000}.modal-backdrop.fade{opacity:0;filter:alpha(opacity=0)}.modal-backdrop.in{opacity:.5;filter:alpha(opacity=50)}.modal-header{padding:15px;border-bottom:1px solid #e5e5e5;min-height:16.43px}.modal-header .close{margin-top:-2px}.modal-title{margin:0;line-height:1.42857143}.modal-body{position:relative;padding:15px}.modal-footer{padding:15px;text-align:right;border-top:1px solid #e5e5e5}.modal-footer .btn+.btn{margin-left:5px;margin-bottom:0}.modal-footer .btn-group .btn+.btn{margin-left:-1px}.modal-footer .btn-block+.btn-block{margin-left:0}.modal-scrollbar-measure{position:absolute;top:-9999px;width:50px;height:50px;overflow:scroll}@media (min-width:768px){.modal-dialog{width:600px;margin:30px auto}.modal-content{-webkit-box-shadow:0 5px 15px rgba(0,0,0,.5);box-shadow:0 5px 15px rgba(0,0,0,.5)}.modal-sm{width:300px}}@media (min-width:992px){.modal-lg{width:900px}}.tooltip{position:absolute;z-index:1070;display:block;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:12px;font-weight:400;line-height:1.4;opacity:0;filter:alpha(opacity=0)}.tooltip.in{opacity:.9;filter:alpha(opacity=90)}.tooltip.top{margin-top:-3px;padding:5px 0}.tooltip.right{margin-left:3px;padding:0 5px}.tooltip.bottom{margin-top:3px;padding:5px 0}.tooltip.left{margin-left:-3px;padding:0 5px}.tooltip-inner{max-width:200px;padding:3px 8px;color:#fff;text-align:center;text-decoration:none;background-color:#000;border-radius:2px}.tooltip-arrow{position:absolute;width:0;height:0;border-color:transparent;border-style:solid}.tooltip.top .tooltip-arrow{bottom:0;left:50%;margin-left:-5px;border-width:5px 5px 0;border-top-color:#000}.tooltip.top-left .tooltip-arrow{bottom:0;right:5px;margin-bottom:-5px;border-width:5px 5px 0;border-top-color:#000}.tooltip.top-right .tooltip-arrow{bottom:0;left:5px;margin-bottom:-5px;border-width:5px 5px 0;border-top-color:#000}.tooltip.right .tooltip-arrow{top:50%;left:0;margin-top:-5px;border-width:5px 5px 5px 0;border-right-color:#000}.tooltip.left .tooltip-arrow{top:50%;right:0;margin-top:-5px;border-width:5px 0 5px 5px;border-left-color:#000}.tooltip.bottom .tooltip-arrow{top:0;left:50%;margin-left:-5px;border-width:0 5px 5px;border-bottom-color:#000}.tooltip.bottom-left .tooltip-arrow{top:0;right:5px;margin-top:-5px;border-width:0 5px 5px;border-bottom-color:#000}.tooltip.bottom-right .tooltip-arrow{top:0;left:5px;margin-top:-5px;border-width:0 5px 5px;border-bottom-color:#000}.popover{position:absolute;top:0;left:0;z-index:1060;display:none;max-width:276px;padding:1px;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:13px;font-weight:400;line-height:1.42857143;text-align:left;background-color:#fff;background-clip:padding-box;border:1px solid #ccc;border:1px solid rgba(0,0,0,.2);border-radius:3px;-webkit-box-shadow:0 5px 10px rgba(0,0,0,.2);box-shadow:0 5px 10px rgba(0,0,0,.2);white-space:normal}.popover.top{margin-top:-10px}.popover.right{margin-left:10px}.popover.bottom{margin-top:10px}.popover.left{margin-left:-10px}.popover-title{margin:0;padding:8px 14px;font-size:13px;background-color:#f7f7f7;border-bottom:1px solid #ebebeb;border-radius:2px 2px 0 0}.popover-content{padding:9px 14px}.popover>.arrow,.popover>.arrow:after{position:absolute;display:block;width:0;height:0;border-color:transparent;border-style:solid}.popover>.arrow{border-width:11px}.popover>.arrow:after{border-width:10px;content:""}.popover.top>.arrow{left:50%;margin-left:-11px;border-bottom-width:0;border-top-color:#999;border-top-color:rgba(0,0,0,.25);bottom:-11px}.popover.top>.arrow:after{content:" ";bottom:1px;margin-left:-10px;border-bottom-width:0;border-top-color:#fff}.popover.right>.arrow{top:50%;left:-11px;margin-top:-11px;border-left-width:0;border-right-color:#999;border-right-color:rgba(0,0,0,.25)}.popover.right>.arrow:after{content:" ";left:1px;bottom:-10px;border-left-width:0;border-right-color:#fff}.popover.bottom>.arrow{left:50%;margin-left:-11px;border-top-width:0;border-bottom-color:#999;border-bottom-color:rgba(0,0,0,.25);top:-11px}.popover.bottom>.arrow:after{content:" ";top:1px;margin-left:-10px;border-top-width:0;border-bottom-color:#fff}.popover.left>.arrow{top:50%;right:-11px;margin-top:-11px;border-right-width:0;border-left-color:#999;border-left-color:rgba(0,0,0,.25)}.popover.left>.arrow:after{content:" ";right:1px;border-right-width:0;border-left-color:#fff;bottom:-10px}.carousel{position:relative}.carousel-inner{position:relative;overflow:hidden;width:100%}.carousel-inner>.item{display:none;position:relative;-webkit-transition:.6s ease-in-out left;-o-transition:.6s ease-in-out left;transition:.6s ease-in-out left}.carousel-inner>.item>a>img,.carousel-inner>.item>img{line-height:1}@media all and (transform-3d),(-webkit-transform-3d){.carousel-inner>.item{-webkit-transition:-webkit-transform .6s ease-in-out;-moz-transition:-moz-transform .6s ease-in-out;-o-transition:-o-transform .6s ease-in-out;transition:transform .6s ease-in-out;-webkit-backface-visibility:hidden;-moz-backface-visibility:hidden;backface-visibility:hidden;-webkit-perspective:1000;-moz-perspective:1000;perspective:1000}.carousel-inner>.item.active.right,.carousel-inner>.item.next{-webkit-transform:translate3d(100%,0,0);transform:translate3d(100%,0,0);left:0}.carousel-inner>.item.active.left,.carousel-inner>.item.prev{-webkit-transform:translate3d(-100%,0,0);transform:translate3d(-100%,0,0);left:0}.carousel-inner>.item.active,.carousel-inner>.item.next.left,.carousel-inner>.item.prev.right{-webkit-transform:translate3d(0,0,0);transform:translate3d(0,0,0);left:0}}.carousel-inner>.active,.carousel-inner>.next,.carousel-inner>.prev{display:block}.carousel-inner>.active{left:0}.carousel-inner>.next,.carousel-inner>.prev{position:absolute;top:0;width:100%}.carousel-inner>.next{left:100%}.carousel-inner>.prev{left:-100%}.carousel-inner>.next.left,.carousel-inner>.prev.right{left:0}.carousel-inner>.active.left{left:-100%}.carousel-inner>.active.right{left:100%}.carousel-control{position:absolute;top:0;left:0;bottom:0;width:15%;opacity:.5;filter:alpha(opacity=50);font-size:20px;color:#fff;text-align:center;text-shadow:0 1px 2px rgba(0,0,0,.6)}.carousel-control.left{background-image:-webkit-linear-gradient(left,rgba(0,0,0,.5) 0,rgba(0,0,0,.0001) 100%);background-image:-o-linear-gradient(left,rgba(0,0,0,.5) 0,rgba(0,0,0,.0001) 100%);background-image:linear-gradient(to right,rgba(0,0,0,.5) 0,rgba(0,0,0,.0001) 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1)}.carousel-control.right{left:auto;right:0;background-image:-webkit-linear-gradient(left,rgba(0,0,0,.0001) 0,rgba(0,0,0,.5) 100%);background-image:-o-linear-gradient(left,rgba(0,0,0,.0001) 0,rgba(0,0,0,.5) 100%);background-image:linear-gradient(to right,rgba(0,0,0,.0001) 0,rgba(0,0,0,.5) 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1)}.carousel-control:focus,.carousel-control:hover{outline:0;color:#fff;text-decoration:none;opacity:.9;filter:alpha(opacity=90)}.carousel-control .glyphicon-chevron-left,.carousel-control .glyphicon-chevron-right,.carousel-control .icon-next,.carousel-control .icon-prev{position:absolute;top:50%;z-index:5;display:inline-block}.carousel-control .glyphicon-chevron-left,.carousel-control .icon-prev{left:50%;margin-left:-10px}.carousel-control .glyphicon-chevron-right,.carousel-control .icon-next{right:50%;margin-right:-10px}.carousel-control .icon-next,.carousel-control .icon-prev{width:20px;height:20px;margin-top:-10px;line-height:1;font-family:serif}.carousel-control .icon-prev:before{content:'\2039'}.carousel-control .icon-next:before{content:'\203a'}.carousel-indicators{position:absolute;bottom:10px;left:50%;z-index:15;width:60%;margin-left:-30%;padding-left:0;list-style:none;text-align:center}.carousel-indicators li{display:inline-block;width:10px;height:10px;margin:1px;text-indent:-999px;border:1px solid #fff;border-radius:10px;cursor:pointer;background-color:transparent}.carousel-indicators .active{margin:0;width:12px;height:12px;background-color:#fff}.carousel-caption{position:absolute;left:15%;right:15%;bottom:20px;z-index:10;padding-top:20px;padding-bottom:20px;color:#fff;text-align:center;text-shadow:0 1px 2px rgba(0,0,0,.6)}.carousel-caption .btn{text-shadow:none}@media screen and (min-width:768px){.carousel-control .glyphicon-chevron-left,.carousel-control .glyphicon-chevron-right,.carousel-control .icon-next,.carousel-control .icon-prev{width:30px;height:30px;margin-top:-15px;font-size:30px}.carousel-control .glyphicon-chevron-left,.carousel-control .icon-prev{margin-left:-15px}.carousel-control .glyphicon-chevron-right,.carousel-control .icon-next{margin-right:-15px}.carousel-caption{left:20%;right:20%;padding-bottom:30px}.carousel-indicators{bottom:20px}}.btn-group-vertical>.btn-group:after,.btn-group-vertical>.btn-group:before,.btn-toolbar:after,.btn-toolbar:before,.clearfix:after,.clearfix:before,.container-fluid:after,.container-fluid:before,.container:after,.container:before,.dl-horizontal dd:after,.dl-horizontal dd:before,.form-horizontal .form-group:after,.form-horizontal .form-group:before,.item_buttons:after,.item_buttons:before,.modal-footer:after,.modal-footer:before,.nav:after,.nav:before,.navbar-collapse:after,.navbar-collapse:before,.navbar-header:after,.navbar-header:before,.navbar:after,.navbar:before,.pager:after,.pager:before,.panel-body:after,.panel-body:before,.row:after,.row:before{content:" ";display:table}.btn-group-vertical>.btn-group:after,.btn-toolbar:after,.clearfix:after,.container-fluid:after,.container:after,.dl-horizontal dd:after,.form-horizontal .form-group:after,.item_buttons:after,.modal-footer:after,.nav:after,.navbar-collapse:after,.navbar-header:after,.navbar:after,.pager:after,.panel-body:after,.row:after{clear:both}.center-block{display:block;margin-left:auto;margin-right:auto}.pull-right{float:right!important}.pull-left{float:left!important}.hide{display:none!important}.show{display:block!important}.invisible{visibility:hidden}.text-hide{font:0/0 a;color:transparent;text-shadow:none;background-color:transparent;border:0}.hidden{display:none!important}.affix{position:fixed}@-ms-viewport{width:device-width}.visible-lg,.visible-lg-block,.visible-lg-inline,.visible-lg-inline-block,.visible-md,.visible-md-block,.visible-md-inline,.visible-md-inline-block,.visible-sm,.visible-sm-block,.visible-sm-inline,.visible-sm-inline-block,.visible-xs,.visible-xs-block,.visible-xs-inline,.visible-xs-inline-block{display:none!important}@media (max-width:767px){.visible-xs{display:block!important}table.visible-xs{display:table}tr.visible-xs{display:table-row!important}td.visible-xs,th.visible-xs{display:table-cell!important}.visible-xs-block{display:block!important}.visible-xs-inline{display:inline!important}.visible-xs-inline-block{display:inline-block!important}}@media (min-width:768px)and (max-width:991px){.visible-sm{display:block!important}table.visible-sm{display:table}tr.visible-sm{display:table-row!important}td.visible-sm,th.visible-sm{display:table-cell!important}.visible-sm-block{display:block!important}.visible-sm-inline{display:inline!important}.visible-sm-inline-block{display:inline-block!important}}@media (min-width:992px)and (max-width:1199px){.visible-md{display:block!important}table.visible-md{display:table}tr.visible-md{display:table-row!important}td.visible-md,th.visible-md{display:table-cell!important}.visible-md-block{display:block!important}.visible-md-inline{display:inline!important}.visible-md-inline-block{display:inline-block!important}}@media (min-width:1200px){.visible-lg{display:block!important}table.visible-lg{display:table}tr.visible-lg{display:table-row!important}td.visible-lg,th.visible-lg{display:table-cell!important}.visible-lg-block{display:block!important}.visible-lg-inline{display:inline!important}.visible-lg-inline-block{display:inline-block!important}}@media (max-width:767px){.hidden-xs{display:none!important}}@media (min-width:768px)and (max-width:991px){.hidden-sm{display:none!important}}@media (min-width:992px)and (max-width:1199px){.hidden-md{display:none!important}}@media (min-width:1200px){.hidden-lg{display:none!important}}.visible-print{display:none!important}@media print{.visible-print{display:block!important}table.visible-print{display:table}tr.visible-print{display:table-row!important}td.visible-print,th.visible-print{display:table-cell!important}}.visible-print-block{display:none!important}@media print{.visible-print-block{display:block!important}}.visible-print-inline{display:none!important}@media print{.visible-print-inline{display:inline!important}}.visible-print-inline-block{display:none!important}@media print{.visible-print-inline-block{display:inline-block!important}.hidden-print{display:none!important}}/*!
*
* Font Awesome
*
*//*!
 *  Font Awesome 4.2.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */@font-face{font-family:'FontAwesome';src:url(../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.2.0);src:url(../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.2.0)format('embedded-opentype'),url(../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.2.0)format('woff'),url(../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.2.0)format('truetype'),url(../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.2.0#fontawesomeregular)format('svg');font-weight:400;font-style:normal}.fa{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.fa-lg{font-size:1.33333333em;line-height:.75em;vertical-align:-15%}.fa-2x{font-size:2em}.fa-3x{font-size:3em}.fa-4x{font-size:4em}.fa-5x{font-size:5em}.fa-fw{width:1.28571429em;text-align:center}.fa-ul{padding-left:0;margin-left:2.14285714em;list-style-type:none}.fa-ul>li{position:relative}.fa-li{position:absolute;left:-2.14285714em;width:2.14285714em;top:.14285714em;text-align:center}.fa-li.fa-lg{left:-1.85714286em}.fa-border{padding:.2em .25em .15em;border:.08em solid #eee;border-radius:.1em}.fa.pull-left{margin-right:.3em}.fa.pull-right{margin-left:.3em}.fa-spin{-webkit-animation:fa-spin 2s infinite linear;animation:fa-spin 2s infinite linear}@-webkit-keyframes fa-spin{0%{-webkit-transform:rotate(0);transform:rotate(0)}100%{-webkit-transform:rotate(359deg);transform:rotate(359deg)}}@keyframes fa-spin{0%{-webkit-transform:rotate(0);transform:rotate(0)}100%{-webkit-transform:rotate(359deg);transform:rotate(359deg)}}.fa-rotate-90{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=1);-webkit-transform:rotate(90deg);-ms-transform:rotate(90deg);transform:rotate(90deg)}.fa-rotate-180{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=2);-webkit-transform:rotate(180deg);-ms-transform:rotate(180deg);transform:rotate(180deg)}.fa-rotate-270{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=3);-webkit-transform:rotate(270deg);-ms-transform:rotate(270deg);transform:rotate(270deg)}.fa-flip-horizontal{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);-webkit-transform:scale(-1,1);-ms-transform:scale(-1,1);transform:scale(-1,1)}.fa-flip-vertical{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);-webkit-transform:scale(1,-1);-ms-transform:scale(1,-1);transform:scale(1,-1)}:root .fa-flip-horizontal,:root .fa-flip-vertical,:root .fa-rotate-180,:root .fa-rotate-270,:root .fa-rotate-90{filter:none}.fa-stack{position:relative;display:inline-block;width:2em;height:2em;line-height:2em;vertical-align:middle}.fa-stack-1x,.fa-stack-2x{position:absolute;left:0;width:100%;text-align:center}.fa-stack-1x{line-height:inherit}.fa-stack-2x{font-size:2em}.fa-inverse{color:#fff}.fa-glass:before{content:"\f000"}.fa-music:before{content:"\f001"}.fa-search:before{content:"\f002"}.fa-envelope-o:before{content:"\f003"}.fa-heart:before{content:"\f004"}.fa-star:before{content:"\f005"}.fa-star-o:before{content:"\f006"}.fa-user:before{content:"\f007"}.fa-film:before{content:"\f008"}.fa-th-large:before{content:"\f009"}.fa-th:before{content:"\f00a"}.fa-th-list:before{content:"\f00b"}.fa-check:before{content:"\f00c"}.fa-close:before,.fa-remove:before,.fa-times:before{content:"\f00d"}.fa-search-plus:before{content:"\f00e"}.fa-search-minus:before{content:"\f010"}.fa-power-off:before{content:"\f011"}.fa-signal:before{content:"\f012"}.fa-cog:before,.fa-gear:before{content:"\f013"}.fa-trash-o:before{content:"\f014"}.fa-home:before{content:"\f015"}.fa-file-o:before{content:"\f016"}.fa-clock-o:before{content:"\f017"}.fa-road:before{content:"\f018"}.fa-download:before{content:"\f019"}.fa-arrow-circle-o-down:before{content:"\f01a"}.fa-arrow-circle-o-up:before{content:"\f01b"}.fa-inbox:before{content:"\f01c"}.fa-play-circle-o:before{content:"\f01d"}.fa-repeat:before,.fa-rotate-right:before{content:"\f01e"}.fa-refresh:before{content:"\f021"}.fa-list-alt:before{content:"\f022"}.fa-lock:before{content:"\f023"}.fa-flag:before{content:"\f024"}.fa-headphones:before{content:"\f025"}.fa-volume-off:before{content:"\f026"}.fa-volume-down:before{content:"\f027"}.fa-volume-up:before{content:"\f028"}.fa-qrcode:before{content:"\f029"}.fa-barcode:before{content:"\f02a"}.fa-tag:before{content:"\f02b"}.fa-tags:before{content:"\f02c"}.fa-book:before{content:"\f02d"}.fa-bookmark:before{content:"\f02e"}.fa-print:before{content:"\f02f"}.fa-camera:before{content:"\f030"}.fa-font:before{content:"\f031"}.fa-bold:before{content:"\f032"}.fa-italic:before{content:"\f033"}.fa-text-height:before{content:"\f034"}.fa-text-width:before{content:"\f035"}.fa-align-left:before{content:"\f036"}.fa-align-center:before{content:"\f037"}.fa-align-right:before{content:"\f038"}.fa-align-justify:before{content:"\f039"}.fa-list:before{content:"\f03a"}.fa-dedent:before,.fa-outdent:before{content:"\f03b"}.fa-indent:before{content:"\f03c"}.fa-video-camera:before{content:"\f03d"}.fa-image:before,.fa-photo:before,.fa-picture-o:before{content:"\f03e"}.fa-pencil:before{content:"\f040"}.fa-map-marker:before{content:"\f041"}.fa-adjust:before{content:"\f042"}.fa-tint:before{content:"\f043"}.fa-edit:before,.fa-pencil-square-o:before{content:"\f044"}.fa-share-square-o:before{content:"\f045"}.fa-check-square-o:before{content:"\f046"}.fa-arrows:before{content:"\f047"}.fa-step-backward:before{content:"\f048"}.fa-fast-backward:before{content:"\f049"}.fa-backward:before{content:"\f04a"}.fa-play:before{content:"\f04b"}.fa-pause:before{content:"\f04c"}.fa-stop:before{content:"\f04d"}.fa-forward:before{content:"\f04e"}.fa-fast-forward:before{content:"\f050"}.fa-step-forward:before{content:"\f051"}.fa-eject:before{content:"\f052"}.fa-chevron-left:before{content:"\f053"}.fa-chevron-right:before{content:"\f054"}.fa-plus-circle:before{content:"\f055"}.fa-minus-circle:before{content:"\f056"}.fa-times-circle:before{content:"\f057"}.fa-check-circle:before{content:"\f058"}.fa-question-circle:before{content:"\f059"}.fa-info-circle:before{content:"\f05a"}.fa-crosshairs:before{content:"\f05b"}.fa-times-circle-o:before{content:"\f05c"}.fa-check-circle-o:before{content:"\f05d"}.fa-ban:before{content:"\f05e"}.fa-arrow-left:before{content:"\f060"}.fa-arrow-right:before{content:"\f061"}.fa-arrow-up:before{content:"\f062"}.fa-arrow-down:before{content:"\f063"}.fa-mail-forward:before,.fa-share:before{content:"\f064"}.fa-expand:before{content:"\f065"}.fa-compress:before{content:"\f066"}.fa-plus:before{content:"\f067"}.fa-minus:before{content:"\f068"}.fa-asterisk:before{content:"\f069"}.fa-exclamation-circle:before{content:"\f06a"}.fa-gift:before{content:"\f06b"}.fa-leaf:before{content:"\f06c"}.fa-fire:before{content:"\f06d"}.fa-eye:before{content:"\f06e"}.fa-eye-slash:before{content:"\f070"}.fa-exclamation-triangle:before,.fa-warning:before{content:"\f071"}.fa-plane:before{content:"\f072"}.fa-calendar:before{content:"\f073"}.fa-random:before{content:"\f074"}.fa-comment:before{content:"\f075"}.fa-magnet:before{content:"\f076"}.fa-chevron-up:before{content:"\f077"}.fa-chevron-down:before{content:"\f078"}.fa-retweet:before{content:"\f079"}.fa-shopping-cart:before{content:"\f07a"}.fa-folder:before{content:"\f07b"}.fa-folder-open:before{content:"\f07c"}.fa-arrows-v:before{content:"\f07d"}.fa-arrows-h:before{content:"\f07e"}.fa-bar-chart-o:before,.fa-bar-chart:before{content:"\f080"}.fa-twitter-square:before{content:"\f081"}.fa-facebook-square:before{content:"\f082"}.fa-camera-retro:before{content:"\f083"}.fa-key:before{content:"\f084"}.fa-cogs:before,.fa-gears:before{content:"\f085"}.fa-comments:before{content:"\f086"}.fa-thumbs-o-up:before{content:"\f087"}.fa-thumbs-o-down:before{content:"\f088"}.fa-star-half:before{content:"\f089"}.fa-heart-o:before{content:"\f08a"}.fa-sign-out:before{content:"\f08b"}.fa-linkedin-square:before{content:"\f08c"}.fa-thumb-tack:before{content:"\f08d"}.fa-external-link:before{content:"\f08e"}.fa-sign-in:before{content:"\f090"}.fa-trophy:before{content:"\f091"}.fa-github-square:before{content:"\f092"}.fa-upload:before{content:"\f093"}.fa-lemon-o:before{content:"\f094"}.fa-phone:before{content:"\f095"}.fa-square-o:before{content:"\f096"}.fa-bookmark-o:before{content:"\f097"}.fa-phone-square:before{content:"\f098"}.fa-twitter:before{content:"\f099"}.fa-facebook:before{content:"\f09a"}.fa-github:before{content:"\f09b"}.fa-unlock:before{content:"\f09c"}.fa-credit-card:before{content:"\f09d"}.fa-rss:before{content:"\f09e"}.fa-hdd-o:before{content:"\f0a0"}.fa-bullhorn:before{content:"\f0a1"}.fa-bell:before{content:"\f0f3"}.fa-certificate:before{content:"\f0a3"}.fa-hand-o-right:before{content:"\f0a4"}.fa-hand-o-left:before{content:"\f0a5"}.fa-hand-o-up:before{content:"\f0a6"}.fa-hand-o-down:before{content:"\f0a7"}.fa-arrow-circle-left:before{content:"\f0a8"}.fa-arrow-circle-right:before{content:"\f0a9"}.fa-arrow-circle-up:before{content:"\f0aa"}.fa-arrow-circle-down:before{content:"\f0ab"}.fa-globe:before{content:"\f0ac"}.fa-wrench:before{content:"\f0ad"}.fa-tasks:before{content:"\f0ae"}.fa-filter:before{content:"\f0b0"}.fa-briefcase:before{content:"\f0b1"}.fa-arrows-alt:before{content:"\f0b2"}.fa-group:before,.fa-users:before{content:"\f0c0"}.fa-chain:before,.fa-link:before{content:"\f0c1"}.fa-cloud:before{content:"\f0c2"}.fa-flask:before{content:"\f0c3"}.fa-cut:before,.fa-scissors:before{content:"\f0c4"}.fa-copy:before,.fa-files-o:before{content:"\f0c5"}.fa-paperclip:before{content:"\f0c6"}.fa-floppy-o:before,.fa-save:before{content:"\f0c7"}.fa-square:before{content:"\f0c8"}.fa-bars:before,.fa-navicon:before,.fa-reorder:before{content:"\f0c9"}.fa-list-ul:before{content:"\f0ca"}.fa-list-ol:before{content:"\f0cb"}.fa-strikethrough:before{content:"\f0cc"}.fa-underline:before{content:"\f0cd"}.fa-table:before{content:"\f0ce"}.fa-magic:before{content:"\f0d0"}.fa-truck:before{content:"\f0d1"}.fa-pinterest:before{content:"\f0d2"}.fa-pinterest-square:before{content:"\f0d3"}.fa-google-plus-square:before{content:"\f0d4"}.fa-google-plus:before{content:"\f0d5"}.fa-money:before{content:"\f0d6"}.fa-caret-down:before{content:"\f0d7"}.fa-caret-up:before{content:"\f0d8"}.fa-caret-left:before{content:"\f0d9"}.fa-caret-right:before{content:"\f0da"}.fa-columns:before{content:"\f0db"}.fa-sort:before,.fa-unsorted:before{content:"\f0dc"}.fa-sort-desc:before,.fa-sort-down:before{content:"\f0dd"}.fa-sort-asc:before,.fa-sort-up:before{content:"\f0de"}.fa-envelope:before{content:"\f0e0"}.fa-linkedin:before{content:"\f0e1"}.fa-rotate-left:before,.fa-undo:before{content:"\f0e2"}.fa-gavel:before,.fa-legal:before{content:"\f0e3"}.fa-dashboard:before,.fa-tachometer:before{content:"\f0e4"}.fa-comment-o:before{content:"\f0e5"}.fa-comments-o:before{content:"\f0e6"}.fa-bolt:before,.fa-flash:before{content:"\f0e7"}.fa-sitemap:before{content:"\f0e8"}.fa-umbrella:before{content:"\f0e9"}.fa-clipboard:before,.fa-paste:before{content:"\f0ea"}.fa-lightbulb-o:before{content:"\f0eb"}.fa-exchange:before{content:"\f0ec"}.fa-cloud-download:before{content:"\f0ed"}.fa-cloud-upload:before{content:"\f0ee"}.fa-user-md:before{content:"\f0f0"}.fa-stethoscope:before{content:"\f0f1"}.fa-suitcase:before{content:"\f0f2"}.fa-bell-o:before{content:"\f0a2"}.fa-coffee:before{content:"\f0f4"}.fa-cutlery:before{content:"\f0f5"}.fa-file-text-o:before{content:"\f0f6"}.fa-building-o:before{content:"\f0f7"}.fa-hospital-o:before{content:"\f0f8"}.fa-ambulance:before{content:"\f0f9"}.fa-medkit:before{content:"\f0fa"}.fa-fighter-jet:before{content:"\f0fb"}.fa-beer:before{content:"\f0fc"}.fa-h-square:before{content:"\f0fd"}.fa-plus-square:before{content:"\f0fe"}.fa-angle-double-left:before{content:"\f100"}.fa-angle-double-right:before{content:"\f101"}.fa-angle-double-up:before{content:"\f102"}.fa-angle-double-down:before{content:"\f103"}.fa-angle-left:before{content:"\f104"}.fa-angle-right:before{content:"\f105"}.fa-angle-up:before{content:"\f106"}.fa-angle-down:before{content:"\f107"}.fa-desktop:before{content:"\f108"}.fa-laptop:before{content:"\f109"}.fa-tablet:before{content:"\f10a"}.fa-mobile-phone:before,.fa-mobile:before{content:"\f10b"}.fa-circle-o:before{content:"\f10c"}.fa-quote-left:before{content:"\f10d"}.fa-quote-right:before{content:"\f10e"}.fa-spinner:before{content:"\f110"}.fa-circle:before{content:"\f111"}.fa-mail-reply:before,.fa-reply:before{content:"\f112"}.fa-github-alt:before{content:"\f113"}.fa-folder-o:before{content:"\f114"}.fa-folder-open-o:before{content:"\f115"}.fa-smile-o:before{content:"\f118"}.fa-frown-o:before{content:"\f119"}.fa-meh-o:before{content:"\f11a"}.fa-gamepad:before{content:"\f11b"}.fa-keyboard-o:before{content:"\f11c"}.fa-flag-o:before{content:"\f11d"}.fa-flag-checkered:before{content:"\f11e"}.fa-terminal:before{content:"\f120"}.fa-code:before{content:"\f121"}.fa-mail-reply-all:before,.fa-reply-all:before{content:"\f122"}.fa-star-half-empty:before,.fa-star-half-full:before,.fa-star-half-o:before{content:"\f123"}.fa-location-arrow:before{content:"\f124"}.fa-crop:before{content:"\f125"}.fa-code-fork:before{content:"\f126"}.fa-chain-broken:before,.fa-unlink:before{content:"\f127"}.fa-question:before{content:"\f128"}.fa-info:before{content:"\f129"}.fa-exclamation:before{content:"\f12a"}.fa-superscript:before{content:"\f12b"}.fa-subscript:before{content:"\f12c"}.fa-eraser:before{content:"\f12d"}.fa-puzzle-piece:before{content:"\f12e"}.fa-microphone:before{content:"\f130"}.fa-microphone-slash:before{content:"\f131"}.fa-shield:before{content:"\f132"}.fa-calendar-o:before{content:"\f133"}.fa-fire-extinguisher:before{content:"\f134"}.fa-rocket:before{content:"\f135"}.fa-maxcdn:before{content:"\f136"}.fa-chevron-circle-left:before{content:"\f137"}.fa-chevron-circle-right:before{content:"\f138"}.fa-chevron-circle-up:before{content:"\f139"}.fa-chevron-circle-down:before{content:"\f13a"}.fa-html5:before{content:"\f13b"}.fa-css3:before{content:"\f13c"}.fa-anchor:before{content:"\f13d"}.fa-unlock-alt:before{content:"\f13e"}.fa-bullseye:before{content:"\f140"}.fa-ellipsis-h:before{content:"\f141"}.fa-ellipsis-v:before{content:"\f142"}.fa-rss-square:before{content:"\f143"}.fa-play-circle:before{content:"\f144"}.fa-ticket:before{content:"\f145"}.fa-minus-square:before{content:"\f146"}.fa-minus-square-o:before{content:"\f147"}.fa-level-up:before{content:"\f148"}.fa-level-down:before{content:"\f149"}.fa-check-square:before{content:"\f14a"}.fa-pencil-square:before{content:"\f14b"}.fa-external-link-square:before{content:"\f14c"}.fa-share-square:before{content:"\f14d"}.fa-compass:before{content:"\f14e"}.fa-caret-square-o-down:before,.fa-toggle-down:before{content:"\f150"}.fa-caret-square-o-up:before,.fa-toggle-up:before{content:"\f151"}.fa-caret-square-o-right:before,.fa-toggle-right:before{content:"\f152"}.fa-eur:before,.fa-euro:before{content:"\f153"}.fa-gbp:before{content:"\f154"}.fa-dollar:before,.fa-usd:before{content:"\f155"}.fa-inr:before,.fa-rupee:before{content:"\f156"}.fa-cny:before,.fa-jpy:before,.fa-rmb:before,.fa-yen:before{content:"\f157"}.fa-rouble:before,.fa-rub:before,.fa-ruble:before{content:"\f158"}.fa-krw:before,.fa-won:before{content:"\f159"}.fa-bitcoin:before,.fa-btc:before{content:"\f15a"}.fa-file:before{content:"\f15b"}.fa-file-text:before{content:"\f15c"}.fa-sort-alpha-asc:before{content:"\f15d"}.fa-sort-alpha-desc:before{content:"\f15e"}.fa-sort-amount-asc:before{content:"\f160"}.fa-sort-amount-desc:before{content:"\f161"}.fa-sort-numeric-asc:before{content:"\f162"}.fa-sort-numeric-desc:before{content:"\f163"}.fa-thumbs-up:before{content:"\f164"}.fa-thumbs-down:before{content:"\f165"}.fa-youtube-square:before{content:"\f166"}.fa-youtube:before{content:"\f167"}.fa-xing:before{content:"\f168"}.fa-xing-square:before{content:"\f169"}.fa-youtube-play:before{content:"\f16a"}.fa-dropbox:before{content:"\f16b"}.fa-stack-overflow:before{content:"\f16c"}.fa-instagram:before{content:"\f16d"}.fa-flickr:before{content:"\f16e"}.fa-adn:before{content:"\f170"}.fa-bitbucket:before{content:"\f171"}.fa-bitbucket-square:before{content:"\f172"}.fa-tumblr:before{content:"\f173"}.fa-tumblr-square:before{content:"\f174"}.fa-long-arrow-down:before{content:"\f175"}.fa-long-arrow-up:before{content:"\f176"}.fa-long-arrow-left:before{content:"\f177"}.fa-long-arrow-right:before{content:"\f178"}.fa-apple:before{content:"\f179"}.fa-windows:before{content:"\f17a"}.fa-android:before{content:"\f17b"}.fa-linux:before{content:"\f17c"}.fa-dribbble:before{content:"\f17d"}.fa-skype:before{content:"\f17e"}.fa-foursquare:before{content:"\f180"}.fa-trello:before{content:"\f181"}.fa-female:before{content:"\f182"}.fa-male:before{content:"\f183"}.fa-gittip:before{content:"\f184"}.fa-sun-o:before{content:"\f185"}.fa-moon-o:before{content:"\f186"}.fa-archive:before{content:"\f187"}.fa-bug:before{content:"\f188"}.fa-vk:before{content:"\f189"}.fa-weibo:before{content:"\f18a"}.fa-renren:before{content:"\f18b"}.fa-pagelines:before{content:"\f18c"}.fa-stack-exchange:before{content:"\f18d"}.fa-arrow-circle-o-right:before{content:"\f18e"}.fa-arrow-circle-o-left:before{content:"\f190"}.fa-caret-square-o-left:before,.fa-toggle-left:before{content:"\f191"}.fa-dot-circle-o:before{content:"\f192"}.fa-wheelchair:before{content:"\f193"}.fa-vimeo-square:before{content:"\f194"}.fa-try:before,.fa-turkish-lira:before{content:"\f195"}.fa-plus-square-o:before{content:"\f196"}.fa-space-shuttle:before{content:"\f197"}.fa-slack:before{content:"\f198"}.fa-envelope-square:before{content:"\f199"}.fa-wordpress:before{content:"\f19a"}.fa-openid:before{content:"\f19b"}.fa-bank:before,.fa-institution:before,.fa-university:before{content:"\f19c"}.fa-graduation-cap:before,.fa-mortar-board:before{content:"\f19d"}.fa-yahoo:before{content:"\f19e"}.fa-google:before{content:"\f1a0"}.fa-reddit:before{content:"\f1a1"}.fa-reddit-square:before{content:"\f1a2"}.fa-stumbleupon-circle:before{content:"\f1a3"}.fa-stumbleupon:before{content:"\f1a4"}.fa-delicious:before{content:"\f1a5"}.fa-digg:before{content:"\f1a6"}.fa-pied-piper:before{content:"\f1a7"}.fa-pied-piper-alt:before{content:"\f1a8"}.fa-drupal:before{content:"\f1a9"}.fa-joomla:before{content:"\f1aa"}.fa-language:before{content:"\f1ab"}.fa-fax:before{content:"\f1ac"}.fa-building:before{content:"\f1ad"}.fa-child:before{content:"\f1ae"}.fa-paw:before{content:"\f1b0"}.fa-spoon:before{content:"\f1b1"}.fa-cube:before{content:"\f1b2"}.fa-cubes:before{content:"\f1b3"}.fa-behance:before{content:"\f1b4"}.fa-behance-square:before{content:"\f1b5"}.fa-steam:before{content:"\f1b6"}.fa-steam-square:before{content:"\f1b7"}.fa-recycle:before{content:"\f1b8"}.fa-automobile:before,.fa-car:before{content:"\f1b9"}.fa-cab:before,.fa-taxi:before{content:"\f1ba"}.fa-tree:before{content:"\f1bb"}.fa-spotify:before{content:"\f1bc"}.fa-deviantart:before{content:"\f1bd"}.fa-soundcloud:before{content:"\f1be"}.fa-database:before{content:"\f1c0"}.fa-file-pdf-o:before{content:"\f1c1"}.fa-file-word-o:before{content:"\f1c2"}.fa-file-excel-o:before{content:"\f1c3"}.fa-file-powerpoint-o:before{content:"\f1c4"}.fa-file-image-o:before,.fa-file-photo-o:before,.fa-file-picture-o:before{content:"\f1c5"}.fa-file-archive-o:before,.fa-file-zip-o:before{content:"\f1c6"}.fa-file-audio-o:before,.fa-file-sound-o:before{content:"\f1c7"}.fa-file-movie-o:before,.fa-file-video-o:before{content:"\f1c8"}.fa-file-code-o:before{content:"\f1c9"}.fa-vine:before{content:"\f1ca"}.fa-codepen:before{content:"\f1cb"}.fa-jsfiddle:before{content:"\f1cc"}.fa-life-bouy:before,.fa-life-buoy:before,.fa-life-ring:before,.fa-life-saver:before,.fa-support:before{content:"\f1cd"}.fa-circle-o-notch:before{content:"\f1ce"}.fa-ra:before,.fa-rebel:before{content:"\f1d0"}.fa-empire:before,.fa-ge:before{content:"\f1d1"}.fa-git-square:before{content:"\f1d2"}.fa-git:before{content:"\f1d3"}.fa-hacker-news:before{content:"\f1d4"}.fa-tencent-weibo:before{content:"\f1d5"}.fa-qq:before{content:"\f1d6"}.fa-wechat:before,.fa-weixin:before{content:"\f1d7"}.fa-paper-plane:before,.fa-send:before{content:"\f1d8"}.fa-paper-plane-o:before,.fa-send-o:before{content:"\f1d9"}.fa-history:before{content:"\f1da"}.fa-circle-thin:before{content:"\f1db"}.fa-header:before{content:"\f1dc"}.fa-paragraph:before{content:"\f1dd"}.fa-sliders:before{content:"\f1de"}.fa-share-alt:before{content:"\f1e0"}.fa-share-alt-square:before{content:"\f1e1"}.fa-bomb:before{content:"\f1e2"}.fa-futbol-o:before,.fa-soccer-ball-o:before{content:"\f1e3"}.fa-tty:before{content:"\f1e4"}.fa-binoculars:before{content:"\f1e5"}.fa-plug:before{content:"\f1e6"}.fa-slideshare:before{content:"\f1e7"}.fa-twitch:before{content:"\f1e8"}.fa-yelp:before{content:"\f1e9"}.fa-newspaper-o:before{content:"\f1ea"}.fa-wifi:before{content:"\f1eb"}.fa-calculator:before{content:"\f1ec"}.fa-paypal:before{content:"\f1ed"}.fa-google-wallet:before{content:"\f1ee"}.fa-cc-visa:before{content:"\f1f0"}.fa-cc-mastercard:before{content:"\f1f1"}.fa-cc-discover:before{content:"\f1f2"}.fa-cc-amex:before{content:"\f1f3"}.fa-cc-paypal:before{content:"\f1f4"}.fa-cc-stripe:before{content:"\f1f5"}.fa-bell-slash:before{content:"\f1f6"}.fa-bell-slash-o:before{content:"\f1f7"}.fa-trash:before{content:"\f1f8"}.fa-copyright:before{content:"\f1f9"}.fa-at:before{content:"\f1fa"}.fa-eyedropper:before{content:"\f1fb"}.fa-paint-brush:before{content:"\f1fc"}.fa-birthday-cake:before{content:"\f1fd"}.fa-area-chart:before{content:"\f1fe"}.fa-pie-chart:before{content:"\f200"}.fa-line-chart:before{content:"\f201"}.fa-lastfm:before{content:"\f202"}.fa-lastfm-square:before{content:"\f203"}.fa-toggle-off:before{content:"\f204"}.fa-toggle-on:before{content:"\f205"}.fa-bicycle:before{content:"\f206"}.fa-bus:before{content:"\f207"}.fa-ioxhost:before{content:"\f208"}.fa-angellist:before{content:"\f209"}.fa-cc:before{content:"\f20a"}.fa-ils:before,.fa-shekel:before,.fa-sheqel:before{content:"\f20b"}.fa-meanpath:before{content:"\f20c"}/*!
*
* IPython base
*
*/.modal.fade .modal-dialog{-webkit-transform:translate(0,0);-ms-transform:translate(0,0);-o-transform:translate(0,0);transform:translate(0,0)}code{color:#000}pre{font-size:inherit;line-height:inherit}label{font-weight:400}.border-box-sizing{box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}.corner-all{border-radius:2px}.no-padding{padding:0}.hbox{display:-webkit-box;-webkit-box-orient:horizontal;display:-moz-box;-moz-box-orient:horizontal;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}.hbox>*{-webkit-box-flex:0;-moz-box-flex:0;box-flex:0;flex:none}.vbox{display:-webkit-box;-webkit-box-orient:vertical;display:-moz-box;-moz-box-orient:vertical;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}.vbox>*{-webkit-box-flex:0;-moz-box-flex:0;box-flex:0;flex:none}.hbox.reverse,.reverse,.vbox.reverse{-webkit-box-direction:reverse;-moz-box-direction:reverse;box-direction:reverse;flex-direction:row-reverse}.box-flex0,.hbox.box-flex0,.vbox.box-flex0{-webkit-box-flex:0;-moz-box-flex:0;box-flex:0;flex:none;width:auto}.box-flex1,.hbox.box-flex1,.vbox.box-flex1{-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}.box-flex,.hbox.box-flex,.vbox.box-flex{-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}.box-flex2,.hbox.box-flex2,.vbox.box-flex2{-webkit-box-flex:2;-moz-box-flex:2;box-flex:2;flex:2}.box-group1{-webkit-box-flex-group:1;-moz-box-flex-group:1;box-flex-group:1}.box-group2{-webkit-box-flex-group:2;-moz-box-flex-group:2;box-flex-group:2}.hbox.start,.start,.vbox.start{-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start}.end,.hbox.end,.vbox.end{-webkit-box-pack:end;-moz-box-pack:end;box-pack:end;justify-content:flex-end}.center,.hbox.center,.vbox.center{-webkit-box-pack:center;-moz-box-pack:center;box-pack:center;justify-content:center}.baseline,.hbox.baseline,.vbox.baseline{-webkit-box-pack:baseline;-moz-box-pack:baseline;box-pack:baseline;justify-content:baseline}.hbox.stretch,.stretch,.vbox.stretch{-webkit-box-pack:stretch;-moz-box-pack:stretch;box-pack:stretch;justify-content:stretch}.align-start,.hbox.align-start,.vbox.align-start{-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start}.align-end,.hbox.align-end,.vbox.align-end{-webkit-box-align:end;-moz-box-align:end;box-align:end;align-items:flex-end}.align-center,.hbox.align-center,.vbox.align-center{-webkit-box-align:center;-moz-box-align:center;box-align:center;align-items:center}.align-baseline,.hbox.align-baseline,.vbox.align-baseline{-webkit-box-align:baseline;-moz-box-align:baseline;box-align:baseline;align-items:baseline}.align-stretch,.hbox.align-stretch,.vbox.align-stretch{-webkit-box-align:stretch;-moz-box-align:stretch;box-align:stretch;align-items:stretch}div.error{margin:2em;text-align:center}div.error>h1{font-size:500%;line-height:normal}div.error>p{font-size:200%;line-height:normal}div.traceback-wrapper{text-align:left;max-width:800px;margin:auto}body{position:absolute;left:0;right:0;top:0;bottom:0;overflow:visible}#header{display:none;background-color:#fff;position:relative;z-index:100}#header #header-container{padding-bottom:5px;padding-top:5px;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}#header .header-bar{width:100%;height:1px;background:#e7e7e7;margin-bottom:-1px}#header-spacer{width:100%;visibility:hidden}@media print{#header{display:none!important}#header-spacer{display:none}}#ipython_notebook{padding-left:0;padding-top:1px;padding-bottom:1px}@media (max-width:991px){#ipython_notebook{margin-left:10px}}#noscript{width:auto;padding-top:16px;padding-bottom:16px;text-align:center;font-size:22px;color:red;font-weight:700}#ipython_notebook img{height:28px}#site{width:100%;display:none;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;overflow:auto}@media print{#site{height:auto!important}}.ui-button .ui-button-text{padding:.2em .8em;font-size:77%}input.ui-button{padding:.3em .9em}span#login_widget{float:right}#logout,span#login_widget>.button{color:#333;background-color:#fff;border-color:#ccc}#logout.active,#logout.focus,#logout:active,#logout:focus,#logout:hover,.open>.dropdown-toggle#logout,.open>.dropdown-togglespan#login_widget>.button,span#login_widget>.button.active,span#login_widget>.button.focus,span#login_widget>.button:active,span#login_widget>.button:focus,span#login_widget>.button:hover{color:#333;background-color:#e6e6e6;border-color:#adadad}#logout.active,#logout:active,.open>.dropdown-toggle#logout,.open>.dropdown-togglespan#login_widget>.button,span#login_widget>.button.active,span#login_widget>.button:active{background-image:none}#logout.disabled,#logout.disabled.active,#logout.disabled.focus,#logout.disabled:active,#logout.disabled:focus,#logout.disabled:hover,#logout[disabled],#logout[disabled].active,#logout[disabled].focus,#logout[disabled]:active,#logout[disabled]:focus,#logout[disabled]:hover,fieldset[disabled] #logout,fieldset[disabled] #logout.active,fieldset[disabled] #logout.focus,fieldset[disabled] #logout:active,fieldset[disabled] #logout:focus,fieldset[disabled] #logout:hover,fieldset[disabled] span#login_widget>.button,fieldset[disabled] span#login_widget>.button.active,fieldset[disabled] span#login_widget>.button.focus,fieldset[disabled] span#login_widget>.button:active,fieldset[disabled] span#login_widget>.button:focus,fieldset[disabled] span#login_widget>.button:hover,span#login_widget>.button.disabled,span#login_widget>.button.disabled.active,span#login_widget>.button.disabled.focus,span#login_widget>.button.disabled:active,span#login_widget>.button.disabled:focus,span#login_widget>.button.disabled:hover,span#login_widget>.button[disabled],span#login_widget>.button[disabled].active,span#login_widget>.button[disabled].focus,span#login_widget>.button[disabled]:active,span#login_widget>.button[disabled]:focus,span#login_widget>.button[disabled]:hover{background-color:#fff;border-color:#ccc}#logout .badge,span#login_widget>.button .badge{color:#fff;background-color:#333}.nav-header{text-transform:none}#header>span{margin-top:10px}.modal_stretch .modal-dialog{display:-webkit-box;-webkit-box-orient:vertical;display:-moz-box;-moz-box-orient:vertical;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;min-height:80vh}.modal_stretch .modal-dialog .modal-body{max-height:calc(100vh - 200px);overflow:auto;flex:1}@media (min-width:768px){.modal .modal-dialog{width:700px}select.form-control{margin-left:12px;margin-right:12px}}/*!
*
* IPython auth
*
*/.center-nav{display:inline-block;margin-bottom:-4px}/*!
*
* IPython tree view
*
*/.alternate_upload{background-color:none;display:inline}.alternate_upload.form{padding:0;margin:0}.alternate_upload input.fileinput{text-align:center;vertical-align:middle;display:inline;opacity:0;z-index:2;width:12ex;margin-right:-12ex}.alternate_upload .btn-upload{height:22px}ul#tabs{margin-bottom:4px}ul#tabs a{padding-top:6px;padding-bottom:4px}ul.breadcrumb a:focus,ul.breadcrumb a:hover{text-decoration:none}ul.breadcrumb i.icon-home{font-size:16px;margin-right:4px}ul.breadcrumb span{color:#5e5e5e}.list_toolbar{padding:4px 0;vertical-align:middle}.list_toolbar .tree-buttons{padding-top:1px}.dynamic-buttons{padding-top:3px;display:inline-block}.list_toolbar [class*=span]{min-height:24px}.list_header{font-weight:700;background-color:#eee}.list_placeholder{font-weight:700;padding:4px 7px}.list_container{margin-top:4px;margin-bottom:20px;border:1px solid #ddd;border-radius:2px}.list_container>div{border-bottom:1px solid #ddd}.list_container>div:hover .list-item{background-color:red}.list_container>div:last-child{border:none}.list_item:hover .list_item{background-color:#ddd}.list_item a{text-decoration:none}.list_item:hover{background-color:#fafafa}.action_col{text-align:right}.list_header>div,.list_item>div{line-height:22px;padding:4px 7px}.list_header>div input,.list_item>div input{margin-right:7px;margin-left:14px;vertical-align:baseline;line-height:22px;position:relative;top:-1px}.list_header>div .item_link,.list_item>div .item_link{margin-left:-1px;vertical-align:baseline;line-height:22px}.new-file input[type=checkbox]{visibility:hidden}.item_name{line-height:22px;height:24px}.item_icon{font-size:14px;color:#5e5e5e;margin-right:7px;margin-left:7px;line-height:22px;vertical-align:baseline}.item_buttons{line-height:1em;margin-left:-5px}.item_buttons .btn-group,.item_buttons .input-group{float:left}.item_buttons>.btn,.item_buttons>.btn-group,.item_buttons>.input-group{margin-left:5px}.item_buttons .btn{min-width:13ex}.item_buttons .running-indicator{padding-top:4px;color:#5cb85c}.toolbar_info{height:24px;line-height:24px}input.engine_num_input,input.nbname_input{padding-top:3px;padding-bottom:3px;height:22px;line-height:14px;margin:0}input.engine_num_input{width:60px}.highlight_text{color:#00f}#project_name{display:inline-block;padding-left:7px;margin-left:-2px}#project_name>.breadcrumb{padding:0;margin-bottom:0;background-color:transparent;font-weight:700}#tree-selector{padding-right:0}#button-select-all{min-width:50px}#select-all{margin-left:7px;margin-right:2px}.menu_icon{margin-right:2px}.tab-content .row{margin-left:0;margin-right:0}.folder_icon:before{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;content:"\f114"}.folder_icon:before.pull-left{margin-right:.3em}.folder_icon:before.pull-right{margin-left:.3em}.notebook_icon:before{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;content:"\f02d";position:relative;top:-1px}.notebook_icon:before.pull-left{margin-right:.3em}.notebook_icon:before.pull-right{margin-left:.3em}.running_notebook_icon:before{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;content:"\f02d";position:relative;top:-1px;color:#5cb85c}.running_notebook_icon:before.pull-left{margin-right:.3em}.running_notebook_icon:before.pull-right{margin-left:.3em}.file_icon:before{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;content:"\f016";position:relative;top:-2px}.file_icon:before.pull-left{margin-right:.3em}.file_icon:before.pull-right{margin-left:.3em}#notebook_toolbar .pull-right{padding-top:0;margin-right:-1px}ul#new-menu{left:auto;right:0}.kernel-menu-icon{padding-right:12px;width:24px;content:"\f096"}.kernel-menu-icon:before{content:"\f096"}.kernel-menu-icon-current:before{content:"\f00c"}#tab_content{padding-top:20px}#running .panel-group .panel{margin-top:3px;margin-bottom:1em}#running .panel-group .panel .panel-heading{background-color:#eee;line-height:22px;padding:4px 7px}#running .panel-group .panel .panel-heading a:focus,#running .panel-group .panel .panel-heading a:hover{text-decoration:none}#running .panel-group .panel .panel-body{padding:0}#running .panel-group .panel .panel-body .list_container{margin-top:0;margin-bottom:0;border:0;border-radius:0}#running .panel-group .panel .panel-body .list_container .list_item{border-bottom:1px solid #ddd}#running .panel-group .panel .panel-body .list_container .list_item:last-child{border-bottom:0}.delete-button,.duplicate-button,.rename-button,.shutdown-button{display:none}.dynamic-instructions{display:inline-block;padding-top:4px}/*!
*
* IPython text editor webapp
*
*/.selected-keymap i.fa{padding:0 5px}.selected-keymap i.fa:before{content:"\f00c"}#mode-menu{overflow:auto;max-height:20em}.edit_app #header{-webkit-box-shadow:0 0 12px 1px rgba(87,87,87,.2);box-shadow:0 0 12px 1px rgba(87,87,87,.2)}.edit_app #menubar .navbar{margin-bottom:-1px}.dirty-indicator{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;width:20px}.dirty-indicator.pull-left{margin-right:.3em}.dirty-indicator.pull-right{margin-left:.3em}.dirty-indicator-dirty{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;width:20px}.dirty-indicator-dirty.pull-left{margin-right:.3em}.dirty-indicator-dirty.pull-right{margin-left:.3em}.dirty-indicator-clean{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;width:20px}.dirty-indicator-clean.pull-left{margin-right:.3em}.dirty-indicator-clean.pull-right{margin-left:.3em}.dirty-indicator-clean:before{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;content:"\f00c"}.dirty-indicator-clean:before.pull-left{margin-right:.3em}.dirty-indicator-clean:before.pull-right{margin-left:.3em}#filename{font-size:16pt;display:table;padding:0 5px}#current-mode{padding-left:5px;padding-right:5px}#texteditor-backdrop{padding-top:20px;padding-bottom:20px}@media not print{#texteditor-backdrop{background-color:#eee}}@media print{#texteditor-backdrop #texteditor-container .CodeMirror-gutter,#texteditor-backdrop #texteditor-container .CodeMirror-gutters{background-color:#fff}}@media not print{#texteditor-backdrop #texteditor-container .CodeMirror-gutter,#texteditor-backdrop #texteditor-container .CodeMirror-gutters{background-color:#fff}#texteditor-backdrop #texteditor-container{padding:0;background-color:#fff;-webkit-box-shadow:0 0 12px 1px rgba(87,87,87,.2);box-shadow:0 0 12px 1px rgba(87,87,87,.2)}}/*!
*
* IPython notebook
*
*/.ansibold{font-weight:700}.ansiblack{color:#000}.ansired{color:#8b0000}.ansigreen{color:#006400}.ansiyellow{color:#c4a000}.ansiblue{color:#00008b}.ansipurple{color:#9400d3}.ansicyan{color:#4682b4}.ansigray{color:gray}.ansibgblack{background-color:#000}.ansibgred{background-color:red}.ansibggreen{background-color:green}.ansibgyellow{background-color:#ff0}.ansibgblue{background-color:#00f}.ansibgpurple{background-color:#ff00ff}.ansibgcyan{background-color:#0ff}.ansibggray{background-color:gray}div.cell{border:1px solid transparent;display:-webkit-box;-webkit-box-orient:vertical;display:-moz-box;-moz-box-orient:vertical;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;border-radius:2px;box-sizing:border-box;-moz-box-sizing:border-box;border-width:thin;border-style:solid;width:100%;padding:5px;margin:0;outline:0}div.cell.selected{border-color:#ababab}@media print{div.cell.selected{border-color:transparent}}.edit_mode div.cell.selected{border-color:green}.prompt{min-width:14ex;padding:.4em;margin:0;font-family:monospace;text-align:right;line-height:1.21429em}div.inner_cell{display:-webkit-box;-webkit-box-orient:vertical;display:-moz-box;-moz-box-orient:vertical;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}@-moz-document url-prefix(){div.inner_cell{overflow-x:hidden}}div.input_area{border:1px solid #cfcfcf;border-radius:2px;background:#f7f7f7;line-height:1.21429em}div.prompt:empty{padding-top:0;padding-bottom:0}div.unrecognized_cell{padding:5px 5px 5px 0;display:-webkit-box;-webkit-box-orient:horizontal;display:-moz-box;-moz-box-orient:horizontal;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}div.unrecognized_cell .inner_cell{border-radius:2px;padding:5px;font-weight:700;color:red;border:1px solid #cfcfcf;background:#eaeaea}div.unrecognized_cell .inner_cell a,div.unrecognized_cell .inner_cell a:hover{color:inherit;text-decoration:none}@media (max-width:540px){.prompt{text-align:left}div.unrecognized_cell>div.prompt{display:none}}div.code_cell{}div.input{page-break-inside:avoid;display:-webkit-box;-webkit-box-orient:horizontal;display:-moz-box;-moz-box-orient:horizontal;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}@media (max-width:540px){div.input{-webkit-box-orient:vertical;-moz-box-orient:vertical;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}}div.input_prompt{color:navy;border-top:1px solid transparent}div.input_area>div.highlight{margin:.4em;border:none;padding:0;background-color:transparent}div.input_area>div.highlight>pre{margin:0;border:none;padding:0;background-color:transparent}.CodeMirror{line-height:1.21429em;font-size:14px;height:auto;background:0 0}.CodeMirror-scroll{overflow-y:hidden;overflow-x:auto}.CodeMirror-lines{padding:.4em}.CodeMirror-linenumber{padding:0 8px 0 4px}.CodeMirror-gutters{border-bottom-left-radius:2px;border-top-left-radius:2px}.CodeMirror pre{padding:0;border:0;border-radius:0}.highlight-base,.highlight-variable{color:#000}.highlight-variable-2{color:#1a1a1a}.highlight-variable-3{color:#333}.highlight-string{color:#BA2121}.highlight-comment{color:#408080;font-style:italic}.highlight-number{color:#080}.highlight-atom{color:#88F}.highlight-keyword{color:green;font-weight:700}.highlight-builtin{color:green}.highlight-error{color:red}.highlight-operator{color:#A2F;font-weight:700}.highlight-meta{color:#A2F}.highlight-def{color:#00f}.highlight-string-2{color:#f50}.highlight-qualifier{color:#555}.highlight-bracket{color:#997}.highlight-tag{color:#170}.highlight-attribute{color:#00c}.highlight-header{color:#00f}.highlight-quote{color:#090}.highlight-link{color:#00c}.cm-s-ipython span.cm-keyword{color:green;font-weight:700}.cm-s-ipython span.cm-atom{color:#88F}.cm-s-ipython span.cm-number{color:#080}.cm-s-ipython span.cm-def{color:#00f}.cm-s-ipython span.cm-variable{color:#000}.cm-s-ipython span.cm-operator{color:#A2F;font-weight:700}.cm-s-ipython span.cm-variable-2{color:#1a1a1a}.cm-s-ipython span.cm-variable-3{color:#333}.cm-s-ipython span.cm-comment{color:#408080;font-style:italic}.cm-s-ipython span.cm-string{color:#BA2121}.cm-s-ipython span.cm-string-2{color:#f50}.cm-s-ipython span.cm-meta{color:#A2F}.cm-s-ipython span.cm-qualifier{color:#555}.cm-s-ipython span.cm-builtin{color:green}.cm-s-ipython span.cm-bracket{color:#997}.cm-s-ipython span.cm-tag{color:#170}.cm-s-ipython span.cm-attribute{color:#00c}.cm-s-ipython span.cm-header{color:#00f}.cm-s-ipython span.cm-quote{color:#090}.cm-s-ipython span.cm-link{color:#00c}.cm-s-ipython span.cm-error{color:red}.cm-s-ipython span.cm-tab{background:url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=')right no-repeat}div.output_wrapper{display:-webkit-box;-webkit-box-align:stretch;display:-moz-box;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;z-index:1}div.output_scroll{height:24em;width:100%;overflow:auto;border-radius:2px;-webkit-box-shadow:inset 0 2px 8px rgba(0,0,0,.8);box-shadow:inset 0 2px 8px rgba(0,0,0,.8);display:block}div.output_collapsed{margin:0;padding:0;display:-webkit-box;-webkit-box-orient:vertical;display:-moz-box;-moz-box-orient:vertical;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}div.out_prompt_overlay{height:100%;padding:0 .4em;position:absolute;border-radius:2px}div.out_prompt_overlay:hover{-webkit-box-shadow:inset 0 0 1px #000;box-shadow:inset 0 0 1px #000;background:rgba(240,240,240,.5)}div.output_prompt{color:#8b0000}div.output_area{padding:0;page-break-inside:avoid;display:-webkit-box;-webkit-box-orient:horizontal;display:-moz-box;-moz-box-orient:horizontal;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}div.output_area .MathJax_Display{text-align:left!important}div.output_area .rendered_html img,div.output_area .rendered_html table{margin-left:0;margin-right:0}div.output_area img,div.output_area svg{max-width:100%;height:auto}div.output_area img.unconfined,div.output_area svg.unconfined{max-width:none}.output{display:-webkit-box;-webkit-box-orient:vertical;display:-moz-box;-moz-box-orient:vertical;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}@media (max-width:540px){div.output_area{-webkit-box-orient:vertical;-moz-box-orient:vertical;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}}div.output_area pre{margin:0;padding:0;border:0;vertical-align:baseline;color:#000;background-color:transparent;border-radius:0}div.output_subarea{overflow-x:auto;padding:.4em;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1;max-width:calc(100% - 14ex)}div.output_text{text-align:left;color:#000;line-height:1.21429em}div.output_stderr{background:#fdd}div.output_latex{text-align:left}div.output_javascript:empty{padding:0}.js-error{color:#8b0000}div.raw_input_container{font-family:monospace;padding-top:5px}span.raw_input_prompt{}input.raw_input{font-family:inherit;font-size:inherit;color:inherit;width:auto;vertical-align:baseline;padding:0 .25em;margin:0 .25em}input.raw_input:focus{box-shadow:none}p.p-space{margin-bottom:10px}div.output_unrecognized{padding:5px;font-weight:700;color:red}div.output_unrecognized a,div.output_unrecognized a:hover{color:inherit;text-decoration:none}.rendered_html{color:#000}.rendered_html em{font-style:italic}.rendered_html strong{font-weight:700}.rendered_html :link,.rendered_html :visited,.rendered_html u{text-decoration:underline}.rendered_html h1{font-size:185.7%;margin:1.08em 0 0;font-weight:700;line-height:1}.rendered_html h2{font-size:157.1%;margin:1.27em 0 0;font-weight:700;line-height:1}.rendered_html h3{font-size:128.6%;margin:1.55em 0 0;font-weight:700;line-height:1}.rendered_html h4{font-size:100%;margin:2em 0 0;font-weight:700;line-height:1}.rendered_html h5,.rendered_html h6{font-size:100%;margin:2em 0 0;font-weight:700;line-height:1;font-style:italic}.rendered_html h1:first-child{margin-top:.538em}.rendered_html h2:first-child{margin-top:.636em}.rendered_html h3:first-child{margin-top:.777em}.rendered_html h4:first-child,.rendered_html h5:first-child,.rendered_html h6:first-child{margin-top:1em}.rendered_html ul{list-style:disc;margin:0 2em;padding-left:0}.rendered_html ul ul{list-style:square;margin:0 2em}.rendered_html ul ul ul{list-style:circle;margin:0 2em}.rendered_html ol{list-style:decimal;margin:0 2em;padding-left:0}.rendered_html ol ol{list-style:upper-alpha;margin:0 2em}.rendered_html ol ol ol{list-style:lower-alpha;margin:0 2em}.rendered_html ol ol ol ol{list-style:lower-roman;margin:0 2em}.rendered_html ol ol ol ol ol{list-style:decimal;margin:0 2em}.rendered_html *+ol,.rendered_html *+ul{margin-top:1em}.rendered_html hr{color:#000;background-color:#000}.rendered_html pre{margin:1em 2em}.rendered_html code,.rendered_html pre{border:0;background-color:#fff;color:#000;font-size:100%;padding:0}.rendered_html blockquote{margin:1em 2em}.rendered_html table{margin-left:auto;margin-right:auto;border:1px solid #000;border-collapse:collapse}.rendered_html td,.rendered_html th,.rendered_html tr{border:1px solid #000;border-collapse:collapse;margin:1em 2em}.rendered_html td,.rendered_html th{text-align:left;vertical-align:middle;padding:4px}.rendered_html th{font-weight:700}.rendered_html *+table{margin-top:1em}.rendered_html p{text-align:left}.rendered_html *+p{margin-top:1em}.rendered_html img{display:block;margin-left:auto;margin-right:auto}.rendered_html *+img{margin-top:1em}.rendered_html img,.rendered_html svg{max-width:100%;height:auto}.rendered_html img.unconfined,.rendered_html svg.unconfined{max-width:none}div.text_cell{display:-webkit-box;-webkit-box-orient:horizontal;display:-moz-box;-moz-box-orient:horizontal;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}@media (max-width:540px){div.text_cell>div.prompt{display:none}}div.text_cell_render{outline:0;resize:none;width:inherit;border-style:none;padding:.5em .5em .5em .4em;color:#000;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}a.anchor-link:link{text-decoration:none;padding:0 20px;visibility:hidden}h1:hover .anchor-link,h2:hover .anchor-link,h3:hover .anchor-link,h4:hover .anchor-link,h5:hover .anchor-link,h6:hover .anchor-link{visibility:visible}.text_cell.rendered .input_area{display:none}.text_cell.rendered .rendered_html{overflow-x:auto}.text_cell.unrendered .text_cell_render{display:none}.cm-header-1,.cm-header-2,.cm-header-3,.cm-header-4,.cm-header-5,.cm-header-6{font-weight:700;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif}.cm-header-1{font-size:185.7%}.cm-header-2{font-size:157.1%}.cm-header-3{font-size:128.6%}.cm-header-4{font-size:110%}.cm-header-5,.cm-header-6{font-size:100%;font-style:italic}/*!
*
* IPython notebook webapp
*
*/@media (max-width:767px){.notebook_app{padding-left:0;padding-right:0}}#ipython-main-app{box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;height:100%}div#notebook_panel{margin:0;padding:0;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;height:100%}#notebook{font-size:14px;line-height:20px;overflow-y:hidden;overflow-x:auto;width:100%;padding-top:20px;margin:0;outline:0;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;min-height:100%}@media not print{#notebook-container{padding:15px;background-color:#fff;min-height:0;-webkit-box-shadow:0 0 12px 1px rgba(87,87,87,.2);box-shadow:0 0 12px 1px rgba(87,87,87,.2)}}div.ui-widget-content{border:1px solid #ababab;outline:0}pre.dialog{background-color:#f7f7f7;border:1px solid #ddd;border-radius:2px;padding:.4em .4em .4em 2em}p.dialog{padding:.2em}code,kbd,pre,samp{white-space:pre-wrap}#fonttest{font-family:monospace}p{margin-bottom:0}.end_space{min-height:100px;transition:height .2s ease}.notebook_app #header{-webkit-box-shadow:0 0 12px 1px rgba(87,87,87,.2);box-shadow:0 0 12px 1px rgba(87,87,87,.2)}@media not print{.notebook_app{background-color:#eee}}.celltoolbar{border:thin solid #CFCFCF;border-bottom:none;background:#EEE;border-radius:2px 2px 0 0;width:100%;height:29px;padding-right:4px;-webkit-box-orient:horizontal;-moz-box-orient:horizontal;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch;-webkit-box-pack:end;-moz-box-pack:end;box-pack:end;justify-content:flex-end;font-size:87%;padding-top:3px}@media print{.edit_mode div.cell.selected{border-color:transparent}div.code_cell{page-break-inside:avoid}#notebook-container{width:100%}.celltoolbar{display:none}}.ctb_hideshow{display:none;vertical-align:bottom}.ctb_global_show .ctb_show.ctb_hideshow{display:block}.ctb_global_show .ctb_show+.input_area,.ctb_global_show .ctb_show+div.text_cell_input,.ctb_global_show .ctb_show~div.text_cell_render{border-top-right-radius:0;border-top-left-radius:0}.ctb_global_show .ctb_show~div.text_cell_render{border:1px solid #cfcfcf}.celltoolbar select{color:#555;background-color:#fff;background-image:none;border:1px solid #ccc;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-webkit-transition:border-color ease-in-out .15s,box-shadow ease-in-out .15s;-o-transition:border-color ease-in-out .15s,box-shadow ease-in-out .15s;transition:border-color ease-in-out .15s,box-shadow ease-in-out .15s;line-height:1.5;border-radius:1px;width:inherit;font-size:inherit;height:22px;padding:0;display:inline-block}.celltoolbar select:focus{border-color:#66afe9;outline:0;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 8px rgba(102,175,233,.6);box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 8px rgba(102,175,233,.6)}.celltoolbar select::-moz-placeholder{color:#999;opacity:1}.celltoolbar select:-ms-input-placeholder{color:#999}.celltoolbar select::-webkit-input-placeholder{color:#999}.celltoolbar select[disabled],.celltoolbar select[readonly],fieldset[disabled] .celltoolbar select{background-color:#eee;opacity:1}.celltoolbar select[disabled],fieldset[disabled] .celltoolbar select{cursor:not-allowed}textarea.celltoolbar select{height:auto}select.celltoolbar select{height:30px;line-height:30px}select[multiple].celltoolbar select,textarea.celltoolbar select{height:auto}.celltoolbar label{margin-left:5px;margin-right:5px}.completions{position:absolute;z-index:10;overflow:hidden;border:1px solid #ababab;border-radius:2px;-webkit-box-shadow:0 6px 10px -1px #adadad;box-shadow:0 6px 10px -1px #adadad;line-height:1}.completions select{background:#fff;outline:0;border:none;padding:0;margin:0;overflow:auto;font-family:monospace;font-size:110%;color:#000;width:auto}.completions select option.context{color:#286090}#kernel_logo_widget{float:right!important;float:right}#kernel_logo_widget .current_kernel_logo{display:none;margin-top:-1px;margin-bottom:-1px;width:32px;height:32px}#menubar{box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;margin-top:1px}#menubar .navbar{border-top:1px;border-radius:0 0 2px 2px;margin-bottom:0}#menubar .navbar-toggle{float:left;padding-top:7px;padding-bottom:7px;border:none}#menubar .navbar-collapse{clear:left}.nav-wrapper{border-bottom:1px solid #e7e7e7}i.menu-icon{padding-top:4px}ul#help_menu li a{overflow:hidden;padding-right:2.2em}ul#help_menu li a i{margin-right:-1.2em}.dropdown-submenu{position:relative}.dropdown-submenu>.dropdown-menu{top:0;left:100%;margin-top:-6px;margin-left:-1px}.dropdown-submenu:hover>.dropdown-menu{display:block}.dropdown-submenu>a:after{font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;display:block;content:"\f0da";float:right;color:#333;margin-top:2px;margin-right:-10px}.dropdown-submenu>a:after.pull-left{margin-right:.3em}.dropdown-submenu>a:after.pull-right{margin-left:.3em}.dropdown-submenu:hover>a:after{color:#262626}.dropdown-submenu.pull-left{float:none}.dropdown-submenu.pull-left>.dropdown-menu{left:-100%;margin-left:10px}#notification_area{float:right!important;float:right;z-index:10}.indicator_area{float:right!important;float:right;color:#777;margin-left:5px;margin-right:5px;z-index:10;text-align:center;width:auto}#kernel_indicator{float:right!important;float:right;color:#777;margin-left:5px;margin-right:5px;z-index:10;text-align:center;width:auto;border-left:1px solid}#kernel_indicator .kernel_indicator_name{padding-left:5px;padding-right:5px}#modal_indicator{float:right!important;float:right;color:#777;margin-left:5px;margin-right:5px;z-index:10;text-align:center;width:auto}#readonly-indicator{float:right!important;float:right;color:#777;z-index:10;text-align:center;width:auto;display:none;margin:2px 0 0}.modal_indicator:before{width:1.28571429em;text-align:center}.edit_mode .modal_indicator:before{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;content:"\f040"}.edit_mode .modal_indicator:before.pull-left{margin-right:.3em}.edit_mode .modal_indicator:before.pull-right{margin-left:.3em}.command_mode .modal_indicator:before{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;content:' '}.command_mode .modal_indicator:before.pull-left{margin-right:.3em}.command_mode .modal_indicator:before.pull-right{margin-left:.3em}.kernel_idle_icon:before{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;content:"\f10c"}.kernel_idle_icon:before.pull-left{margin-right:.3em}.kernel_idle_icon:before.pull-right{margin-left:.3em}.kernel_busy_icon:before{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;content:"\f111"}.kernel_busy_icon:before.pull-left{margin-right:.3em}.kernel_busy_icon:before.pull-right{margin-left:.3em}.kernel_dead_icon:before{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;content:"\f1e2"}.kernel_dead_icon:before.pull-left{margin-right:.3em}.kernel_dead_icon:before.pull-right{margin-left:.3em}.kernel_disconnected_icon:before{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;content:"\f127"}.kernel_disconnected_icon:before.pull-left{margin-right:.3em}.kernel_disconnected_icon:before.pull-right{margin-left:.3em}.notification_widget{z-index:10;background:rgba(240,240,240,.5);margin-right:4px;color:#333;background-color:#fff;border-color:#ccc}.notification_widget.active,.notification_widget.focus,.notification_widget:active,.notification_widget:focus,.notification_widget:hover,.open>.dropdown-toggle.notification_widget{color:#333;background-color:#e6e6e6;border-color:#adadad}.notification_widget.active,.notification_widget:active,.open>.dropdown-toggle.notification_widget{background-image:none}.notification_widget.disabled,.notification_widget.disabled.active,.notification_widget.disabled.focus,.notification_widget.disabled:active,.notification_widget.disabled:focus,.notification_widget.disabled:hover,.notification_widget[disabled],.notification_widget[disabled].active,.notification_widget[disabled].focus,.notification_widget[disabled]:active,.notification_widget[disabled]:focus,.notification_widget[disabled]:hover,fieldset[disabled] .notification_widget,fieldset[disabled] .notification_widget.active,fieldset[disabled] .notification_widget.focus,fieldset[disabled] .notification_widget:active,fieldset[disabled] .notification_widget:focus,fieldset[disabled] .notification_widget:hover{background-color:#fff;border-color:#ccc}.notification_widget .badge{color:#fff;background-color:#333}.notification_widget.warning{color:#fff;background-color:#f0ad4e;border-color:#eea236}.notification_widget.warning.active,.notification_widget.warning.focus,.notification_widget.warning:active,.notification_widget.warning:focus,.notification_widget.warning:hover,.open>.dropdown-toggle.notification_widget.warning{color:#fff;background-color:#ec971f;border-color:#d58512}.notification_widget.warning.active,.notification_widget.warning:active,.open>.dropdown-toggle.notification_widget.warning{background-image:none}.notification_widget.warning.disabled,.notification_widget.warning.disabled.active,.notification_widget.warning.disabled.focus,.notification_widget.warning.disabled:active,.notification_widget.warning.disabled:focus,.notification_widget.warning.disabled:hover,.notification_widget.warning[disabled],.notification_widget.warning[disabled].active,.notification_widget.warning[disabled].focus,.notification_widget.warning[disabled]:active,.notification_widget.warning[disabled]:focus,.notification_widget.warning[disabled]:hover,fieldset[disabled] .notification_widget.warning,fieldset[disabled] .notification_widget.warning.active,fieldset[disabled] .notification_widget.warning.focus,fieldset[disabled] .notification_widget.warning:active,fieldset[disabled] .notification_widget.warning:focus,fieldset[disabled] .notification_widget.warning:hover{background-color:#f0ad4e;border-color:#eea236}.notification_widget.warning .badge{color:#f0ad4e;background-color:#fff}.notification_widget.success{color:#fff;background-color:#5cb85c;border-color:#4cae4c}.notification_widget.success.active,.notification_widget.success.focus,.notification_widget.success:active,.notification_widget.success:focus,.notification_widget.success:hover,.open>.dropdown-toggle.notification_widget.success{color:#fff;background-color:#449d44;border-color:#398439}.notification_widget.success.active,.notification_widget.success:active,.open>.dropdown-toggle.notification_widget.success{background-image:none}.notification_widget.success.disabled,.notification_widget.success.disabled.active,.notification_widget.success.disabled.focus,.notification_widget.success.disabled:active,.notification_widget.success.disabled:focus,.notification_widget.success.disabled:hover,.notification_widget.success[disabled],.notification_widget.success[disabled].active,.notification_widget.success[disabled].focus,.notification_widget.success[disabled]:active,.notification_widget.success[disabled]:focus,.notification_widget.success[disabled]:hover,fieldset[disabled] .notification_widget.success,fieldset[disabled] .notification_widget.success.active,fieldset[disabled] .notification_widget.success.focus,fieldset[disabled] .notification_widget.success:active,fieldset[disabled] .notification_widget.success:focus,fieldset[disabled] .notification_widget.success:hover{background-color:#5cb85c;border-color:#4cae4c}.notification_widget.success .badge{color:#5cb85c;background-color:#fff}.notification_widget.info{color:#fff;background-color:#5bc0de;border-color:#46b8da}.notification_widget.info.active,.notification_widget.info.focus,.notification_widget.info:active,.notification_widget.info:focus,.notification_widget.info:hover,.open>.dropdown-toggle.notification_widget.info{color:#fff;background-color:#31b0d5;border-color:#269abc}.notification_widget.info.active,.notification_widget.info:active,.open>.dropdown-toggle.notification_widget.info{background-image:none}.notification_widget.info.disabled,.notification_widget.info.disabled.active,.notification_widget.info.disabled.focus,.notification_widget.info.disabled:active,.notification_widget.info.disabled:focus,.notification_widget.info.disabled:hover,.notification_widget.info[disabled],.notification_widget.info[disabled].active,.notification_widget.info[disabled].focus,.notification_widget.info[disabled]:active,.notification_widget.info[disabled]:focus,.notification_widget.info[disabled]:hover,fieldset[disabled] .notification_widget.info,fieldset[disabled] .notification_widget.info.active,fieldset[disabled] .notification_widget.info.focus,fieldset[disabled] .notification_widget.info:active,fieldset[disabled] .notification_widget.info:focus,fieldset[disabled] .notification_widget.info:hover{background-color:#5bc0de;border-color:#46b8da}.notification_widget.info .badge{color:#5bc0de;background-color:#fff}.notification_widget.danger{color:#fff;background-color:#d9534f;border-color:#d43f3a}.notification_widget.danger.active,.notification_widget.danger.focus,.notification_widget.danger:active,.notification_widget.danger:focus,.notification_widget.danger:hover,.open>.dropdown-toggle.notification_widget.danger{color:#fff;background-color:#c9302c;border-color:#ac2925}.notification_widget.danger.active,.notification_widget.danger:active,.open>.dropdown-toggle.notification_widget.danger{background-image:none}.notification_widget.danger.disabled,.notification_widget.danger.disabled.active,.notification_widget.danger.disabled.focus,.notification_widget.danger.disabled:active,.notification_widget.danger.disabled:focus,.notification_widget.danger.disabled:hover,.notification_widget.danger[disabled],.notification_widget.danger[disabled].active,.notification_widget.danger[disabled].focus,.notification_widget.danger[disabled]:active,.notification_widget.danger[disabled]:focus,.notification_widget.danger[disabled]:hover,fieldset[disabled] .notification_widget.danger,fieldset[disabled] .notification_widget.danger.active,fieldset[disabled] .notification_widget.danger.focus,fieldset[disabled] .notification_widget.danger:active,fieldset[disabled] .notification_widget.danger:focus,fieldset[disabled] .notification_widget.danger:hover{background-color:#d9534f;border-color:#d43f3a}.notification_widget.danger .badge{color:#d9534f;background-color:#fff}div#pager{background-color:#fff;font-size:14px;line-height:20px;overflow:hidden;display:none;position:fixed;bottom:0;width:100%;max-height:50%;padding-top:8px;-webkit-box-shadow:0 0 12px 1px rgba(87,87,87,.2);box-shadow:0 0 12px 1px rgba(87,87,87,.2);z-index:100;top:auto!important}div#pager pre{line-height:1.21429em;color:#000;background-color:#f7f7f7;padding:.4em}div#pager #pager-button-area{position:absolute;top:8px;right:20px}div#pager #pager-contents{position:relative;overflow:auto;width:100%;height:100%}div#pager #pager-contents #pager-container{position:relative;padding:15px 0;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}div#pager .ui-resizable-handle{top:0;height:8px;background:#f7f7f7;border-top:1px solid #cfcfcf;border-bottom:1px solid #cfcfcf}div#pager .ui-resizable-handle::after{content:'';top:2px;left:50%;height:3px;width:30px;margin-left:-15px;position:absolute;border-top:1px solid #cfcfcf}.quickhelp{display:-webkit-box;-webkit-box-orient:horizontal;display:-moz-box;-moz-box-orient:horizontal;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}.shortcut_key{display:inline-block;width:20ex;text-align:right;font-family:monospace}.shortcut_descr{display:inline-block;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}span.save_widget{margin-top:6px}span.save_widget span.filename{height:1em;line-height:1em;padding:3px;margin-left:16px;border:none;font-size:146.5%;border-radius:2px}span.save_widget span.filename:hover{background-color:#e6e6e6}span.autosave_status,span.checkpoint_status{font-size:small}@media (max-width:767px){span.save_widget{font-size:small}span.autosave_status,span.checkpoint_status{display:none}}@media (min-width:768px)and (max-width:991px){span.checkpoint_status{display:none}span.autosave_status{font-size:x-small}}.toolbar{padding:0;margin-left:-5px;margin-top:2px;margin-bottom:5px;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}.toolbar label,.toolbar select{width:auto;vertical-align:middle;margin-bottom:0;display:inline;font-size:92%;margin-left:.3em;margin-right:.3em;padding:3px 0 0}.toolbar .btn{padding:2px 8px}.toolbar .btn-group{margin-top:0;margin-left:5px}#maintoolbar{margin-bottom:-3px;margin-top:-8px;border:0;min-height:27px;margin-left:0;padding-top:11px;padding-bottom:3px}#maintoolbar .navbar-text{float:none;vertical-align:middle;text-align:right;margin-left:5px;margin-right:0;margin-top:0}.select-xs{height:24px}@-moz-keyframes fadeOut{from{opacity:1}to{opacity:0}}@-webkit-keyframes fadeOut{from{opacity:1}to{opacity:0}}@-moz-keyframes fadeIn{from{opacity:0}to{opacity:1}}@-webkit-keyframes fadeIn{from{opacity:0}to{opacity:1}}.bigtooltip{overflow:auto;height:200px;-webkit-transition-property:height;-webkit-transition-duration:500ms;-moz-transition-property:height;-moz-transition-duration:500ms;transition-property:height;transition-duration:500ms}.smalltooltip{-webkit-transition-property:height;-webkit-transition-duration:500ms;-moz-transition-property:height;-moz-transition-duration:500ms;transition-property:height;transition-duration:500ms;text-overflow:ellipsis;overflow:hidden;height:80px}.tooltipbuttons{position:absolute;padding-right:15px;top:0;right:0}.tooltiptext{padding-right:30px}.ipython_tooltip{max-width:700px;animation:fadeOut 400ms;-webkit-animation:fadeIn 400ms;-moz-animation:fadeIn 400ms;animation:fadeIn 400ms;vertical-align:middle;background-color:#f7f7f7;overflow:visible;border:1px solid #ababab;outline:0;padding:3px 3px 3px 7px;padding-left:7px;font-family:monospace;min-height:50px;-moz-box-shadow:0 6px 10px -1px #adadad;-webkit-box-shadow:0 6px 10px -1px #adadad;box-shadow:0 6px 10px -1px #adadad;border-radius:2px;position:absolute;z-index:1000}.ipython_tooltip a{float:right}.ipython_tooltip .tooltiptext pre{border:0;border-radius:0;font-size:100%;background-color:#f7f7f7}.pretooltiparrow{left:0;margin:0;top:-16px;width:40px;height:16px;overflow:hidden;position:absolute}.pretooltiparrow:before{background-color:#f7f7f7;border:1px solid #ababab;z-index:11;content:"";position:absolute;left:15px;top:10px;width:25px;height:25px;-webkit-transform:rotate(45deg);-moz-transform:rotate(45deg);-ms-transform:rotate(45deg);-o-transform:rotate(45deg)}.terminal-app{background:#eee}.terminal-app #header{background:#fff;-webkit-box-shadow:0 0 12px 1px rgba(87,87,87,.2);box-shadow:0 0 12px 1px rgba(87,87,87,.2)}.terminal-app .terminal{float:left;font-family:monospace;color:#fff;background:#000;padding:.4em;border-radius:2px;-webkit-box-shadow:0 0 12px 1px rgba(87,87,87,.4);box-shadow:0 0 12px 1px rgba(87,87,87,.4)}.terminal-app .terminal,.terminal-app .terminal dummy-screen{line-height:1em;font-size:14px}.terminal-app .terminal-cursor{color:#000;background:#fff}.terminal-app #terminado-container{margin-top:20px}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}

@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Wrangling--OpenStreetMap-Data--with-MongoDB">Wrangling  OpenStreetMap Data  with MongoDB<a class="anchor-link" href="#Wrangling--OpenStreetMap-Data--with-MongoDB">&#182;</a></h1><h3 id="by-Duc-Vu-in-fulfillment-of-Udacity&#8217;s-Data-Analyst-Nanodegree,-Project-3">by Duc Vu in fulfillment of Udacity&#8217;s Data Analyst Nanodegree, Project 3<a class="anchor-link" href="#by-Duc-Vu-in-fulfillment-of-Udacity&#8217;s-Data-Analyst-Nanodegree,-Project-3">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>OpenStreetMap is an open project that lets eveyone use and create a free editable map of the world.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="1.-Chosen-Map-Area">1. Chosen Map Area<a class="anchor-link" href="#1.-Chosen-Map-Area">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In this project, I choose to analyze data from Boston, Massachusetts want to show you to fix one type of error, that is the address of the street. And not only that, I also will show you how to put the data that has been audited into MongoDB instance. We also use MongoDB's Agregation Framework to get overview and analysis of the data</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[80]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">HTML</span>
<span class="n">HTML</span><span class="p">(</span><span class="s">&#39;&lt;iframe width=&quot;425&quot; height=&quot;350&quot; frameborder=&quot;0&quot; scrolling=&quot;no&quot; marginheight=&quot;0&quot; marginwidth=&quot;0&quot; </span><span class="se">\</span>
<span class="s">src=&quot;http://www.openstreetmap.org/export/embed.html?bbox=-71.442,42.1858,-70.6984,42.4918&amp;amp;layer=mapnik&quot;&gt;&lt;/iframe&gt;&lt;br/&gt;&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[80]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://www.openstreetmap.org/export/embed.html?bbox=-71.442,42.1858,-70.6984,42.4918&amp;layer=mapnik"></iframe><br/>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The dataset is here <a href="https://s3.amazonaws.com/metro-extracts.mapzen.com/boston_massachusetts.osm.bz2">https://s3.amazonaws.com/metro-extracts.mapzen.com/boston_massachusetts.osm.bz2</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">filename</span> <span class="o">=</span> <span class="s">&#39;boston_massachusetts.osm&#39;</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I used the Overpass API to download the OpenStreetMap XML for the corresponding bounding box:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="2.-Auditing-the-Data">2. Auditing the Data<a class="anchor-link" href="#2.-Auditing-the-Data">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In this project, I will parse through the downloaded OSM XML file with ElementTree and find the number of each type of element since the XML file are too large to work with in memory.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">import</span> <span class="nn">xml.etree.cElementTree</span> <span class="kn">as</span> <span class="nn">ET</span>
<span class="kn">import</span> <span class="nn">pprint</span>

<span class="k">def</span> <span class="nf">count_tags</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">    this function will return a dictionary with the tag name as the key </span>
<span class="sd">    and number of times this tag can be encountered in the map as value.</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">tags</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">for</span> <span class="n">event</span><span class="p">,</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">ET</span><span class="o">.</span><span class="n">iterparse</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
            <span class="n">tags</span><span class="p">[</span><span class="n">elem</span><span class="o">.</span><span class="n">tag</span><span class="p">]</span> <span class="o">+=</span><span class="mi">1</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">tags</span><span class="p">[</span><span class="n">elem</span><span class="o">.</span><span class="n">tag</span><span class="p">]</span><span class="o">=</span> <span class="mi">1</span>
                
    <span class="k">return</span> <span class="n">tags</span>
<span class="n">tags</span> <span class="o">=</span> <span class="n">count_tags</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span>
<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>{&apos;bounds&apos;: 1,
 &apos;member&apos;: 9586,
 &apos;nd&apos;: 2242045,
 &apos;node&apos;: 1886391,
 &apos;osm&apos;: 1,
 &apos;relation&apos;: 1186,
 &apos;tag&apos;: 846441,
 &apos;way&apos;: 294246}
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Before processing the data and add it into MongoDB, I should check the "k" value for each 'tag' and see if they can be valid keys in MongoDB, as well as see if there are any other potential problems.</p>
<p>I have built 3 regular expressions to check for certain patterns in the tags to change the data model
and expand the "addr:street" type of keys to a dictionary like this:</p>
<p>Here are three regular expressions: lower, lower_colon, and problemchars.</p>
<ul>
<li>lower: matches strings containing lower case characters</li>
<li>lower_colon: matches strings containing lower case characters and a single colon within the string</li>
<li>problemchars: matches characters that cannot be used within keys in MongoDB</li>
</ul>
<ul>
<li>example: {"address": {"street": "Some value"}}</li>
</ul>
<p>So, we have to see if we have such tags, and if we have any tags with problematic characters.
Please complete the function 'key_type'.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">import</span> <span class="nn">re</span>

<span class="n">lower</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^([a-z]|_)*$&#39;</span><span class="p">)</span>
<span class="n">lower_colon</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^([a-z]|_)*:([a-z]|_)*$&#39;</span><span class="p">)</span>
<span class="n">problemchars</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;[=\+/&amp;&lt;&gt;;</span><span class="se">\&#39;</span><span class="s">&quot;\?%#$@\,\. \t\r\n]&#39;</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">key_type</span><span class="p">(</span><span class="n">element</span><span class="p">,</span> <span class="n">keys</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">     this function counts number of times the unusual tag element can be encountered in the map.</span>
<span class="sd">    Args:</span>
<span class="sd">        element(string): tag element in the map.</span>
<span class="sd">        keys(int): number of that encountered tag in the map</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="k">if</span> <span class="n">element</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="s">&quot;tag&quot;</span><span class="p">:</span>

        <span class="k">if</span> <span class="n">lower</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">element</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="s">&#39;k&#39;</span><span class="p">]):</span>
            <span class="n">keys</span><span class="p">[</span><span class="s">&quot;lower&quot;</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">elif</span> <span class="n">lower_colon</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">element</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="s">&#39;k&#39;</span><span class="p">]):</span>
            <span class="n">keys</span><span class="p">[</span><span class="s">&quot;lower_colon&quot;</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">elif</span> <span class="n">problemchars</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">element</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="s">&#39;k&#39;</span><span class="p">]):</span>
            <span class="n">keys</span><span class="p">[</span><span class="s">&quot;problemchars&quot;</span><span class="p">]</span> <span class="o">+=</span><span class="mi">1</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">keys</span><span class="p">[</span><span class="s">&quot;other&quot;</span><span class="p">]</span> <span class="o">+=</span><span class="mi">1</span>
        

    <span class="k">return</span> <span class="n">keys</span>


<span class="k">def</span> <span class="nf">process_map</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">     this function will return a dictionary with the unexpexted tag element as the key </span>
<span class="sd">     and number of times this string can be encountered in the map as value.</span>
<span class="sd">    Args:</span>
<span class="sd">        filename(osm): openstreetmap file.</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">keys</span> <span class="o">=</span> <span class="p">{</span><span class="s">&quot;lower&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s">&quot;lower_colon&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s">&quot;problemchars&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s">&quot;other&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">}</span>
    <span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">ET</span><span class="o">.</span><span class="n">iterparse</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
        <span class="n">keys</span> <span class="o">=</span> <span class="n">key_type</span><span class="p">(</span><span class="n">element</span><span class="p">,</span> <span class="n">keys</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">keys</span>

<span class="sd">&#39;&#39;&#39;</span>
<span class="sd">#Below unit testing runs process_map with file example.osm</span>
<span class="sd">def test():</span>
<span class="sd">    keys = process_map(&#39;example.osm&#39;)</span>
<span class="sd">    pprint.pprint(keys)</span>
<span class="sd">    assert keys == {&#39;lower&#39;: 5, &#39;lower_colon&#39;: 0, &#39;other&#39;: 1, &#39;problemchars&#39;: 1}</span>


<span class="sd">if __name__ == &quot;__main__&quot;:</span>
<span class="sd">    test()</span>

<span class="sd">&#39;&#39;&#39;</span>

<span class="n">keys</span> <span class="o">=</span> <span class="n">process_map</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span>
<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="n">keys</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>{&apos;lower&apos;: 749756, &apos;lower_colon&apos;: 56532, &apos;other&apos;: 40149, &apos;problemchars&apos;: 4}
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now I will redefine process_map to build a set of unique userid's found within the XML. I will then output the length of this set, representing the number of unique users making edits in the chosen map area.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">process_map</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">    This function will return a set of unique user IDs (&quot;uid&quot;) </span>
<span class="sd">    making edits in the chosen map area (i.e Boston area).</span>
<span class="sd">    Args:</span>
<span class="sd">        filename(osm): openstreetmap file.</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">users</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">ET</span><span class="o">.</span><span class="n">iterparse</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
        <span class="c">#print element.attrib</span>
        
        <span class="k">try</span><span class="p">:</span>
            <span class="n">users</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">element</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="s">&#39;uid&#39;</span><span class="p">])</span>
        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
            <span class="k">continue</span>
        <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">        if &quot;uid&quot; in element.attrib:</span>
<span class="sd">            users.add(element.attrib[&#39;uid&#39;])</span>
<span class="sd">        &#39;&#39;&#39;</span>
    <span class="k">return</span> <span class="n">users</span>

<span class="sd">&#39;&#39;&#39;</span>
<span class="sd">#Below unit testing runs process_map with file example.osm</span>
<span class="sd">def test():</span>

<span class="sd">    users = process_map(&#39;example.osm&#39;)</span>
<span class="sd">    pprint.pprint(users)</span>
<span class="sd">    assert len(users) == 6</span>

<span class="sd">if __name__ == &quot;__main__&quot;:</span>
<span class="sd">    test()</span>
<span class="sd">&#39;&#39;&#39;</span>

    
    
<span class="n">users</span> <span class="o">=</span> <span class="n">process_map</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span>
<span class="c">#pprint.pprint(users)</span>
<span class="k">print</span> <span class="nb">len</span><span class="p">(</span><span class="n">users</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>1016
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="3.-Problems-Encountered-in-the-Map">3. Problems Encountered in the Map<a class="anchor-link" href="#3.-Problems-Encountered-in-the-Map">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="3.1-Street-name">3.1 Street name<a class="anchor-link" href="#3.1-Street-name">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The majority of this project will be devoted to auditing and cleaning street names in the OSM XML file by changing the variable 'mapping' to reflect the changes needed to fix the unexpected or abbreviated street types to the appropriate ones in the expected list. I will find these abbreviations and replace them with their full text form.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">defaultdict</span>

<span class="n">street_type_re</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;\b\S+\.?$&#39;</span><span class="p">,</span> <span class="n">re</span><span class="o">.</span><span class="n">IGNORECASE</span><span class="p">)</span>


<span class="n">expected</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;Street&quot;</span><span class="p">,</span> <span class="s">&quot;Avenue&quot;</span><span class="p">,</span> <span class="s">&quot;Boulevard&quot;</span><span class="p">,</span> <span class="s">&quot;Drive&quot;</span><span class="p">,</span> <span class="s">&quot;Court&quot;</span><span class="p">,</span> <span class="s">&quot;Place&quot;</span><span class="p">,</span> <span class="s">&quot;Square&quot;</span><span class="p">,</span> <span class="s">&quot;Lane&quot;</span><span class="p">,</span> <span class="s">&quot;Road&quot;</span><span class="p">,</span> 
            <span class="s">&quot;Trail&quot;</span><span class="p">,</span> <span class="s">&quot;Parkway&quot;</span><span class="p">,</span> <span class="s">&quot;Commons&quot;</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">audit_street_type</span><span class="p">(</span><span class="n">street_types</span><span class="p">,</span> <span class="n">street_name</span><span class="p">,</span> <span class="n">rex</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">     This function will take in the dictionary of street types, a string of street name to audit, </span>
<span class="sd">     a regex to match against that string, and the list of expected street types.</span>
<span class="sd">     Args:</span>
<span class="sd">        street_types(dictionary): dictionary of street types.</span>
<span class="sd">        street_name(string):  a string of street name to audit.</span>
<span class="sd">        rex(regex): a compiled regular expression to match against the street_name.</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="c">#m = street_type_re.search(street_name)</span>
    <span class="n">m</span> <span class="o">=</span> <span class="n">rex</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">street_name</span><span class="p">)</span>
    <span class="c">#print m</span>
    <span class="c">#print m.group()</span>
    <span class="k">if</span> <span class="n">m</span><span class="p">:</span>
        <span class="n">street_type</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">street_type</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">expected</span><span class="p">:</span>
            <span class="n">street_types</span><span class="p">[</span><span class="n">street_type</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">street_name</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Let's define a function that not only audits tag elements where k="addr:street", but whichever tag elements match the is_street_name function. The audit function also takes in a regex and the list of expected matches</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">audit</span><span class="p">(</span><span class="n">osmfile</span><span class="p">,</span><span class="n">rex</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">     This function changes the variable &#39;mapping&#39; to reflect the changes needed to fix</span>
<span class="sd">    the unexpected street types to the appropriate ones in the expected list.</span>
<span class="sd">     Args:</span>
<span class="sd">        filename(osm): openstreetmap file.</span>
<span class="sd">        rex(regex): a compiled regular expression to match against the street_name.</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">osm_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">osmfile</span><span class="p">,</span> <span class="s">&quot;r&quot;</span><span class="p">)</span>
    <span class="n">street_types</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">set</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">event</span><span class="p">,</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">ET</span><span class="o">.</span><span class="n">iterparse</span><span class="p">(</span><span class="n">osm_file</span><span class="p">,</span> <span class="n">events</span><span class="o">=</span><span class="p">(</span><span class="s">&quot;start&quot;</span><span class="p">,)):</span>

        <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="s">&quot;node&quot;</span> <span class="ow">or</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="s">&quot;way&quot;</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">elem</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="s">&quot;tag&quot;</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">is_street_name</span><span class="p">(</span><span class="n">tag</span><span class="p">):</span>
                    <span class="n">audit_street_type</span><span class="p">(</span><span class="n">street_types</span><span class="p">,</span> <span class="n">tag</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="s">&#39;v&#39;</span><span class="p">],</span><span class="n">rex</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">street_types</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The function is_street_name determines if an element contains an attribute k="addr:street". I will use is_street_name as the tag filter when I call the audit function to audit street names.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">is_street_name</span><span class="p">(</span><span class="n">elem</span><span class="p">):</span>
    <span class="k">return</span> <span class="p">(</span><span class="n">elem</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="s">&#39;k&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;addr:street&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now print the output of audit</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">st_types</span> <span class="o">=</span> <span class="n">audit</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">rex</span> <span class="o">=</span> <span class="n">street_type_re</span><span class="p">)</span>
<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">dict</span><span class="p">(</span><span class="n">st_types</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>{&apos;1100&apos;: set([&apos;First Street, Suite 1100&apos;]),
 &apos;1702&apos;: set([&apos;Franklin Street, Suite 1702&apos;]),
 &apos;303&apos;: set([&apos;First Street, Suite 303&apos;]),
 &apos;6&apos;: set([&apos;South Station, near Track 6&apos;]),
 &apos;846028&apos;: set([&apos;PO Box 846028&apos;]),
 &apos;Artery&apos;: set([&apos;Southern Artery&apos;]),
 &apos;Ave&apos;: set([&apos;360 Huntington Ave&apos;,
             &apos;738 Commonwealth Ave&apos;,
             &apos;Blue Hill Ave&apos;,
             &apos;Boston Ave&apos;,
             &apos;College Ave&apos;,
             &apos;Commonwealth Ave&apos;,
             &apos;Concord Ave&apos;,
             &apos;Francesca Ave&apos;,
             &apos;Harrison Ave&apos;,
             &apos;Highland Ave&apos;,
             &apos;Huntington Ave&apos;,
             &apos;Josephine Ave&apos;,
             &apos;Lexington Ave&apos;,
             &apos;Massachusetts Ave&apos;,
             &apos;Morrison Ave&apos;,
             &apos;Mystic Ave&apos;,
             &apos;Sagamore Ave&apos;,
             &apos;Somerville Ave&apos;,
             &quot;St. Paul&apos;s Ave&quot;,
             &apos;Washington Ave&apos;,
             &apos;Western Ave&apos;,
             &apos;Willow Ave&apos;]),
 &apos;Ave.&apos;: set([&apos;Brighton Ave.&apos;,
              &apos;Huntington Ave.&apos;,
              &apos;Massachusetts Ave.&apos;,
              &apos;Somerville Ave.&apos;,
              &apos;Spaulding Ave.&apos;]),
 &apos;Boylston&apos;: set([&apos;Boylston&apos;]),
 &apos;Broadway&apos;: set([&apos;Broadway&apos;, &apos;West Broadway&apos;]),
 &apos;Brook&apos;: set([&apos;Furnace Brook&apos;]),
 &apos;Cambrdige&apos;: set([&apos;Cambrdige&apos;]),
 &apos;Center&apos;: set([&apos;Cambridge Center&apos;]),
 &apos;Circle&apos;: set([&apos;Edgewood Circle&apos;]),
 &apos;Corner&apos;: set([&apos;Webster Street, Coolidge Corner&apos;]),
 &apos;Ct&apos;: set([&apos;Kelley Ct&apos;]),
 &apos;Elm&apos;: set([&apos;Elm&apos;]),
 &apos;Federal&apos;: set([&apos;Federal&apos;]),
 &apos;Fellsway&apos;: set([&apos;Fellsway&apos;]),
 &apos;Fenway&apos;: set([&apos;Fenway&apos;]),
 &apos;Floor&apos;: set([&apos;Boylston Street, 5th Floor&apos;]),
 &apos;HIghway&apos;: set([&apos;American Legion HIghway&apos;]),
 &apos;Hall&apos;: set([&apos;Faneuil Hall&apos;]),
 &apos;Hampshire&apos;: set([&apos;Hampshire&apos;]),
 &apos;Highway&apos;: set([&apos;American Legion Highway&apos;,
                 &apos;Cummins Highway&apos;,
                 &quot;Monsignor O&apos;Brien Highway&quot;,
                 &apos;Providence Highway&apos;,
                 &apos;Santilli Highway&apos;]),
 &apos;Holland&apos;: set([&apos;Holland&apos;]),
 &apos;Hwy&apos;: set([&quot;Monsignor O&apos;Brien Hwy&quot;]),
 &apos;LEVEL&apos;: set([&apos;LOMASNEY WAY, ROOF LEVEL&apos;]),
 &apos;Lafayette&apos;: set([&apos;Avenue De Lafayette&apos;]),
 &apos;Mall&apos;: set([&apos;Cummington Mall&apos;]),
 &apos;Newbury&apos;: set([&apos;Newbury&apos;]),
 &apos;Park&apos;: set([&apos;Austin Park&apos;,
              &apos;Batterymarch Park&apos;,
              &apos;Canal Park&apos;,
              &apos;Exeter Park&apos;,
              &apos;Giles Park&apos;,
              &apos;Malden Street Park&apos;,
              &apos;Monument Park&apos;]),
 &apos;Pkwy&apos;: set([&apos;Birmingham Pkwy&apos;]),
 &apos;Pl&apos;: set([&apos;Longfellow Pl&apos;]),
 &apos;Rd&apos;: set([&apos;Abby Rd&apos;,
            &apos;Aberdeen Rd&apos;,
            &apos;Bristol Rd&apos;,
            &apos;Goodnough Rd&apos;,
            &apos;Oakland Rd&apos;,
            &apos;Soldiers Field Rd&apos;,
            &apos;Squanto Rd&apos;]),
 &apos;Row&apos;: set([&apos;Assembly Row&apos;, &apos;East India Row&apos;, &apos;Professors Row&apos;]),
 &apos;ST&apos;: set([&apos;Newton ST&apos;]),
 &apos;South&apos;: set([&apos;Charles Street South&apos;]),
 &apos;Sq.&apos;: set([&apos;1 Kendall Sq.&apos;]),
 &apos;St&apos;: set([&apos;1629 Cambridge St&apos;,
            &apos;644 Beacon St&apos;,
            &apos;Adams St&apos;,
            &apos;Antwerp St&apos;,
            &apos;Arsenal St&apos;,
            &apos;Athol St&apos;,
            &apos;Bagnal St&apos;,
            &apos;Beacon St&apos;,
            &apos;Brentwood St&apos;,
            &apos;Broad St&apos;,
            &apos;Cambridge St&apos;,
            &apos;Congress St&apos;,
            &apos;Court St&apos;,
            &apos;Cummington St&apos;,
            &apos;Dane St&apos;,
            &apos;Duval St&apos;,
            &apos;E 4th St&apos;,
            &apos;Elm St&apos;,
            &apos;Everett St&apos;,
            &apos;George St&apos;,
            &apos;Grove St&apos;,
            &apos;Hampshire St&apos;,
            &apos;Holton St&apos;,
            &apos;Kirkland St&apos;,
            &apos;Leighton St&apos;,
            &apos;Litchfield St&apos;,
            &apos;Lothrop St&apos;,
            &apos;Mackin St&apos;,
            &apos;Maverick St&apos;,
            &apos;Medford St&apos;,
            &apos;Merrill St&apos;,
            &apos;N Beacon St&apos;,
            &apos;Newbury St&apos;,
            &apos;Norfolk St&apos;,
            &apos;Portsmouth St&apos;,
            &apos;Richardson St&apos;,
            &apos;Salem St&apos;,
            &apos;Sea St&apos;,
            &apos;South Waverly St&apos;,
            &apos;Stewart St&apos;,
            &apos;Summer St&apos;,
            &apos;Ware St&apos;,
            &apos;Waverly St&apos;,
            &apos;Winter St&apos;]),
 &apos;St,&apos;: set([&apos;Walnut St,&apos;]),
 &apos;St.&apos;: set([&apos;Albion St.&apos;,
             &apos;Banks St.&apos;,
             &apos;Boylston St.&apos;,
             &apos;Brookline St.&apos;,
             &apos;Centre St.&apos;,
             &apos;Elm St.&apos;,
             &apos;Main St.&apos;,
             &apos;Marshall St.&apos;,
             &apos;Maverick St.&apos;,
             &apos;Pearl St.&apos;,
             &apos;Prospect St.&apos;,
             &quot;Saint Mary&apos;s St.&quot;,
             &apos;Stuart St.&apos;,
             &apos;Tremont St.&apos;]),
 &apos;Street.&apos;: set([&apos;Hancock Street.&apos;]),
 &apos;Terrace&apos;: set([&apos;Alberta Terrace&apos;, &apos;Norfolk Terrace&apos;, &apos;Westbourne Terrace&apos;]),
 &apos;Way&apos;: set([&apos;Artisan Way&apos;,
             &apos;Courthouse Way&apos;,
             &apos;David G Mugar Way&apos;,
             &apos;Davidson Way&apos;,
             &apos;Evans Way&apos;,
             &apos;Harry Agganis Way&apos;,
             &apos;Ross Way&apos;,
             &apos;Yawkey Way&apos;]),
 &apos;Wharf&apos;: set([&apos;Long Wharf&apos;, &apos;Rowes Wharf&apos;]),
 &apos;Windsor&apos;: set([&apos;Windsor&apos;]),
 &apos;Winsor&apos;: set([&apos;Winsor&apos;]),
 &apos;ave&apos;: set([&apos;Massachusetts ave&apos;]),
 &apos;floor&apos;: set([&apos;First Street, 18th floor&apos;, &apos;Sidney Street, 2nd floor&apos;]),
 &apos;place&apos;: set([&apos;argus place&apos;]),
 &apos;rd.&apos;: set([&apos;Corey rd.&apos;]),
 &apos;st&apos;: set([&apos;Church st&apos;]),
 &apos;street&apos;: set([&apos;Boston street&apos;])}
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>From the results of the audit, I will create a dictionary to map abbreviations to their full, clean representations.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="c"># UPDATE THIS VARIABLE</span>
<span class="n">mapping</span> <span class="o">=</span> <span class="p">{</span> <span class="s">&quot;ave&quot;</span> <span class="p">:</span> <span class="s">&quot;Avenue&quot;</span><span class="p">,</span>
            <span class="s">&quot;Ave&quot;</span> <span class="p">:</span> <span class="s">&quot;Avenue&quot;</span><span class="p">,</span>
            <span class="s">&quot;Ave.&quot;</span><span class="p">:</span> <span class="s">&quot;Avenue&quot;</span><span class="p">,</span>
            <span class="s">&quot;Ct&quot;</span> <span class="p">:</span> <span class="s">&quot;Court&quot;</span><span class="p">,</span>
            <span class="s">&quot;HIghway&quot;</span><span class="p">:</span> <span class="s">&quot;Highway&quot;</span><span class="p">,</span>
            <span class="s">&quot;Hwy&quot;</span><span class="p">:</span> <span class="s">&quot;Highway&quot;</span><span class="p">,</span>
            <span class="s">&quot;LEVEL&quot;</span><span class="p">:</span> <span class="s">&quot;Level&quot;</span><span class="p">,</span>
            <span class="s">&quot;Pkwy&quot;</span><span class="p">:</span> <span class="s">&quot;Parkway&quot;</span><span class="p">,</span>
            <span class="s">&quot;Pl&quot;</span><span class="p">:</span> <span class="s">&quot;Place&quot;</span><span class="p">,</span>
            <span class="s">&quot;rd.&quot;</span> <span class="p">:</span> <span class="s">&quot;Road&quot;</span><span class="p">,</span>
            <span class="s">&quot;Rd&quot;</span> <span class="p">:</span> <span class="s">&quot;Road&quot;</span><span class="p">,</span>
            <span class="s">&quot;Rd.&quot;</span> <span class="p">:</span> <span class="s">&quot;Road&quot;</span><span class="p">,</span>
            <span class="s">&quot;Sq.&quot;</span> <span class="p">:</span> <span class="s">&quot;Square&quot;</span><span class="p">,</span> 
            <span class="s">&quot;st&quot;</span><span class="p">:</span> <span class="s">&quot;Street&quot;</span><span class="p">,</span>
            <span class="s">&quot;St&quot;</span><span class="p">:</span> <span class="s">&quot;Street&quot;</span><span class="p">,</span>
            <span class="s">&quot;St.&quot;</span><span class="p">:</span> <span class="s">&quot;Street&quot;</span><span class="p">,</span>
            <span class="s">&quot;St,&quot;</span><span class="p">:</span> <span class="s">&quot;Street&quot;</span><span class="p">,</span> 
            <span class="s">&quot;ST&quot;</span><span class="p">:</span> <span class="s">&quot;Street&quot;</span><span class="p">,</span>
            <span class="s">&quot;Street.&quot;</span> <span class="p">:</span> <span class="s">&quot;Street&quot;</span><span class="p">,</span>               
            <span class="p">}</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The first result of audit gives me a list of some abbreviated street types (as well as unexpected clean street types, cardinal directions, and highway numbers). So I need to build an update_name function to replace these abbreviated street types.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">update_name</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">mapping</span><span class="p">,</span><span class="n">rex</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">     This function takes a string with street name as an argument </span>
<span class="sd">     and replace these abbreviated street types with the fixed name.</span>
<span class="sd">     Args:</span>
<span class="sd">        name(string): street name to update.</span>
<span class="sd">        mapping(dictionary): a mapping dictionary.</span>
<span class="sd">        rex(regex): a compiled regular expression to match against the street_name.</span>
<span class="sd">    &#39;&#39;&#39;</span>

    <span class="c">#m = street_type_re.search(name)</span>
    <span class="n">m</span> <span class="o">=</span> <span class="n">rex</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">m</span><span class="p">:</span>
        <span class="n">street_type</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">()</span>
        <span class="n">new_street_type</span> <span class="o">=</span> <span class="n">mapping</span><span class="p">[</span><span class="n">street_type</span><span class="p">]</span>
        <span class="n">name</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">rex</span><span class="p">,</span> <span class="n">new_street_type</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span> <span class="c"># re.sub(old_pattern, new_pattern, file)</span>
        <span class="c">#name = street_type_re.sub(new_street_type, name)</span>
    <span class="k">return</span> <span class="n">name</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Let's see how this update_name works.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">for</span> <span class="n">st_type</span><span class="p">,</span> <span class="n">ways</span> <span class="ow">in</span> <span class="n">st_types</span><span class="o">.</span><span class="n">iteritems</span><span class="p">():</span>
    <span class="k">if</span> <span class="n">st_type</span> <span class="ow">in</span> <span class="n">mapping</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">ways</span><span class="p">:</span>
            <span class="n">better_name</span> <span class="o">=</span> <span class="n">update_name</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">mapping</span><span class="p">,</span> <span class="n">rex</span> <span class="o">=</span> <span class="n">street_type_re</span><span class="p">)</span>
            <span class="k">print</span> <span class="n">name</span><span class="p">,</span> <span class="s">&quot;=&gt;&quot;</span><span class="p">,</span> <span class="n">better_name</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Walnut St, =&gt; Walnut Street
Maverick St. =&gt; Maverick Street
Pearl St. =&gt; Pearl Street
Banks St. =&gt; Banks Street
Tremont St. =&gt; Tremont Street
Centre St. =&gt; Centre Street
Marshall St. =&gt; Marshall Street
Prospect St. =&gt; Prospect Street
Main St. =&gt; Main Street
Albion St. =&gt; Albion Street
Saint Mary&apos;s St. =&gt; Saint Mary&apos;s Street
Boylston St. =&gt; Boylston Street
Stuart St. =&gt; Stuart Street
Elm St. =&gt; Elm Street
Brookline St. =&gt; Brookline Street
Oakland Rd =&gt; Oakland Road
Abby Rd =&gt; Abby Road
Bristol Rd =&gt; Bristol Road
Squanto Rd =&gt; Squanto Road
Goodnough Rd =&gt; Goodnough Road
Soldiers Field Rd =&gt; Soldiers Field Road
Aberdeen Rd =&gt; Aberdeen Road
Massachusetts ave =&gt; Massachusetts Avenue
Newton ST =&gt; Newton Street
Longfellow Pl =&gt; Longfellow Place
Hancock Street. =&gt; Hancock Street
Monsignor O&apos;Brien Hwy =&gt; Monsignor O&apos;Brien Highway
Corey rd. =&gt; Corey Road
Brighton Ave. =&gt; Brighton Avenue
Spaulding Ave. =&gt; Spaulding Avenue
Massachusetts Ave. =&gt; Massachusetts Avenue
Somerville Ave. =&gt; Somerville Avenue
Huntington Ave. =&gt; Huntington Avenue
LOMASNEY WAY, ROOF LEVEL =&gt; LOMASNEY WAY, ROOF Level
Salem St =&gt; Salem Street
Brentwood St =&gt; Brentwood Street
Medford St =&gt; Medford Street
Athol St =&gt; Athol Street
Everett St =&gt; Everett Street
South Waverly St =&gt; South Waverly Street
Litchfield St =&gt; Litchfield Street
Hampshire St =&gt; Hampshire Street
George St =&gt; George Street
Winter St =&gt; Winter Street
Broad St =&gt; Broad Street
Cambridge St =&gt; Cambridge Street
Arsenal St =&gt; Arsenal Street
Merrill St =&gt; Merrill Street
Maverick St =&gt; Maverick Street
Antwerp St =&gt; Antwerp Street
Beacon St =&gt; Beacon Street
1629 Cambridge St =&gt; 1629 Cambridge Street
E 4th St =&gt; E 4th Street
Elm St =&gt; Elm Street
Congress St =&gt; Congress Street
Lothrop St =&gt; Lothrop Street
Stewart St =&gt; Stewart Street
Dane St =&gt; Dane Street
Norfolk St =&gt; Norfolk Street
Bagnal St =&gt; Bagnal Street
Cummington St =&gt; Cummington Street
Holton St =&gt; Holton Street
Mackin St =&gt; Mackin Street
Waverly St =&gt; Waverly Street
Court St =&gt; Court Street
Summer St =&gt; Summer Street
Duval St =&gt; Duval Street
Kirkland St =&gt; Kirkland Street
Adams St =&gt; Adams Street
644 Beacon St =&gt; 644 Beacon Street
N Beacon St =&gt; N Beacon Street
Grove St =&gt; Grove Street
Leighton St =&gt; Leighton Street
Richardson St =&gt; Richardson Street
Newbury St =&gt; Newbury Street
Sea St =&gt; Sea Street
Ware St =&gt; Ware Street
Portsmouth St =&gt; Portsmouth Street
Massachusetts Ave =&gt; Massachusetts Avenue
Highland Ave =&gt; Highland Avenue
Lexington Ave =&gt; Lexington Avenue
Huntington Ave =&gt; Huntington Avenue
Francesca Ave =&gt; Francesca Avenue
Willow Ave =&gt; Willow Avenue
360 Huntington Ave =&gt; 360 Huntington Avenue
Harrison Ave =&gt; Harrison Avenue
Somerville Ave =&gt; Somerville Avenue
Mystic Ave =&gt; Mystic Avenue
Blue Hill Ave =&gt; Blue Hill Avenue
Washington Ave =&gt; Washington Avenue
Morrison Ave =&gt; Morrison Avenue
Boston Ave =&gt; Boston Avenue
738 Commonwealth Ave =&gt; 738 Commonwealth Avenue
Josephine Ave =&gt; Josephine Avenue
Sagamore Ave =&gt; Sagamore Avenue
Commonwealth Ave =&gt; Commonwealth Avenue
St. Paul&apos;s Ave =&gt; St. Paul&apos;s Avenue
Concord Ave =&gt; Concord Avenue
Western Ave =&gt; Western Avenue
College Ave =&gt; College Avenue
Birmingham Pkwy =&gt; Birmingham Parkway
Church st =&gt; Church Street
1 Kendall Sq. =&gt; 1 Kendall Square
American Legion HIghway =&gt; American Legion Highway
Kelley Ct =&gt; Kelley Court
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>It seems that all the abbreviated street types updated as expected.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="3.2-Cardinal-direction">3.2 Cardinal direction<a class="anchor-link" href="#3.2-Cardinal-direction">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>But I can see there is still an issue: cardinal directions (North, South, East, and West) appear to be universally abbreviated.  Therefore , I will traverse the cardinal_directions dictionary and apply the updates for both street type and cardinal direction</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">cardinal_dir_re</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^[NSEW]\b\.?&#39;</span><span class="p">,</span> <span class="n">re</span><span class="o">.</span><span class="n">IGNORECASE</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Here is the result of audit the cardinal directions with this new regex 'cardinal_dir_re'</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">dir_st_types</span> <span class="o">=</span> <span class="n">audit</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">rex</span> <span class="o">=</span> <span class="n">cardinal_dir_re</span><span class="p">)</span>
<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">dict</span><span class="p">(</span><span class="n">dir_st_types</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>{&apos;E&apos;: set([&apos;E 4th St&apos;, &apos;E Elm Avenue&apos;]), &apos;N&apos;: set([&apos;N Beacon St&apos;])}
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I will create a dictionary to map abbreviations (N, S, E and W) to their full representations of cardinal directions.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">cardinal_directions_mapping</span> <span class="o">=</span> \
    <span class="p">{</span>
        <span class="s">&quot;E&quot;</span> <span class="p">:</span> <span class="s">&quot;East&quot;</span><span class="p">,</span>
        <span class="s">&quot;N&quot;</span> <span class="p">:</span> <span class="s">&quot;North&quot;</span><span class="p">,</span>
        <span class="s">&quot;S&quot;</span> <span class="p">:</span> <span class="s">&quot;South&quot;</span><span class="p">,</span>
        <span class="s">&quot;W&quot;</span> <span class="p">:</span> <span class="s">&quot;West&quot;</span>
    <span class="p">}</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Look like all expected cardinal directions have been replaced.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">for</span> <span class="n">st_type</span><span class="p">,</span> <span class="n">ways</span> <span class="ow">in</span> <span class="n">dir_st_types</span><span class="o">.</span><span class="n">iteritems</span><span class="p">():</span>
    <span class="k">if</span> <span class="n">st_type</span> <span class="ow">in</span> <span class="n">cardinal_directions_mapping</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">ways</span><span class="p">:</span>
            <span class="n">better_name</span> <span class="o">=</span> <span class="n">update_name</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">cardinal_directions_mapping</span><span class="p">,</span> <span class="n">rex</span> <span class="o">=</span> <span class="n">cardinal_dir_re</span><span class="p">)</span>
            <span class="k">print</span> <span class="n">name</span><span class="p">,</span> <span class="s">&quot;=&gt;&quot;</span><span class="p">,</span> <span class="n">better_name</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>E Elm Avenue =&gt; East Elm Avenue
E 4th St =&gt; East 4th St
N Beacon St =&gt; North Beacon St
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="3.3-Postal-codes">3.3 Postal codes<a class="anchor-link" href="#3.3-Postal-codes">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Let's exam the postal codes, we can see that there are still some invalid postal codes, so we also need to clean postal codes. I will use regular expressions to identify invalid postal codes and return standardized results. For example, if postal codes like 'MA 02131-4931' and '02131-2460' should be mapped to '02131'.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">badZipCode</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;MA&quot;</span><span class="p">,</span> <span class="s">&quot;Mass Ave&quot;</span><span class="p">]</span>


<span class="n">zip_code_re</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&quot;(\d{5})(-\d{4})?$&quot;</span><span class="p">)</span> <span class="c">#5 digits in a row @ end of string</span>
                                           <span class="c">#and optionally dash plus 4 digits</span>
                                           <span class="c">#return different parts of the match and an optional clause (?) </span>
                                           <span class="c">#for the dash and four digits at the end of the string ($)</span>

<span class="c"># find the zipcodes</span>
<span class="k">def</span> <span class="nf">get_postcode</span><span class="p">(</span><span class="n">element</span><span class="p">):</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">element</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="s">&#39;k&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;addr:postcode&quot;</span><span class="p">):</span>
        <span class="n">postcode</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="s">&#39;v&#39;</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">postcode</span>

    
<span class="c"># update zipcodes</span>
<span class="k">def</span> <span class="nf">update_postal</span><span class="p">(</span><span class="n">postcode</span><span class="p">,</span> <span class="n">rex</span><span class="p">):</span>
     <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">     This function takes a string with zip code as an argument </span>
<span class="sd">     and replace these wrong zip code with the fixed zip code.</span>
<span class="sd">     Args:</span>
<span class="sd">        postcode(string): zip code to update.</span>
<span class="sd">        rex(regex): a compiled regular expression to match against the zip code.</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="k">if</span> <span class="n">postcode</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">zip_code</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">rex</span><span class="p">,</span><span class="n">postcode</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">zip_code</span><span class="p">:</span>
            <span class="n">postcode</span> <span class="o">=</span> <span class="n">zip_code</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
                   
    <span class="k">return</span> <span class="n">postcode</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">audit</span><span class="p">(</span><span class="n">osmfile</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">     This function return a dictionary with the key is the zip code </span>
<span class="sd">     and the value is the number of that zip code in osm file.</span>
<span class="sd">     Args:</span>
<span class="sd">        filename(osm): openstreetmap file.</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">osm_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">osmfile</span><span class="p">,</span> <span class="s">&quot;r&quot;</span><span class="p">)</span>
    <span class="n">data_dict</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">event</span><span class="p">,</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">ET</span><span class="o">.</span><span class="n">iterparse</span><span class="p">(</span><span class="n">osm_file</span><span class="p">,</span> <span class="n">events</span><span class="o">=</span><span class="p">(</span><span class="s">&quot;start&quot;</span><span class="p">,)):</span>
        
        <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="s">&quot;node&quot;</span> <span class="ow">or</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="s">&quot;way&quot;</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">elem</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="s">&quot;tag&quot;</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">get_postcode</span><span class="p">(</span><span class="n">tag</span><span class="p">):</span>
                    <span class="n">postcode</span> <span class="o">=</span> <span class="n">get_postcode</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
                    <span class="n">data_dict</span><span class="p">[</span><span class="n">postcode</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span> 
    <span class="k">return</span> <span class="n">data_dict</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">zip_code_types</span> <span class="o">=</span> <span class="n">audit</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span>
<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">dict</span><span class="p">(</span><span class="n">zip_code_types</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>{&apos; 02472&apos;: 1,
 &apos;01125&apos;: 1,
 &apos;01238&apos;: 1,
 &apos;01240&apos;: 1,
 &apos;01250&apos;: 1,
 &apos;01821&apos;: 1,
 &apos;01944&apos;: 1,
 &apos;02026&apos;: 1,
 &apos;02026-5036&apos;: 1,
 &apos;02043&apos;: 3,
 &apos;02108&apos;: 11,
 &apos;02109&apos;: 8,
 &apos;02110&apos;: 7,
 &apos;02110-1301&apos;: 1,
 &apos;02111&apos;: 16,
 &apos;02113&apos;: 1,
 &apos;02114&apos;: 58,
 &apos;02114-3203&apos;: 1,
 &apos;02115&apos;: 9,
 &apos;02116&apos;: 41,
 &apos;02118&apos;: 5,
 &apos;02119&apos;: 1,
 &apos;02120&apos;: 3,
 &apos;02121&apos;: 2,
 &apos;02122&apos;: 6,
 &apos;02124&apos;: 8,
 &apos;02125&apos;: 5,
 &apos;02126&apos;: 7,
 &apos;02127&apos;: 11,
 &apos;02128&apos;: 22,
 &apos;02129&apos;: 2,
 &apos;02130&apos;: 43,
 &apos;02130-4803&apos;: 1,
 &apos;02131&apos;: 8,
 &apos;02131-3025&apos;: 2,
 &apos;02131-4931&apos;: 1,
 &apos;02132&apos;: 17,
 &apos;02132-1239&apos;: 1,
 &apos;02132-3226&apos;: 1,
 &apos;02134&apos;: 48,
 &apos;02134-1305&apos;: 9,
 &apos;02134-1306&apos;: 2,
 &apos;02134-1307&apos;: 29,
 &apos;02134-1311&apos;: 4,
 &apos;02134-1312&apos;: 2,
 &apos;02134-1313&apos;: 4,
 &apos;02134-1316&apos;: 3,
 &apos;02134-1317&apos;: 4,
 &apos;02134-1318&apos;: 2,
 &apos;02134-1319&apos;: 5,
 &apos;02134-1321&apos;: 4,
 &apos;02134-1322&apos;: 4,
 &apos;02134-1327&apos;: 1,
 &apos;02134-1409&apos;: 4,
 &apos;02134-1420&apos;: 9,
 &apos;02134-1433&apos;: 11,
 &apos;02134-1442&apos;: 5,
 &apos;02135&apos;: 249,
 &apos;02136&apos;: 6,
 &apos;02136-2460&apos;: 1,
 &apos;02138&apos;: 49,
 &apos;02138-1901&apos;: 1,
 &apos;02138-2701&apos;: 8,
 &apos;02138-2706&apos;: 3,
 &apos;02138-2724&apos;: 1,
 &apos;02138-2735&apos;: 1,
 &apos;02138-2736&apos;: 2,
 &apos;02138-2742&apos;: 1,
 &apos;02138-2762&apos;: 1,
 &apos;02138-2763&apos;: 1,
 &apos;02138-2801&apos;: 4,
 &apos;02138-2901&apos;: 4,
 &apos;02138-2903&apos;: 8,
 &apos;02138-2933&apos;: 3,
 &apos;02138-3003&apos;: 1,
 &apos;02138-3824&apos;: 1,
 &apos;02139&apos;: 227,
 &apos;02140&apos;: 14,
 &apos;02140-1340&apos;: 1,
 &apos;02140-2215&apos;: 1,
 &apos;02141&apos;: 16,
 &apos;02142&apos;: 31,
 &apos;02143&apos;: 50,
 &apos;02144&apos;: 89,
 &apos;02145&apos;: 18,
 &apos;02148&apos;: 1,
 &apos;02149&apos;: 15,
 &apos;02150&apos;: 8,
 &apos;02151&apos;: 4,
 &apos;02152&apos;: 2,
 &apos;02155&apos;: 22,
 &apos;02159&apos;: 1,
 &apos;02169&apos;: 52,
 &apos;02170&apos;: 3,
 &apos;02171&apos;: 5,
 &apos;02174&apos;: 1,
 &apos;02184&apos;: 3,
 &apos;02186&apos;: 8,
 &apos;02205&apos;: 1,
 &apos;02210&apos;: 26,
 &apos;02215&apos;: 59,
 &apos;02228&apos;: 1,
 &apos;02284-6028&apos;: 1,
 &apos;02445&apos;: 11,
 &apos;02445-5841&apos;: 1,
 &apos;02446&apos;: 36,
 &apos;02458&apos;: 4,
 &apos;02459&apos;: 5,
 &apos;02467&apos;: 23,
 &apos;02472&apos;: 29,
 &apos;02474&apos;: 21,
 &apos;02474-8735&apos;: 1,
 &apos;02476&apos;: 8,
 &apos;02478&apos;: 9,
 &apos;MA&apos;: 6,
 &apos;MA 02116&apos;: 4,
 &apos;MA 02186&apos;: 1,
 &apos;Mass Ave&apos;: 1}
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">for</span> <span class="n">raw_zip_code</span> <span class="ow">in</span> <span class="n">zip_code_types</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">raw_zip_code</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">badZipCode</span><span class="p">:</span>
        <span class="n">better_zip_code</span> <span class="o">=</span> <span class="n">update_postal</span><span class="p">(</span><span class="n">raw_zip_code</span><span class="p">,</span> <span class="n">rex</span> <span class="o">=</span> <span class="n">zip_code_re</span><span class="p">)</span>
        <span class="k">print</span> <span class="n">raw_zip_code</span><span class="p">,</span> <span class="s">&quot;=&gt;&quot;</span><span class="p">,</span> <span class="n">better_zip_code</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>02186 =&gt; 02186
02184 =&gt; 02184
02134-1327 =&gt; 02134
02130 =&gt; 02130
02134-1322 =&gt; 02134
02134-1321 =&gt; 02134
02138-1901 =&gt; 02138
02132-3226 =&gt; 02132
01821 =&gt; 01821
02134-1433 =&gt; 02134
02108 =&gt; 02108
02026 =&gt; 02026
02476 =&gt; 02476
02474 =&gt; 02474
02472 =&gt; 02472
02139 =&gt; 02139
02134-1319 =&gt; 02134
02478 =&gt; 02478
02136-2460 =&gt; 02136
02131-3025 =&gt; 02131
02136 =&gt; 02136
02140-1340 =&gt; 02140
02134 =&gt; 02134
02205 =&gt; 02205
02132 =&gt; 02132
02131 =&gt; 02131
 02472 =&gt; 02472
02110-1301 =&gt; 02110
02138 =&gt; 02138
02138-2903 =&gt; 02138
02138-2901 =&gt; 02138
02134-1442 =&gt; 02134
01250 =&gt; 01250
02132-1239 =&gt; 02132
02446 =&gt; 02446
02445 =&gt; 02445
02138-2742 =&gt; 02138
02120 =&gt; 02120
02121 =&gt; 02121
02210 =&gt; 02210
02124 =&gt; 02124
02125 =&gt; 02125
02126 =&gt; 02126
02215 =&gt; 02215
02128 =&gt; 02128
02129 =&gt; 02129
02474-8735 =&gt; 02474
01240 =&gt; 01240
02114-3203 =&gt; 02114
02458 =&gt; 02458
02459 =&gt; 02459
MA 02116 =&gt; 02116
01125 =&gt; 01125
02109 =&gt; 02109
02228 =&gt; 02228
MA 02186 =&gt; 02186
02155 =&gt; 02155
02151 =&gt; 02151
02150 =&gt; 02150
02152 =&gt; 02152
02159 =&gt; 02159
02026-5036 =&gt; 02026
01238 =&gt; 01238
02138-2724 =&gt; 02138
02445-5841 =&gt; 02445
02138-2933 =&gt; 02138
02144 =&gt; 02144
02145 =&gt; 02145
02142 =&gt; 02142
02143 =&gt; 02143
02140 =&gt; 02140
02141 =&gt; 02141
02148 =&gt; 02148
02149 =&gt; 02149
02138-2735 =&gt; 02138
02138-2736 =&gt; 02138
02131-4931 =&gt; 02131
02138-3824 =&gt; 02138
02134-1316 =&gt; 02134
02134-1317 =&gt; 02134
02134-1312 =&gt; 02134
02134-1313 =&gt; 02134
02134-1311 =&gt; 02134
02134-1318 =&gt; 02134
01944 =&gt; 01944
02171 =&gt; 02171
02134-1409 =&gt; 02134
02174 =&gt; 02174
02170 =&gt; 02170
02122 =&gt; 02122
02138-2706 =&gt; 02138
02138-2701 =&gt; 02138
02140-2215 =&gt; 02140
02134-1420 =&gt; 02134
02127 =&gt; 02127
02114 =&gt; 02114
02134-1305 =&gt; 02134
02134-1307 =&gt; 02134
02134-1306 =&gt; 02134
02043 =&gt; 02043
02169 =&gt; 02169
02130-4803 =&gt; 02130
02138-2801 =&gt; 02138
02284-6028 =&gt; 02284
02119 =&gt; 02119
02118 =&gt; 02118
02138-3003 =&gt; 02138
02111 =&gt; 02111
02110 =&gt; 02110
02113 =&gt; 02113
02115 =&gt; 02115
02135 =&gt; 02135
02116 =&gt; 02116
02467 =&gt; 02467
02138-2762 =&gt; 02138
02138-2763 =&gt; 02138
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre> 
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="3.4-The-total-number-of-nodes-and-ways">3.4 The total number of nodes and ways<a class="anchor-link" href="#3.4-The-total-number-of-nodes-and-ways">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Then I will count the total number of nodes and ways that contain a tag child with k="addr:street"</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">osm_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s">&quot;r&quot;</span><span class="p">)</span>
<span class="n">address_count</span> <span class="o">=</span> <span class="mi">0</span>

<span class="k">for</span> <span class="n">event</span><span class="p">,</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">ET</span><span class="o">.</span><span class="n">iterparse</span><span class="p">(</span><span class="n">osm_file</span><span class="p">,</span> <span class="n">events</span><span class="o">=</span><span class="p">(</span><span class="s">&quot;start&quot;</span><span class="p">,)):</span>
    <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="s">&quot;node&quot;</span> <span class="ow">or</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="s">&quot;way&quot;</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">elem</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="s">&quot;tag&quot;</span><span class="p">):</span> 
            <span class="k">if</span> <span class="n">is_street_name</span><span class="p">(</span><span class="n">tag</span><span class="p">):</span>
                <span class="n">address_count</span> <span class="o">+=</span> <span class="mi">1</span>

<span class="n">address_count</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[30]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>2976</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="4.-Preparing-for-MongoDB">4. Preparing for MongoDB<a class="anchor-link" href="#4.-Preparing-for-MongoDB">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Before importing the XML data into MongoDB, I have to transform the shape of data into json documents structured (a list of dictionaries) like this</p>

</div>
</div>
</div>{
"id": "2406124091",
"type: "node",
"visible":"true",
"created": {         
          "version":"2",          
          "changeset":"17206049",
          "timestamp":"2013-08-03T16:43:42Z",          
          "user":"linuxUser16",          
          "uid":"1219059"        
        },
"pos": [41.9757030, -87.6921867],
"address": {
          "housenumber": "5157",
          "postcode": "60625",
          "street": "North Lincoln Ave"        
        },
"amenity": "restaurant",
"cuisine": "mexican",
"name": "La Cabana De Don Luis",
"phone": "1 (773)-271-5176"
}
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Here are the rules:</p>
<ul>
<li>process only 2 types of top level tags: "node" and "way"</li>
<li>all attributes of "node" and "way" should be turned into regular key/value pairs, except:<ul>
<li>attributes in the CREATED array should be added under a key "created"</li>
<li>attributes for latitude and longitude should be added to a "pos" array,
for use in geospacial indexing. Make sure the values inside "pos" array are floats
and not strings.</li>
</ul>
</li>
<li>if second level tag "k" value contains problematic characters, it should be ignored</li>
<li>if second level tag "k" value starts with "addr:", it should be added to a dictionary "address"</li>
<li>if second level tag "k" value does not start with "addr:", but contains ":", you can process it
same as any other tag.</li>
<li>if there is a second ":" that separates the type/direction of a street,
the tag should be ignored, for example:</li>
</ul>

</div>
</div>
</div><tag k="addr:housenumber" v="5158"/>
<tag k="addr:street" v="North Lincoln Avenue"/>
<tag k="addr:street:name" v="Lincoln"/>
<tag k="addr:street:prefix" v="North"/>
<tag k="addr:street:type" v="Avenue"/>
<tag k="amenity" v="pharmacy"/>
  should be turned into:
{...
"address": {    
    "housenumber": 5158,
    "street": "North Lincoln Avenue"
}
"amenity": "pharmacy",
...
}
- for "way" specifically:
  <nd ref="305896090"/>  
  <nd ref="1719825889"/>should be turned into# "node_refs": ["305896090", "1719825889"]
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">CREATED</span> <span class="o">=</span> <span class="p">[</span> <span class="s">&quot;version&quot;</span><span class="p">,</span> <span class="s">&quot;changeset&quot;</span><span class="p">,</span> <span class="s">&quot;timestamp&quot;</span><span class="p">,</span> <span class="s">&quot;user&quot;</span><span class="p">,</span> <span class="s">&quot;uid&quot;</span><span class="p">]</span>

<span class="k">def</span> <span class="nf">shape_element</span><span class="p">(</span><span class="n">element</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">     This function will parse the map file and return a dictionary, </span>
<span class="sd">     containing the shaped data for that element.</span>
<span class="sd">     Args:</span>
<span class="sd">        element(string): element in the map.</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">node</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="c"># create an address dictionary</span>
    <span class="n">address</span> <span class="o">=</span> <span class="p">{}</span>
    
    <span class="k">if</span> <span class="n">element</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="s">&quot;node&quot;</span> <span class="ow">or</span> <span class="n">element</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="s">&quot;way&quot;</span> <span class="p">:</span>
        <span class="c"># YOUR CODE HERE</span>
        <span class="n">node</span><span class="p">[</span><span class="s">&quot;type&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">tag</span>

        <span class="c">#for key in element.attrib.keys()</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">element</span><span class="o">.</span><span class="n">attrib</span><span class="p">:</span>
            <span class="c">#print key</span>

            <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">CREATED</span><span class="p">:</span>
                <span class="k">if</span> <span class="s">&quot;created&quot;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">node</span><span class="p">:</span>
                    <span class="n">node</span><span class="p">[</span><span class="s">&quot;created&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
                <span class="n">node</span><span class="p">[</span><span class="s">&quot;created&quot;</span><span class="p">][</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>

            <span class="k">elif</span> <span class="n">key</span> <span class="ow">in</span> <span class="p">[</span><span class="s">&quot;lat&quot;</span><span class="p">,</span><span class="s">&quot;lon&quot;</span><span class="p">]:</span>
                <span class="k">if</span> <span class="s">&quot;pos&quot;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">node</span><span class="p">:</span>
                    <span class="n">node</span><span class="p">[</span><span class="s">&quot;pos&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">]</span>
                <span class="k">if</span> <span class="n">key</span> <span class="o">==</span> <span class="s">&quot;lat&quot;</span><span class="p">:</span>
                    <span class="n">node</span><span class="p">[</span><span class="s">&quot;pos&quot;</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="n">element</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="n">key</span><span class="p">])</span>
                <span class="k">elif</span> <span class="n">key</span> <span class="o">==</span> <span class="s">&quot;lon&quot;</span><span class="p">:</span>
                    <span class="n">node</span><span class="p">[</span><span class="s">&quot;pos&quot;</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="n">element</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="n">key</span><span class="p">])</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">node</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>

            <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">element</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="s">&quot;tag&quot;</span><span class="p">):</span>
                <span class="n">tag_key</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="s">&quot;k&quot;</span><span class="p">]</span>   <span class="c"># key</span>
                <span class="n">tag_value</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="s">&quot;v&quot;</span><span class="p">]</span> <span class="c"># value</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">problemchars</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">tag_key</span><span class="p">):</span>
                    <span class="k">if</span> <span class="n">tag_key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&quot;addr:&quot;</span><span class="p">):</span><span class="c"># Single colon beginning with addr</span>
                        <span class="k">if</span> <span class="s">&quot;address&quot;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">node</span><span class="p">:</span>
                            <span class="n">node</span><span class="p">[</span><span class="s">&quot;address&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
                        <span class="n">sub_addr</span> <span class="o">=</span> <span class="n">tag_key</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="s">&quot;addr:&quot;</span><span class="p">):]</span>
                        <span class="k">if</span> <span class="ow">not</span> <span class="n">lower_colon</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">sub_addr</span><span class="p">):</span> <span class="c"># Tags with no colon</span>
                            <span class="n">address</span><span class="p">[</span><span class="n">sub_addr</span><span class="p">]</span> <span class="o">=</span> <span class="n">tag_value</span> 
                            <span class="n">node</span><span class="p">[</span><span class="s">&quot;address&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">address</span>
                            <span class="c">#node[&quot;address&quot;][sub_addr] = tag_value</span>
                    <span class="k">elif</span> <span class="n">lower_colon</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">tag_key</span><span class="p">):</span> <span class="c"># Single colon not beginnning with &quot;addr:&quot;</span>
                        <span class="n">node</span><span class="p">[</span><span class="n">tag_key</span><span class="p">]</span> <span class="o">=</span> <span class="n">tag_value</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="n">node</span><span class="p">[</span><span class="n">tag_key</span><span class="p">]</span> <span class="o">=</span> <span class="n">tag_value</span> <span class="c"># Tags with no colon, not beginnning with &quot;addr:&quot;</span>

        <span class="k">for</span> <span class="n">nd</span> <span class="ow">in</span> <span class="n">element</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="s">&quot;nd&quot;</span><span class="p">):</span>
            <span class="k">if</span> <span class="s">&quot;node_refs&quot;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">node</span><span class="p">:</span>
                <span class="n">node</span><span class="p">[</span><span class="s">&quot;node_refs&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">node</span><span class="p">[</span><span class="s">&quot;node_refs&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">nd</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="s">&quot;ref&quot;</span><span class="p">])</span>

        <span class="k">return</span> <span class="n">node</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">None</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>It's time to parse the XML, shape the elements, and write to a json file</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">import</span> <span class="nn">codecs</span>
<span class="kn">import</span> <span class="nn">json</span>

<span class="k">def</span> <span class="nf">process_map</span><span class="p">(</span><span class="n">file_in</span><span class="p">,</span> <span class="n">pretty</span> <span class="o">=</span> <span class="bp">False</span><span class="p">):</span>
    <span class="c"># You do not need to change this file</span>
    <span class="n">file_out</span> <span class="o">=</span> <span class="s">&quot;{0}.json&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">file_in</span><span class="p">)</span>
    <span class="n">data</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">with</span> <span class="n">codecs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file_out</span><span class="p">,</span> <span class="s">&quot;w&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fo</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">ET</span><span class="o">.</span><span class="n">iterparse</span><span class="p">(</span><span class="n">file_in</span><span class="p">):</span>
            <span class="n">el</span> <span class="o">=</span> <span class="n">shape_element</span><span class="p">(</span><span class="n">element</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">el</span><span class="p">:</span>
                <span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">el</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">pretty</span><span class="p">:</span>
                    <span class="n">fo</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">el</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span><span class="o">+</span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">fo</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">el</span><span class="p">)</span> <span class="o">+</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">data</span>

<span class="n">process_map</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[32]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>[{&apos;created&apos;: {&apos;changeset&apos;: &apos;244358&apos;,
   &apos;timestamp&apos;: &apos;2007-03-24T19:38:02Z&apos;,
   &apos;uid&apos;: &apos;6817&apos;,
   &apos;user&apos;: &apos;lurker&apos;,
   &apos;version&apos;: &apos;1&apos;},
  &apos;created_by&apos;: &apos;YahooApplet 1.0&apos;,
  &apos;id&apos;: &apos;26746680&apos;,
  &apos;pos&apos;: [42.3089253, -71.1191797],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;30730952&apos;,
  &apos;pos&apos;: [42.3678097, -71.0218711],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;30730953&apos;,
  &apos;pos&apos;: [42.3677364, -71.0218568],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;30730954&apos;,
  &apos;pos&apos;: [42.3676084, -71.0218168],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;30730955&apos;,
  &apos;pos&apos;: [42.3675229, -71.0218486],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;30730956&apos;,
  &apos;pos&apos;: [42.3674548, -71.0218865],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;30730957&apos;,
  &apos;pos&apos;: [42.3666762, -71.0225905],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;30730958&apos;,
  &apos;pos&apos;: [42.3666294, -71.0226837],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;30730959&apos;,
  &apos;pos&apos;: [42.3666032, -71.0227675],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;30730960&apos;,
  &apos;pos&apos;: [42.3665745, -71.0228874],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;30730961&apos;,
  &apos;pos&apos;: [42.3665821, -71.0232172],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;30730962&apos;,
  &apos;pos&apos;: [42.3666858, -71.0236541],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;30730963&apos;,
  &apos;pos&apos;: [42.3667051, -71.023767],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;30730964&apos;,
  &apos;pos&apos;: [42.3667095, -71.0239758],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:24:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;30730965&apos;,
  &apos;pos&apos;: [42.3666947, -71.0242345],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;106539&apos;,
   &apos;timestamp&apos;: &apos;2007-06-21T09:47:59Z&apos;,
   &apos;uid&apos;: &apos;8609&apos;,
   &apos;user&apos;: &apos;ewedistrict&apos;,
   &apos;version&apos;: &apos;1&apos;},
  &apos;id&apos;: &apos;30730967&apos;,
  &apos;pos&apos;: [42.3665527, -71.0217637],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;14335103&apos;,
   &apos;timestamp&apos;: &apos;2012-12-19T19:38:28Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;30730968&apos;,
  &apos;pos&apos;: [42.3668798, -71.0224961],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;106539&apos;,
   &apos;timestamp&apos;: &apos;2007-06-21T10:01:26Z&apos;,
   &apos;uid&apos;: &apos;8609&apos;,
   &apos;user&apos;: &apos;ewedistrict&apos;,
   &apos;version&apos;: &apos;1&apos;},
  &apos;id&apos;: &apos;30731113&apos;,
  &apos;pos&apos;: [42.3733949, -71.0366467],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;106539&apos;,
   &apos;timestamp&apos;: &apos;2007-06-21T10:01:26Z&apos;,
   &apos;uid&apos;: &apos;8609&apos;,
   &apos;user&apos;: &apos;ewedistrict&apos;,
   &apos;version&apos;: &apos;1&apos;},
  &apos;id&apos;: &apos;30731114&apos;,
  &apos;pos&apos;: [42.3738832, -71.0363034],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;106539&apos;,
   &apos;timestamp&apos;: &apos;2007-06-21T10:03:22Z&apos;,
   &apos;uid&apos;: &apos;8609&apos;,
   &apos;user&apos;: &apos;ewedistrict&apos;,
   &apos;version&apos;: &apos;1&apos;},
  &apos;id&apos;: &apos;30731163&apos;,
  &apos;pos&apos;: [42.3749547, -71.0386809],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;106539&apos;,
   &apos;timestamp&apos;: &apos;2007-06-21T10:03:52Z&apos;,
   &apos;uid&apos;: &apos;8609&apos;,
   &apos;user&apos;: &apos;ewedistrict&apos;,
   &apos;version&apos;: &apos;1&apos;},
  &apos;id&apos;: &apos;30731166&apos;,
  &apos;pos&apos;: [42.3767999, -71.0337886],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;106539&apos;,
   &apos;timestamp&apos;: &apos;2007-06-21T10:06:54Z&apos;,
   &apos;uid&apos;: &apos;8609&apos;,
   &apos;user&apos;: &apos;ewedistrict&apos;,
   &apos;version&apos;: &apos;1&apos;},
  &apos;id&apos;: &apos;30731185&apos;,
  &apos;pos&apos;: [42.3746631, -71.0390586],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;106539&apos;,
   &apos;timestamp&apos;: &apos;2007-06-21T10:06:54Z&apos;,
   &apos;uid&apos;: &apos;8609&apos;,
   &apos;user&apos;: &apos;ewedistrict&apos;,
   &apos;version&apos;: &apos;1&apos;},
  &apos;id&apos;: &apos;30731186&apos;,
  &apos;pos&apos;: [42.3756649, -71.0390843],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;106539&apos;,
   &apos;timestamp&apos;: &apos;2007-06-21T10:06:54Z&apos;,
   &apos;uid&apos;: &apos;8609&apos;,
   &apos;user&apos;: &apos;ewedistrict&apos;,
   &apos;version&apos;: &apos;1&apos;},
  &apos;id&apos;: &apos;30731187&apos;,
  &apos;pos&apos;: [42.3788605, -71.039153],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;106539&apos;,
   &apos;timestamp&apos;: &apos;2007-06-21T10:06:54Z&apos;,
   &apos;uid&apos;: &apos;8609&apos;,
   &apos;user&apos;: &apos;ewedistrict&apos;,
   &apos;version&apos;: &apos;1&apos;},
  &apos;id&apos;: &apos;30731188&apos;,
  &apos;pos&apos;: [42.3813205, -71.039256],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:12:33Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;31004512&apos;,
  &apos;pos&apos;: [42.3742782, -71.0178919],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:14:09Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;31004513&apos;,
  &apos;pos&apos;: [42.3585891, -70.9968697],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:12:59Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;31004514&apos;,
  &apos;pos&apos;: [42.3546443, -70.9915848],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:10:02Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;31004515&apos;,
  &apos;pos&apos;: [42.3557464, -71.0128869],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:09:41Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;31004516&apos;,
  &apos;pos&apos;: [42.3602139, -70.987701],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;142410&apos;,
   &apos;timestamp&apos;: &apos;2008-06-12T17:52:34Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;31004517&apos;,
  &apos;pos&apos;: [42.376899, -70.9992944],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:14:10Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;id&apos;: &apos;31004519&apos;,
  &apos;pos&apos;: [42.356399, -71.009208],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:10:32Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;31004520&apos;,
  &apos;pos&apos;: [42.3510507, -71.0117953],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:14:08Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;31004522&apos;,
  &apos;pos&apos;: [42.3647756, -71.0051586],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:12:14Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;31004523&apos;,
  &apos;pos&apos;: [42.3782965, -71.004497],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:14:19Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;31004526&apos;,
  &apos;pos&apos;: [42.3680064, -71.0094871],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:11:55Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;31004527&apos;,
  &apos;pos&apos;: [42.3735767, -71.0091131],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:14:19Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;9&apos;},
  &apos;id&apos;: &apos;31004528&apos;,
  &apos;pos&apos;: [42.3723021, -71.007404],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:14:01Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;id&apos;: &apos;31004529&apos;,
  &apos;pos&apos;: [42.3690784, -71.0030778],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7376100&apos;,
   &apos;timestamp&apos;: &apos;2011-02-23T20:11:39Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;31004530&apos;,
  &apos;pos&apos;: [42.3686049, -71.0024424],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;amenity&apos;: &apos;restaurant&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;14796087&apos;,
   &apos;timestamp&apos;: &apos;2013-01-26T18:21:38Z&apos;,
   &apos;uid&apos;: &apos;492311&apos;,
   &apos;user&apos;: &apos;zacmccormick&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;31419556&apos;,
  &apos;name&apos;: &apos;Firebrand Saints&apos;,
  &apos;pos&apos;: [42.3624181, -71.0831048],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;17674245&apos;,
   &apos;timestamp&apos;: &apos;2013-09-04T20:18:50Z&apos;,
   &apos;uid&apos;: &apos;165061&apos;,
   &apos;user&apos;: &apos;mapper999&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;description&apos;: &apos;Outbound only&apos;,
  &apos;id&apos;: &apos;31419650&apos;,
  &apos;name&apos;: &apos;Kendall/MIT&apos;,
  &apos;pos&apos;: [42.3627266, -71.0861289],
  &apos;railway&apos;: &apos;subway_entrance&apos;,
  &apos;type&apos;: &apos;node&apos;,
  &apos;url&apos;: &apos;http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=12412&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;131807&apos;,
   &apos;timestamp&apos;: &apos;2007-07-07T20:27:40Z&apos;,
   &apos;uid&apos;: &apos;7906&apos;,
   &apos;user&apos;: &apos;ravn&apos;,
   &apos;version&apos;: &apos;1&apos;},
  &apos;id&apos;: &apos;31419991&apos;,
  &apos;pos&apos;: [42.3708042, -71.0787171],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2453875&apos;,
   &apos;timestamp&apos;: &apos;2009-09-12T06:32:06Z&apos;,
   &apos;uid&apos;: &apos;58305&apos;,
   &apos;user&apos;: &apos;fiveisalive&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;36303521&apos;,
  &apos;name&apos;: &apos;Central Street Historical District&apos;,
  &apos;pos&apos;: [42.4173849, -71.1562276],
  &apos;tourism&apos;: &apos;attraction&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10589104&apos;,
   &apos;timestamp&apos;: &apos;2012-02-04T22:15:24Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;60656559&apos;,
  &apos;pos&apos;: [42.3455107, -71.0981581],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7217269&apos;,
   &apos;timestamp&apos;: &apos;2011-02-07T15:31:28Z&apos;,
   &apos;uid&apos;: &apos;116029&apos;,
   &apos;user&apos;: &apos;Gregory Arenius&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;60656560&apos;,
  &apos;pos&apos;: [42.3467934, -71.0988177],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7217269&apos;,
   &apos;timestamp&apos;: &apos;2011-02-07T15:31:28Z&apos;,
   &apos;uid&apos;: &apos;116029&apos;,
   &apos;user&apos;: &apos;Gregory Arenius&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;60656561&apos;,
  &apos;pos&apos;: [42.3470832, -71.0984901],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;13588000&apos;,
   &apos;timestamp&apos;: &apos;2012-10-22T04:01:21Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61151272&apos;,
  &apos;pos&apos;: [42.3822063, -71.0939042],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;6702541&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:22:27Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61151274&apos;,
  &apos;pos&apos;: [42.3818108, -71.0933165],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;485479&apos;,
   &apos;timestamp&apos;: &apos;2009-02-16T14:28:11Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;created_by&apos;: &apos;JOSM&apos;,
  &apos;id&apos;: &apos;61152567&apos;,
  &apos;pos&apos;: [42.399444, -71.111436],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;485479&apos;,
   &apos;timestamp&apos;: &apos;2009-02-16T14:28:11Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;created_by&apos;: &apos;JOSM&apos;,
  &apos;id&apos;: &apos;61152568&apos;,
  &apos;pos&apos;: [42.399344, -71.111519],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T22:20:36Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61155415&apos;,
  &apos;pos&apos;: [42.3929603, -71.0886976],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;6702541&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:22:28Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61155686&apos;,
  &apos;pos&apos;: [42.38172, -71.0932382],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;2681685&apos;,
   &apos;timestamp&apos;: &apos;2009-09-29T21:24:31Z&apos;,
   &apos;uid&apos;: &apos;166129&apos;,
   &apos;user&apos;: &apos;BugBuster&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61155739&apos;,
  &apos;pos&apos;: [42.380787, -71.091453],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;13669201&apos;,
   &apos;timestamp&apos;: &apos;2012-10-29T02:19:29Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61155740&apos;,
  &apos;pos&apos;: [42.3807355, -71.0916541],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;2681685&apos;,
   &apos;timestamp&apos;: &apos;2009-09-29T21:24:31Z&apos;,
   &apos;uid&apos;: &apos;166129&apos;,
   &apos;user&apos;: &apos;BugBuster&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61155741&apos;,
  &apos;pos&apos;: [42.380724, -71.091895],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;13669201&apos;,
   &apos;timestamp&apos;: &apos;2012-10-29T02:19:29Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61155742&apos;,
  &apos;pos&apos;: [42.3807741, -71.0921738],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;2681685&apos;,
   &apos;timestamp&apos;: &apos;2009-09-29T21:24:30Z&apos;,
   &apos;uid&apos;: &apos;166129&apos;,
   &apos;user&apos;: &apos;BugBuster&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61155746&apos;,
  &apos;pos&apos;: [42.380902, -71.091146],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;13669201&apos;,
   &apos;timestamp&apos;: &apos;2012-10-29T02:19:29Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61155753&apos;,
  &apos;pos&apos;: [42.3809194, -71.0924575],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;13669201&apos;,
   &apos;timestamp&apos;: &apos;2012-10-29T02:19:29Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61155754&apos;,
  &apos;pos&apos;: [42.3811514, -71.0927115],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008124914&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:37:55Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170312&apos;,
  &apos;pos&apos;: [42.3870595, -71.0921853],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:37:55Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170313&apos;,
  &apos;pos&apos;: [42.387159, -71.0924876],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6692003&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T23:41:24Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170320&apos;,
  &apos;pos&apos;: [42.3870508, -71.0814075],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845410&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T00:30:53Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170342&apos;,
  &apos;pos&apos;: [42.3872153, -71.116705],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:09Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;9&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170349&apos;,
  &apos;pos&apos;: [42.3879485, -71.1154222],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12143236&apos;,
   &apos;timestamp&apos;: &apos;2012-07-07T19:19:18Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170350&apos;,
  &apos;pos&apos;: [42.3956994, -71.1204735],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12336041&apos;,
   &apos;timestamp&apos;: &apos;2012-07-19T15:42:17Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170351&apos;,
  &apos;pos&apos;: [42.3955178, -71.120579],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:50:55Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170353&apos;,
  &apos;pos&apos;: [42.3946953, -71.121425],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:02Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170355&apos;,
  &apos;pos&apos;: [42.39519, -71.102708],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:03Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170357&apos;,
  &apos;pos&apos;: [42.394691, -71.102278],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:05:06Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170363&apos;,
  &apos;pos&apos;: [42.396319, -71.101152],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:07:49Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170380&apos;,
  &apos;pos&apos;: [42.3948105, -71.1136831],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:04:16Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170385&apos;,
  &apos;pos&apos;: [42.394908, -71.122503],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:04:17Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170387&apos;,
  &apos;pos&apos;: [42.395333, -71.121863],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6749853&apos;,
   &apos;timestamp&apos;: &apos;2010-12-23T21:22:31Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61170393&apos;,
  &apos;pos&apos;: [42.3949515, -71.0881886],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170395&apos;,
  &apos;pos&apos;: [42.3948947, -71.1186097],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170397&apos;,
  &apos;pos&apos;: [42.3938475, -71.1161927],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;21189633&apos;,
   &apos;timestamp&apos;: &apos;2014-03-19T10:38:21Z&apos;,
   &apos;uid&apos;: &apos;1670311&apos;,
   &apos;user&apos;: &apos;SophoM&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170398&apos;,
  &apos;pos&apos;: [42.3941212, -71.1168213],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31954058&apos;,
   &apos;timestamp&apos;: &apos;2015-06-14T02:20:30Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170401&apos;,
  &apos;pos&apos;: [42.3926201, -71.0830303],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61170420&apos;,
  &apos;pos&apos;: [42.3932827, -71.1148882],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12384518&apos;,
   &apos;timestamp&apos;: &apos;2012-07-20T17:00:57Z&apos;,
   &apos;uid&apos;: &apos;81285&apos;,
   &apos;user&apos;: &apos;Ahlzen&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;id&apos;: &apos;61170424&apos;,
  &apos;pos&apos;: [42.3927891, -71.1151463],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6993315&apos;,
   &apos;timestamp&apos;: &apos;2011-01-16T20:25:32Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170428&apos;,
  &apos;pos&apos;: [42.393559, -71.1171955],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26242801&apos;,
   &apos;timestamp&apos;: &apos;2014-10-21T20:54:49Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170429&apos;,
  &apos;pos&apos;: [42.392878, -71.117653],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6993326&apos;,
   &apos;timestamp&apos;: &apos;2011-01-16T20:26:50Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170430&apos;,
  &apos;pos&apos;: [42.3932289, -71.117422],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:13Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170431&apos;,
  &apos;pos&apos;: [42.39281, -71.098301],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2255197&apos;,
   &apos;timestamp&apos;: &apos;2009-08-25T12:30:01Z&apos;,
   &apos;uid&apos;: &apos;38786&apos;,
   &apos;user&apos;: &apos;Ian McIntosh&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170432&apos;,
  &apos;pos&apos;: [42.3931514, -71.1183167],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170444&apos;,
  &apos;pos&apos;: [42.3929011, -71.1140032],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:14Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170447&apos;,
  &apos;pos&apos;: [42.3941, -71.101838],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:50:55Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170457&apos;,
  &apos;pos&apos;: [42.3936838, -71.1196536],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170470&apos;,
  &apos;pos&apos;: [42.3935716, -71.1155532],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:04:33Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170472&apos;,
  &apos;pos&apos;: [42.393652, -71.124372],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;29539707&apos;,
   &apos;timestamp&apos;: &apos;2015-03-17T12:56:02Z&apos;,
   &apos;uid&apos;: &apos;2655992&apos;,
   &apos;user&apos;: &apos;steverumizen&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170474&apos;,
  &apos;pos&apos;: [42.394072, -71.120619],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:50:54Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170514&apos;,
  &apos;pos&apos;: [42.3909083, -71.1183141],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:22Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170518&apos;,
  &apos;pos&apos;: [42.393791, -71.097546],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26242801&apos;,
   &apos;timestamp&apos;: &apos;2014-10-21T20:54:49Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170519&apos;,
  &apos;pos&apos;: [42.3938254, -71.120884],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:50:53Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170521&apos;,
  &apos;pos&apos;: [42.3945747, -71.1213471],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;568005&apos;,
   &apos;timestamp&apos;: &apos;2009-02-19T17:42:04Z&apos;,
   &apos;uid&apos;: &apos;100884&apos;,
   &apos;user&apos;: &apos;jkw&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170531&apos;,
  &apos;pos&apos;: [42.391839, -71.115738],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:04:41Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170533&apos;,
  &apos;pos&apos;: [42.392154, -71.116339],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26584106&apos;,
   &apos;timestamp&apos;: &apos;2014-11-06T01:47:54Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170539&apos;,
  &apos;pos&apos;: [42.391321, -71.099405],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:30Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170540&apos;,
  &apos;pos&apos;: [42.39114, -71.099216],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:30Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170541&apos;,
  &apos;pos&apos;: [42.390889, -71.098957],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:04:42Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170542&apos;,
  &apos;pos&apos;: [42.392498, -71.116959],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170544&apos;,
  &apos;pos&apos;: [42.3918661, -71.1116462],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:07:59Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170546&apos;,
  &apos;pos&apos;: [42.39111, -71.112165],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:32Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170551&apos;,
  &apos;pos&apos;: [42.392585, -71.099472],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:33Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170552&apos;,
  &apos;pos&apos;: [42.392958, -71.099205],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:33Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170553&apos;,
  &apos;pos&apos;: [42.391894, -71.099999],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26584106&apos;,
   &apos;timestamp&apos;: &apos;2014-11-06T01:47:54Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170554&apos;,
  &apos;pos&apos;: [42.392478, -71.100573],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:51:02Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170557&apos;,
  &apos;pos&apos;: [42.391868, -71.1193798],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6993326&apos;,
   &apos;timestamp&apos;: &apos;2011-01-16T20:26:50Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;9&apos;},
  &apos;id&apos;: &apos;61170560&apos;,
  &apos;pos&apos;: [42.3923054, -71.1154388],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;9&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170562&apos;,
  &apos;pos&apos;: [42.3922111, -71.1124076],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:50:55Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170563&apos;,
  &apos;pos&apos;: [42.3923228, -71.1198002],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;19072675&apos;,
   &apos;timestamp&apos;: &apos;2013-11-23T14:45:07Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170583&apos;,
  &apos;pos&apos;: [42.3905789, -71.0862116],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6020841&apos;,
   &apos;timestamp&apos;: &apos;2010-10-12T13:22:27Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170585&apos;,
  &apos;pos&apos;: [42.3898947, -71.1111464],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6690197&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T20:07:11Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170590&apos;,
  &apos;pos&apos;: [42.3894273, -71.0874024],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170593&apos;,
  &apos;pos&apos;: [42.3912169, -71.110202],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170594&apos;,
  &apos;pos&apos;: [42.390863, -71.1094169],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170595&apos;,
  &apos;pos&apos;: [42.3925362, -71.1131596],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:38Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170596&apos;,
  &apos;pos&apos;: [42.392441, -71.098557],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:39Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170597&apos;,
  &apos;pos&apos;: [42.392005, -71.097381],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3079621&apos;,
   &apos;timestamp&apos;: &apos;2009-11-10T03:07:48Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170615&apos;,
  &apos;pos&apos;: [42.391048, -71.098047],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170617&apos;,
  &apos;pos&apos;: [42.3899023, -71.1072794],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170618&apos;,
  &apos;pos&apos;: [42.3896838, -71.1067968],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:23Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170621&apos;,
  &apos;pos&apos;: [42.390421, -71.098482],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6020841&apos;,
   &apos;timestamp&apos;: &apos;2010-10-12T13:22:27Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170622&apos;,
  &apos;pos&apos;: [42.3895934, -71.1113563],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:08:07Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170625&apos;,
  &apos;pos&apos;: [42.390862, -71.114179],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T02:55:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170633&apos;,
  &apos;pos&apos;: [42.3907729, -71.0902257],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6020841&apos;,
   &apos;timestamp&apos;: &apos;2010-10-12T13:22:13Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170638&apos;,
  &apos;pos&apos;: [42.391414, -71.114983],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:29Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170643&apos;,
  &apos;pos&apos;: [42.386209, -71.096878],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;29392974&apos;,
   &apos;timestamp&apos;: &apos;2015-03-10T20:49:06Z&apos;,
   &apos;uid&apos;: &apos;2655992&apos;,
   &apos;user&apos;: &apos;steverumizen&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170644&apos;,
  &apos;pos&apos;: [42.386532, -71.097825],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:12Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170649&apos;,
  &apos;pos&apos;: [42.390473, -71.11362],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:31Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170657&apos;,
  &apos;pos&apos;: [42.390491, -71.100021],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:41Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170658&apos;,
  &apos;pos&apos;: [42.390821, -71.099773],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:06Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170660&apos;,
  &apos;pos&apos;: [42.3915271, -71.1108948],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:50:55Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170665&apos;,
  &apos;pos&apos;: [42.3870439, -71.1146338],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:14:41Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170669&apos;,
  &apos;pos&apos;: [42.387948, -71.105953],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:14:42Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170671&apos;,
  &apos;pos&apos;: [42.387367, -71.106361],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6020841&apos;,
   &apos;timestamp&apos;: &apos;2010-10-12T13:22:27Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170673&apos;,
  &apos;pos&apos;: [42.3873841, -71.1128956],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:37:52Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170675&apos;,
  &apos;pos&apos;: [42.386065, -71.082369],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6020841&apos;,
   &apos;timestamp&apos;: &apos;2010-10-12T13:22:27Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170676&apos;,
  &apos;pos&apos;: [42.3877899, -71.1126128],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:29:44Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170679&apos;,
  &apos;pos&apos;: [42.385036, -71.085723],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11109635&apos;,
   &apos;timestamp&apos;: &apos;2012-03-26T19:28:56Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170691&apos;,
  &apos;pos&apos;: [42.3862333, -71.0830039],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:37:55Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170692&apos;,
  &apos;pos&apos;: [42.386705, -71.08267],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:37:55Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170701&apos;,
  &apos;pos&apos;: [42.3870031, -71.0919983],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26242718&apos;,
   &apos;timestamp&apos;: &apos;2014-10-21T20:50:31Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170707&apos;,
  &apos;pos&apos;: [42.3860407, -71.1051039],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12181505&apos;,
   &apos;timestamp&apos;: &apos;2012-07-11T03:53:01Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170722&apos;,
  &apos;pos&apos;: [42.3857576, -71.104319],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12181505&apos;,
   &apos;timestamp&apos;: &apos;2012-07-11T03:53:01Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170732&apos;,
  &apos;pos&apos;: [42.3855242, -71.1036605],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:11:26Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170738&apos;,
  &apos;pos&apos;: [42.385428, -71.115206],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12181505&apos;,
   &apos;timestamp&apos;: &apos;2012-07-11T03:53:01Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170751&apos;,
  &apos;pos&apos;: [42.3850792, -71.1023937],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:29:48Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170761&apos;,
  &apos;pos&apos;: [42.384944, -71.085432],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12181505&apos;,
   &apos;timestamp&apos;: &apos;2012-07-11T03:53:01Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170766&apos;,
  &apos;pos&apos;: [42.3852926, -71.103001],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:38:06Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170769&apos;,
  &apos;pos&apos;: [42.385445, -71.087035],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702541&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:22:28Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170799&apos;,
  &apos;pos&apos;: [42.385892, -71.0960613],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:24:23Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170802&apos;,
  &apos;pos&apos;: [42.383621, -71.102723],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;5013636&apos;,
   &apos;timestamp&apos;: &apos;2010-06-18T03:23:40Z&apos;,
   &apos;uid&apos;: &apos;23351&apos;,
   &apos;user&apos;: &apos;JasonWoof&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61170816&apos;,
  &apos;pos&apos;: [42.3834141, -71.1021055],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:14:39Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170835&apos;,
  &apos;pos&apos;: [42.384196, -71.113665],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:14:40Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170837&apos;,
  &apos;pos&apos;: [42.383724, -71.113076],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;1806622&apos;,
   &apos;timestamp&apos;: &apos;2009-07-12T13:32:34Z&apos;,
   &apos;uid&apos;: &apos;60604&apos;,
   &apos;user&apos;: &apos;cmurtaugh&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170845&apos;,
  &apos;pos&apos;: [42.3839335, -71.1035751],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:50:55Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;id&apos;: &apos;61170875&apos;,
  &apos;pos&apos;: [42.3860922, -71.1138132],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702541&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:22:28Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170881&apos;,
  &apos;pos&apos;: [42.38468, -71.0926581],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702541&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:22:28Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170882&apos;,
  &apos;pos&apos;: [42.3848506, -71.0927809],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:41Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170885&apos;,
  &apos;pos&apos;: [42.385513, -71.093458],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:29:50Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170890&apos;,
  &apos;pos&apos;: [42.384563, -71.084212],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:29:54Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170906&apos;,
  &apos;pos&apos;: [42.384867, -71.082164],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:29:55Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170907&apos;,
  &apos;pos&apos;: [42.384524, -71.08241],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:29:56Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170908&apos;,
  &apos;pos&apos;: [42.384143, -71.082681],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12135181&apos;,
   &apos;timestamp&apos;: &apos;2012-07-06T21:44:57Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170914&apos;,
  &apos;pos&apos;: [42.3819517, -71.0980999],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12181505&apos;,
   &apos;timestamp&apos;: &apos;2012-07-11T03:53:01Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170915&apos;,
  &apos;pos&apos;: [42.3822043, -71.0983316],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7681591&apos;,
   &apos;timestamp&apos;: &apos;2011-03-27T01:22:25Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170916&apos;,
  &apos;pos&apos;: [42.3819704, -71.0819487],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:29:58Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170924&apos;,
  &apos;pos&apos;: [42.381777, -71.083072],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:29:59Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170925&apos;,
  &apos;pos&apos;: [42.382435, -71.083119],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:29:59Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170926&apos;,
  &apos;pos&apos;: [42.382897, -71.083144],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:30:00Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170927&apos;,
  &apos;pos&apos;: [42.383247, -71.083134],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:30:01Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170928&apos;,
  &apos;pos&apos;: [42.383544, -71.083083],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:30:02Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170930&apos;,
  &apos;pos&apos;: [42.383828, -71.082899],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7681514&apos;,
   &apos;timestamp&apos;: &apos;2011-03-27T00:53:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170931&apos;,
  &apos;pos&apos;: [42.3819025, -71.0823551],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2386443&apos;,
   &apos;timestamp&apos;: &apos;2009-09-06T02:40:21Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170932&apos;,
  &apos;pos&apos;: [42.3834, -71.113587],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:14:50Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170944&apos;,
  &apos;pos&apos;: [42.384565, -71.114123],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702541&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:22:28Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170946&apos;,
  &apos;pos&apos;: [42.3848835, -71.0935001],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;19073633&apos;,
   &apos;timestamp&apos;: &apos;2013-11-23T15:39:54Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170948&apos;,
  &apos;pos&apos;: [42.3845473, -71.092648],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:24:44Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170949&apos;,
  &apos;pos&apos;: [42.384659, -71.092918],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7141091&apos;,
   &apos;timestamp&apos;: &apos;2011-01-30T23:30:05Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170954&apos;,
  &apos;pos&apos;: [42.3833653, -71.1126369],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12181505&apos;,
   &apos;timestamp&apos;: &apos;2012-07-11T03:53:01Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170956&apos;,
  &apos;pos&apos;: [42.3832651, -71.099342],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7141091&apos;,
   &apos;timestamp&apos;: &apos;2011-01-30T23:30:04Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170957&apos;,
  &apos;pos&apos;: [42.3831822, -71.1124126],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12181505&apos;,
   &apos;timestamp&apos;: &apos;2012-07-11T03:53:01Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170960&apos;,
  &apos;pos&apos;: [42.3829836, -71.099075],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32171768&apos;,
   &apos;timestamp&apos;: &apos;2015-06-23T23:25:33Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170975&apos;,
  &apos;pos&apos;: [42.3820397, -71.0815273],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6642755&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T22:14:59Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170986&apos;,
  &apos;pos&apos;: [42.3800943, -71.1044896],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6642755&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T22:15:22Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170988&apos;,
  &apos;pos&apos;: [42.3804136, -71.1045977],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:24:54Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61170993&apos;,
  &apos;pos&apos;: [42.380487, -71.097739],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632151&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T03:33:32Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170994&apos;,
  &apos;pos&apos;: [42.379366, -71.1001239],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;457421&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T17:26:02Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170995&apos;,
  &apos;pos&apos;: [42.37869, -71.096112],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;457421&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T17:26:02Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61170996&apos;,
  &apos;pos&apos;: [42.379108, -71.096231],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3369091&apos;,
   &apos;timestamp&apos;: &apos;2009-12-14T02:52:32Z&apos;,
   &apos;uid&apos;: &apos;175058&apos;,
   &apos;user&apos;: &apos;Tom Walsh&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;crossing&apos;: &apos;traffic_signals&apos;,
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61170997&apos;,
  &apos;pos&apos;: [42.379635, -71.096387],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6670798&apos;,
   &apos;timestamp&apos;: &apos;2010-12-15T19:41:05Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61170998&apos;,
  &apos;pos&apos;: [42.3795466, -71.0972533],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:52:39Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171011&apos;,
  &apos;pos&apos;: [42.3836734, -71.086913],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:24:59Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171032&apos;,
  &apos;pos&apos;: [42.380829, -71.098585],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:24:59Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171035&apos;,
  &apos;pos&apos;: [42.380557, -71.097904],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632518&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T06:19:22Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61171038&apos;,
  &apos;pos&apos;: [42.3751057, -71.1024965],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632518&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T06:18:56Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171042&apos;,
  &apos;pos&apos;: [42.3756286, -71.1017267],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12899968&apos;,
   &apos;timestamp&apos;: &apos;2012-08-29T02:16:01Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171059&apos;,
  &apos;pos&apos;: [42.3772848, -71.0892675],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6591204&apos;,
   &apos;timestamp&apos;: &apos;2010-12-09T00:28:26Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171064&apos;,
  &apos;pos&apos;: [42.3757368, -71.1015773],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632151&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T03:34:05Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171065&apos;,
  &apos;pos&apos;: [42.3765482, -71.0994382],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:25:00Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171070&apos;,
  &apos;pos&apos;: [42.380308, -71.097315],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;27238329&apos;,
   &apos;timestamp&apos;: &apos;2014-12-04T16:14:44Z&apos;,
   &apos;uid&apos;: &apos;2462466&apos;,
   &apos;user&apos;: &apos;EvanMula&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171071&apos;,
  &apos;pos&apos;: [42.380179, -71.096995],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:15:01Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171075&apos;,
  &apos;pos&apos;: [42.380496, -71.109095],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6932046&apos;,
   &apos;timestamp&apos;: &apos;2011-01-10T22:27:02Z&apos;,
   &apos;uid&apos;: &apos;23351&apos;,
   &apos;user&apos;: &apos;JasonWoof&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171088&apos;,
  &apos;pos&apos;: [42.3810566, -71.0991637],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:15:08Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171091&apos;,
  &apos;pos&apos;: [42.380889, -71.109572],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6932046&apos;,
   &apos;timestamp&apos;: &apos;2011-01-10T22:27:02Z&apos;,
   &apos;uid&apos;: &apos;23351&apos;,
   &apos;user&apos;: &apos;JasonWoof&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61171094&apos;,
  &apos;pos&apos;: [42.3812437, -71.0998043],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;19922728&apos;,
   &apos;timestamp&apos;: &apos;2014-01-10T18:51:04Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61171106&apos;,
  &apos;pos&apos;: [42.3786335, -71.1048178],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13435407&apos;,
   &apos;timestamp&apos;: &apos;2012-10-10T02:03:51Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171110&apos;,
  &apos;pos&apos;: [42.378536, -71.092589],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;19922728&apos;,
   &apos;timestamp&apos;: &apos;2014-01-10T18:51:04Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;crossing&apos;: &apos;traffic_signals&apos;,
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171112&apos;,
  &apos;name&apos;: &apos;SP4 Daniel J. Ryan Square&apos;,
  &apos;pos&apos;: [42.3788395, -71.1040534],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6008358&apos;,
   &apos;timestamp&apos;: &apos;2010-10-11T03:57:18Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171113&apos;,
  &apos;pos&apos;: [42.3787184, -71.0930989],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;29539707&apos;,
   &apos;timestamp&apos;: &apos;2015-03-17T12:56:02Z&apos;,
   &apos;uid&apos;: &apos;2655992&apos;,
   &apos;user&apos;: &apos;steverumizen&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171114&apos;,
  &apos;pos&apos;: [42.3872989, -71.082264],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:44Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171117&apos;,
  &apos;pos&apos;: [42.3749507, -71.0894318],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:44Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171118&apos;,
  &apos;pos&apos;: [42.375697, -71.0892782],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6692003&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T23:41:24Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171121&apos;,
  &apos;pos&apos;: [42.387124, -71.0816694],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T01:58:30Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61171122&apos;,
  &apos;pos&apos;: [42.3866839, -71.0801502],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845410&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T00:30:53Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;id&apos;: &apos;61171135&apos;,
  &apos;pos&apos;: [42.3866507, -71.1156992],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845410&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T00:30:53Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171136&apos;,
  &apos;pos&apos;: [42.386904, -71.1161581],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26584106&apos;,
   &apos;timestamp&apos;: &apos;2014-11-06T01:47:54Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171138&apos;,
  &apos;name&apos;: &apos;Magoun Square&apos;,
  &apos;pos&apos;: [42.397361, -71.104396],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2273850&apos;,
   &apos;timestamp&apos;: &apos;2009-08-27T05:16:54Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171139&apos;,
  &apos;pos&apos;: [42.37606, -71.09623],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632151&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T03:34:09Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171140&apos;,
  &apos;pos&apos;: [42.3764817, -71.0998701],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6619643&apos;,
   &apos;timestamp&apos;: &apos;2010-12-11T07:14:33Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61171145&apos;,
  &apos;pos&apos;: [42.3766261, -71.1043605],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3169035&apos;,
   &apos;timestamp&apos;: &apos;2009-11-20T15:01:48Z&apos;,
   &apos;uid&apos;: &apos;175058&apos;,
   &apos;user&apos;: &apos;Tom Walsh&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171170&apos;,
  &apos;pos&apos;: [42.3771247, -71.1049509],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13435407&apos;,
   &apos;timestamp&apos;: &apos;2012-10-10T02:03:51Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61171187&apos;,
  &apos;pos&apos;: [42.377842, -71.0958634],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13435407&apos;,
   &apos;timestamp&apos;: &apos;2012-10-10T02:03:51Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;id&apos;: &apos;61171188&apos;,
  &apos;pos&apos;: [42.3779391, -71.0958888],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6619643&apos;,
   &apos;timestamp&apos;: &apos;2010-12-11T07:14:54Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171192&apos;,
  &apos;pos&apos;: [42.3785424, -71.1051809],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:30:19Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171202&apos;,
  &apos;pos&apos;: [42.380671, -71.0886],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:45:51Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171205&apos;,
  &apos;pos&apos;: [42.377988, -71.091043],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6619643&apos;,
   &apos;timestamp&apos;: &apos;2010-12-11T07:15:04Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;crossing&apos;: &apos;traffic_signals&apos;,
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171206&apos;,
  &apos;pos&apos;: [42.3782853, -71.1063731],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:21Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171207&apos;,
  &apos;pos&apos;: [42.3796201, -71.0914086],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6642755&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T22:15:38Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61171208&apos;,
  &apos;pos&apos;: [42.3789507, -71.1071915],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6642755&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T22:14:54Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61171209&apos;,
  &apos;pos&apos;: [42.3788851, -71.1071092],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;21189633&apos;,
   &apos;timestamp&apos;: &apos;2014-03-19T10:38:22Z&apos;,
   &apos;uid&apos;: &apos;1670311&apos;,
   &apos;user&apos;: &apos;SophoM&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171234&apos;,
  &apos;pos&apos;: [42.386836, -71.098724],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6642755&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T22:15:31Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61171235&apos;,
  &apos;pos&apos;: [42.3808503, -71.104343],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:43Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171236&apos;,
  &apos;pos&apos;: [42.387237, -71.099921],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:43Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171237&apos;,
  &apos;pos&apos;: [42.38701, -71.099242],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;4046063&apos;,
   &apos;timestamp&apos;: &apos;2010-03-06T00:12:24Z&apos;,
   &apos;uid&apos;: &apos;23351&apos;,
   &apos;user&apos;: &apos;JasonWoof&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171238&apos;,
  &apos;pos&apos;: [42.3876325, -71.1011089],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:45Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171239&apos;,
  &apos;pos&apos;: [42.387347, -71.100261],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:46Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171240&apos;,
  &apos;pos&apos;: [42.387907, -71.1019],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:07Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171242&apos;,
  &apos;pos&apos;: [42.3945236, -71.1177573],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:15Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171349&apos;,
  &apos;pos&apos;: [42.405231, -71.130333],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:15Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171350&apos;,
  &apos;pos&apos;: [42.405117, -71.130178],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:16Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171351&apos;,
  &apos;pos&apos;: [42.405101, -71.130158],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T20:12:28Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171355&apos;,
  &apos;pos&apos;: [42.3976391, -71.0842658],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T20:12:28Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171356&apos;,
  &apos;pos&apos;: [42.3980323, -71.0841329],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2090105&apos;,
   &apos;timestamp&apos;: &apos;2009-08-09T20:33:17Z&apos;,
   &apos;uid&apos;: &apos;42429&apos;,
   &apos;user&apos;: &apos;42429&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171357&apos;,
  &apos;pos&apos;: [42.379881, -71.090653],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;19670450&apos;,
   &apos;timestamp&apos;: &apos;2013-12-27T22:09:31Z&apos;,
   &apos;uid&apos;: &apos;1670311&apos;,
   &apos;user&apos;: &apos;SophoM&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61171367&apos;,
  &apos;pos&apos;: [42.380125, -71.0892987],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:30:27Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171368&apos;,
  &apos;pos&apos;: [42.379998, -71.089397],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16591452&apos;,
   &apos;timestamp&apos;: &apos;2013-06-17T15:52:03Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171375&apos;,
  &apos;pos&apos;: [42.4069869, -71.1248238],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16591452&apos;,
   &apos;timestamp&apos;: &apos;2013-06-17T15:52:03Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171385&apos;,
  &apos;pos&apos;: [42.4068535, -71.1249179],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6008358&apos;,
   &apos;timestamp&apos;: &apos;2010-10-11T03:57:31Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171388&apos;,
  &apos;pos&apos;: [42.3815556, -71.103943],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6642755&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T22:14:58Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171398&apos;,
  &apos;pos&apos;: [42.3810181, -71.10424],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6682746&apos;,
   &apos;timestamp&apos;: &apos;2010-12-16T23:34:43Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171424&apos;,
  &apos;pos&apos;: [42.3798882, -71.0902444],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:30:34Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171427&apos;,
  &apos;pos&apos;: [42.379914, -71.089672],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:30:35Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171428&apos;,
  &apos;pos&apos;: [42.379936, -71.08956],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:30:35Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171429&apos;,
  &apos;pos&apos;: [42.379948, -71.089498],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;30487413&apos;,
   &apos;timestamp&apos;: &apos;2015-04-25T23:28:23Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61171434&apos;,
  &apos;pos&apos;: [42.3913281, -71.1188059],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12899968&apos;,
   &apos;timestamp&apos;: &apos;2012-08-29T02:16:01Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171436&apos;,
  &apos;pos&apos;: [42.3758188, -71.0845435],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:44Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171442&apos;,
  &apos;pos&apos;: [42.393343, -71.097892],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:22:45Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171443&apos;,
  &apos;pos&apos;: [42.393299, -71.097925],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:48Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171446&apos;,
  &apos;pos&apos;: [42.389319, -71.100864],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:49Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171447&apos;,
  &apos;pos&apos;: [42.389181, -71.100963],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:38:11Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171454&apos;,
  &apos;pos&apos;: [42.386036, -71.088937],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:38:12Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171455&apos;,
  &apos;pos&apos;: [42.385935, -71.088617],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;27238329&apos;,
   &apos;timestamp&apos;: &apos;2014-12-04T16:14:44Z&apos;,
   &apos;uid&apos;: &apos;2462466&apos;,
   &apos;user&apos;: &apos;EvanMula&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171456&apos;,
  &apos;pos&apos;: [42.385692, -71.087838],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3043710&apos;,
   &apos;timestamp&apos;: &apos;2009-11-05T20:43:26Z&apos;,
   &apos;uid&apos;: &apos;179506&apos;,
   &apos;user&apos;: &apos;nkhall&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171460&apos;,
  &apos;pos&apos;: [42.378791, -71.094311],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26242718&apos;,
   &apos;timestamp&apos;: &apos;2014-10-21T20:50:32Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171464&apos;,
  &apos;pos&apos;: [42.3877941, -71.1096354],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:04:51Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171472&apos;,
  &apos;pos&apos;: [42.39463, -71.116446],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:04:52Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171473&apos;,
  &apos;pos&apos;: [42.394991, -71.117375],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:04:53Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171474&apos;,
  &apos;pos&apos;: [42.394822, -71.117517],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3043710&apos;,
   &apos;timestamp&apos;: &apos;2009-11-05T20:43:22Z&apos;,
   &apos;uid&apos;: &apos;179506&apos;,
   &apos;user&apos;: &apos;nkhall&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171490&apos;,
  &apos;pos&apos;: [42.378038, -71.094829],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;19072675&apos;,
   &apos;timestamp&apos;: &apos;2013-11-23T14:45:07Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61171493&apos;,
  &apos;pos&apos;: [42.3912504, -71.0913321],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:45:59Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171494&apos;,
  &apos;pos&apos;: [42.374344, -71.090233],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:00Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171495&apos;,
  &apos;pos&apos;: [42.374573, -71.090181],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:44Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61171497&apos;,
  &apos;pos&apos;: [42.375016, -71.0900797],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32061008&apos;,
   &apos;timestamp&apos;: &apos;2015-06-18T22:41:06Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171499&apos;,
  &apos;pos&apos;: [42.3944388, -71.0835447],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:02Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171502&apos;,
  &apos;pos&apos;: [42.375508, -71.094088],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:03Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171503&apos;,
  &apos;pos&apos;: [42.375226, -71.094018],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:04Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171505&apos;,
  &apos;pos&apos;: [42.375782, -71.094234],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:05Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171508&apos;,
  &apos;pos&apos;: [42.375592, -71.094108],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6664722&apos;,
   &apos;timestamp&apos;: &apos;2010-12-15T05:57:11Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171512&apos;,
  &apos;pos&apos;: [42.3806232, -71.1010554],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T11:06:07Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171565&apos;,
  &apos;pos&apos;: [42.374253, -71.093746],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:05Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171566&apos;,
  &apos;pos&apos;: [42.374701, -71.09386],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T22:20:36Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171581&apos;,
  &apos;pos&apos;: [42.3960527, -71.0884265],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32032153&apos;,
   &apos;timestamp&apos;: &apos;2015-06-17T15:49:10Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61171593&apos;,
  &apos;pos&apos;: [42.3957311, -71.0839012],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6020841&apos;,
   &apos;timestamp&apos;: &apos;2010-10-12T13:22:22Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171594&apos;,
  &apos;pos&apos;: [42.3868143, -71.1132926],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:06Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171608&apos;,
  &apos;pos&apos;: [42.374377, -71.096331],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:09Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171615&apos;,
  &apos;pos&apos;: [42.375868, -71.095239],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T02:55:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171682&apos;,
  &apos;pos&apos;: [42.3939717, -71.0932533],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:37:56Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171698&apos;,
  &apos;pos&apos;: [42.3866387, -71.0908259],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31954058&apos;,
   &apos;timestamp&apos;: &apos;2015-06-14T03:03:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171710&apos;,
  &apos;pos&apos;: [42.3866189, -71.0785866],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31954058&apos;,
   &apos;timestamp&apos;: &apos;2015-06-14T03:03:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171713&apos;,
  &apos;pos&apos;: [42.387021, -71.0790022],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31954058&apos;,
   &apos;timestamp&apos;: &apos;2015-06-14T03:03:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171716&apos;,
  &apos;pos&apos;: [42.3872007, -71.0791746],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31954058&apos;,
   &apos;timestamp&apos;: &apos;2015-06-14T03:03:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171718&apos;,
  &apos;pos&apos;: [42.3874817, -71.0794553],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6683709&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T06:09:48Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171720&apos;,
  &apos;pos&apos;: [42.3876643, -71.0796352],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6692363&apos;,
   &apos;timestamp&apos;: &apos;2010-12-18T00:58:54Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171721&apos;,
  &apos;pos&apos;: [42.3879382, -71.0799048],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6692363&apos;,
   &apos;timestamp&apos;: &apos;2010-12-18T00:58:54Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171723&apos;,
  &apos;pos&apos;: [42.3881945, -71.0801414],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632151&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T03:33:53Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171725&apos;,
  &apos;pos&apos;: [42.3765873, -71.0991648],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26653037&apos;,
   &apos;timestamp&apos;: &apos;2014-11-08T22:26:23Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171764&apos;,
  &apos;pos&apos;: [42.3890983, -71.0866745],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:15Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61171810&apos;,
  &apos;pos&apos;: [42.3944372, -71.1084288],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:02Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171814&apos;,
  &apos;pos&apos;: [42.3942492, -71.1080107],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2420446&apos;,
   &apos;timestamp&apos;: &apos;2009-09-09T00:44:05Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171834&apos;,
  &apos;pos&apos;: [42.387817, -71.11779],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2420446&apos;,
   &apos;timestamp&apos;: &apos;2009-09-09T00:44:05Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171841&apos;,
  &apos;pos&apos;: [42.387465, -71.117161],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12899968&apos;,
   &apos;timestamp&apos;: &apos;2012-08-29T02:16:01Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171852&apos;,
  &apos;pos&apos;: [42.375771, -71.0854704],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:09Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171853&apos;,
  &apos;pos&apos;: [42.376204, -71.085879],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:10Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171854&apos;,
  &apos;pos&apos;: [42.376808, -71.086463],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12899968&apos;,
   &apos;timestamp&apos;: &apos;2012-08-29T02:16:01Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171857&apos;,
  &apos;pos&apos;: [42.3755668, -71.085282],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12899968&apos;,
   &apos;timestamp&apos;: &apos;2012-08-29T02:16:01Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171858&apos;,
  &apos;pos&apos;: [42.3756585, -71.0853932],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12899968&apos;,
   &apos;timestamp&apos;: &apos;2012-08-29T02:16:01Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171859&apos;,
  &apos;pos&apos;: [42.3757316, -71.085454],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3296696&apos;,
   &apos;timestamp&apos;: &apos;2009-12-05T17:01:22Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171861&apos;,
  &apos;pos&apos;: [42.385544, -71.106413],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6691095&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T21:56:16Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171868&apos;,
  &apos;pos&apos;: [42.387881, -71.0840065],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6691095&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T21:56:16Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171869&apos;,
  &apos;pos&apos;: [42.3878195, -71.0841754],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:38:35Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171870&apos;,
  &apos;pos&apos;: [42.388168, -71.084663],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:15Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171877&apos;,
  &apos;pos&apos;: [42.374669, -71.091503],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:44Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61171880&apos;,
  &apos;pos&apos;: [42.3752244, -71.0928312],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:50Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171886&apos;,
  &apos;pos&apos;: [42.389545, -71.100701],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:16Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171897&apos;,
  &apos;pos&apos;: [42.374868, -71.091904],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:44Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171898&apos;,
  &apos;pos&apos;: [42.3751239, -71.0924476],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;27238329&apos;,
   &apos;timestamp&apos;: &apos;2014-12-04T16:14:44Z&apos;,
   &apos;uid&apos;: &apos;2462466&apos;,
   &apos;user&apos;: &apos;EvanMula&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61171899&apos;,
  &apos;pos&apos;: [42.3911386, -71.0911675],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T02:55:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171901&apos;,
  &apos;pos&apos;: [42.3913076, -71.0911679],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T02:55:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171902&apos;,
  &apos;pos&apos;: [42.3912261, -71.0910545],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;19072675&apos;,
   &apos;timestamp&apos;: &apos;2013-11-23T14:45:07Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61171905&apos;,
  &apos;pos&apos;: [42.390601, -71.0903191],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T02:55:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61171906&apos;,
  &apos;pos&apos;: [42.3909947, -71.0906528],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:51Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61171919&apos;,
  &apos;pos&apos;: [42.390099, -71.100302],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7681591&apos;,
   &apos;timestamp&apos;: &apos;2011-03-27T01:22:25Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61171924&apos;,
  &apos;pos&apos;: [42.3837897, -71.0813291],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32032153&apos;,
   &apos;timestamp&apos;: &apos;2015-06-17T15:49:10Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61171942&apos;,
  &apos;pos&apos;: [42.3962994, -71.084037],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12071828&apos;,
   &apos;timestamp&apos;: &apos;2012-07-01T05:41:27Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61171999&apos;,
  &apos;pos&apos;: [42.414647, -71.1301816],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:52:39Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172015&apos;,
  &apos;pos&apos;: [42.3834975, -71.0861555],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7681365&apos;,
   &apos;timestamp&apos;: &apos;2011-03-27T00:12:36Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172019&apos;,
  &apos;pos&apos;: [42.3825298, -71.0855831],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:18Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172020&apos;,
  &apos;pos&apos;: [42.376569, -71.099309],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11694735&apos;,
   &apos;timestamp&apos;: &apos;2012-05-25T01:08:06Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172025&apos;,
  &apos;pos&apos;: [42.3817853, -71.0860815],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;5970253&apos;,
   &apos;timestamp&apos;: &apos;2010-10-06T15:19:07Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172030&apos;,
  &apos;pos&apos;: [42.3957312, -71.1071422],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845520&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T00:52:05Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172035&apos;,
  &apos;pos&apos;: [42.3893307, -71.1167018],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:51:44Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172044&apos;,
  &apos;pos&apos;: [42.397118, -71.120731],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;21963413&apos;,
   &apos;timestamp&apos;: &apos;2014-04-26T20:31:33Z&apos;,
   &apos;uid&apos;: &apos;2049068&apos;,
   &apos;user&apos;: &apos;Ron Newman&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172059&apos;,
  &apos;pos&apos;: [42.3879592, -71.095974],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:10Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172067&apos;,
  &apos;pos&apos;: [42.3958893, -71.109759],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;25971126&apos;,
   &apos;timestamp&apos;: &apos;2014-10-09T21:51:47Z&apos;,
   &apos;uid&apos;: &apos;2389162&apos;,
   &apos;user&apos;: &apos;mapper117&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172068&apos;,
  &apos;pos&apos;: [42.388142, -71.0957372],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31954058&apos;,
   &apos;timestamp&apos;: &apos;2015-06-14T02:36:30Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61172071&apos;,
  &apos;pos&apos;: [42.3901301, -71.081776],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12528124&apos;,
   &apos;timestamp&apos;: &apos;2012-07-28T20:43:03Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172075&apos;,
  &apos;pos&apos;: [42.3866642, -71.1162815],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:04Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172077&apos;,
  &apos;pos&apos;: [42.395764, -71.1098498],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16582966&apos;,
   &apos;timestamp&apos;: &apos;2013-06-16T23:16:49Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172082&apos;,
  &apos;pos&apos;: [42.3878128, -71.0958113],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16582966&apos;,
   &apos;timestamp&apos;: &apos;2013-06-16T23:16:50Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172083&apos;,
  &apos;pos&apos;: [42.3876611, -71.0956486],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16582966&apos;,
   &apos;timestamp&apos;: &apos;2013-06-16T23:16:49Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172084&apos;,
  &apos;pos&apos;: [42.3874673, -71.0954388],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12528124&apos;,
   &apos;timestamp&apos;: &apos;2012-07-28T20:43:03Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172085&apos;,
  &apos;pos&apos;: [42.3865498, -71.1162675],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:33:59Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172102&apos;,
  &apos;pos&apos;: [42.389638, -71.100635],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6120857&apos;,
   &apos;timestamp&apos;: &apos;2010-10-20T23:37:09Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172103&apos;,
  &apos;pos&apos;: [42.3898779, -71.1004639],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:34:01Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172104&apos;,
  &apos;pos&apos;: [42.389813, -71.100508],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16582966&apos;,
   &apos;timestamp&apos;: &apos;2013-06-16T23:16:49Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172105&apos;,
  &apos;pos&apos;: [42.3869088, -71.0948817],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16582966&apos;,
   &apos;timestamp&apos;: &apos;2013-06-16T23:16:50Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172106&apos;,
  &apos;pos&apos;: [42.3866849, -71.0946484],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:34:03Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172107&apos;,
  &apos;pos&apos;: [42.386383, -71.094352],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:34:04Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172108&apos;,
  &apos;pos&apos;: [42.386095, -71.094056],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16582966&apos;,
   &apos;timestamp&apos;: &apos;2013-06-16T23:16:50Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172109&apos;,
  &apos;pos&apos;: [42.3872534, -71.0952183],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6120857&apos;,
   &apos;timestamp&apos;: &apos;2010-10-20T23:37:27Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172116&apos;,
  &apos;pos&apos;: [42.389717, -71.1005758],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:15Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172118&apos;,
  &apos;pos&apos;: [42.3965851, -71.1092773],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7681365&apos;,
   &apos;timestamp&apos;: &apos;2011-03-27T00:12:36Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172122&apos;,
  &apos;pos&apos;: [42.3820532, -71.0858999],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6993097&apos;,
   &apos;timestamp&apos;: &apos;2011-01-16T20:09:37Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172132&apos;,
  &apos;pos&apos;: [42.3967697, -71.1247942],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:21Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172137&apos;,
  &apos;pos&apos;: [42.3796165, -71.0946846],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:15:45Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172144&apos;,
  &apos;pos&apos;: [42.382337, -71.111385],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31954058&apos;,
   &apos;timestamp&apos;: &apos;2015-06-14T03:03:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172148&apos;,
  &apos;pos&apos;: [42.387592, -71.0784184],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:20Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172160&apos;,
  &apos;pos&apos;: [42.376153, -71.083861],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:37:56Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172164&apos;,
  &apos;pos&apos;: [42.3878444, -71.094733],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;5970253&apos;,
   &apos;timestamp&apos;: &apos;2010-10-06T15:19:15Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172165&apos;,
  &apos;pos&apos;: [42.3954757, -71.1073193],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:37:56Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172173&apos;,
  &apos;pos&apos;: [42.3875513, -71.0937676],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:21Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172194&apos;,
  &apos;pos&apos;: [42.375462, -71.095116],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:21Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172195&apos;,
  &apos;pos&apos;: [42.375283, -71.095062],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2420387&apos;,
   &apos;timestamp&apos;: &apos;2009-09-09T00:21:04Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172197&apos;,
  &apos;pos&apos;: [42.3750909, -71.0950075],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:23Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172198&apos;,
  &apos;pos&apos;: [42.375808, -71.094708],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:45Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172212&apos;,
  &apos;pos&apos;: [42.4029453, -71.1264735],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:20Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172214&apos;,
  &apos;pos&apos;: [42.403909, -71.12687],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:21Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172215&apos;,
  &apos;pos&apos;: [42.404128, -71.126735],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26633392&apos;,
   &apos;timestamp&apos;: &apos;2014-11-08T02:25:52Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61172216&apos;,
  &apos;pos&apos;: [42.403293, -71.127246],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:22Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172217&apos;,
  &apos;pos&apos;: [42.40364, -71.127035],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:23Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172224&apos;,
  &apos;pos&apos;: [42.404839, -71.126231],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3383517&apos;,
   &apos;timestamp&apos;: &apos;2009-12-15T22:37:48Z&apos;,
   &apos;uid&apos;: &apos;175058&apos;,
   &apos;user&apos;: &apos;Tom Walsh&apos;,
   &apos;version&apos;: &apos;9&apos;},
  &apos;crossing&apos;: &apos;traffic_signals&apos;,
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61172228&apos;,
  &apos;pos&apos;: [42.3769336, -71.0955906],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2271795&apos;,
   &apos;timestamp&apos;: &apos;2009-08-26T21:14:18Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172231&apos;,
  &apos;pos&apos;: [42.376449, -71.09597],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3424734&apos;,
   &apos;timestamp&apos;: &apos;2009-12-22T04:29:23Z&apos;,
   &apos;uid&apos;: &apos;23351&apos;,
   &apos;user&apos;: &apos;JasonWoof&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172248&apos;,
  &apos;pos&apos;: [42.3766552, -71.0978769],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:21Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172284&apos;,
  &apos;pos&apos;: [42.3797118, -71.0956969],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172292&apos;,
  &apos;pos&apos;: [42.3797217, -71.0957904],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:33Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172302&apos;,
  &apos;pos&apos;: [42.379475, -71.097975],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:34Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172303&apos;,
  &apos;pos&apos;: [42.379503, -71.097696],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:50:56Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172325&apos;,
  &apos;pos&apos;: [42.3890216, -71.116415],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6020841&apos;,
   &apos;timestamp&apos;: &apos;2010-10-12T13:22:13Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172339&apos;,
  &apos;pos&apos;: [42.389226, -71.116608],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:52:39Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172387&apos;,
  &apos;pos&apos;: [42.3838381, -71.087857],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:52:39Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172388&apos;,
  &apos;pos&apos;: [42.3838109, -71.087739],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:22Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172391&apos;,
  &apos;pos&apos;: [42.378961, -71.091969],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13435407&apos;,
   &apos;timestamp&apos;: &apos;2012-10-10T02:03:51Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172392&apos;,
  &apos;pos&apos;: [42.3782927, -71.0918574],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:15:47Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172400&apos;,
  &apos;pos&apos;: [42.38193, -71.103721],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;crossing&apos;,
  &apos;id&apos;: &apos;61172401&apos;,
  &apos;pos&apos;: [42.3793765, -71.0920266],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:24Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172402&apos;,
  &apos;pos&apos;: [42.379252, -71.092001],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172404&apos;,
  &apos;pos&apos;: [42.3794659, -71.0921827],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:10Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172408&apos;,
  &apos;pos&apos;: [42.3945302, -71.1107146],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:04Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61172409&apos;,
  &apos;pos&apos;: [42.3944384, -71.110782],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:08Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172416&apos;,
  &apos;pos&apos;: [42.3952273, -71.1102205],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26764866&apos;,
   &apos;timestamp&apos;: &apos;2014-11-13T20:43:35Z&apos;,
   &apos;uid&apos;: &apos;61257&apos;,
   &apos;user&apos;: &apos;mregan&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61172421&apos;,
  &apos;pos&apos;: [42.405437, -71.125837],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:26Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172422&apos;,
  &apos;pos&apos;: [42.405112, -71.126061],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:26Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172423&apos;,
  &apos;pos&apos;: [42.40481, -71.126253],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:27Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172424&apos;,
  &apos;pos&apos;: [42.404314, -71.126589],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;862336&apos;,
   &apos;timestamp&apos;: &apos;2009-03-26T14:27:19Z&apos;,
   &apos;uid&apos;: &apos;110489&apos;,
   &apos;user&apos;: &apos;Pouletic&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172429&apos;,
  &apos;pos&apos;: [42.376189, -71.088948],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;862336&apos;,
   &apos;timestamp&apos;: &apos;2009-03-26T14:27:19Z&apos;,
   &apos;uid&apos;: &apos;110489&apos;,
   &apos;user&apos;: &apos;Pouletic&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172430&apos;,
  &apos;pos&apos;: [42.37582, -71.08878],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;862336&apos;,
   &apos;timestamp&apos;: &apos;2009-03-26T14:27:19Z&apos;,
   &apos;uid&apos;: &apos;110489&apos;,
   &apos;user&apos;: &apos;Pouletic&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172431&apos;,
  &apos;pos&apos;: [42.374964, -71.088424],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;862336&apos;,
   &apos;timestamp&apos;: &apos;2009-03-26T14:27:19Z&apos;,
   &apos;uid&apos;: &apos;110489&apos;,
   &apos;user&apos;: &apos;Pouletic&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172432&apos;,
  &apos;pos&apos;: [42.37484, -71.08837],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;862336&apos;,
   &apos;timestamp&apos;: &apos;2009-03-26T14:27:19Z&apos;,
   &apos;uid&apos;: &apos;110489&apos;,
   &apos;user&apos;: &apos;Pouletic&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172435&apos;,
  &apos;pos&apos;: [42.376737, -71.089119],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;862336&apos;,
   &apos;timestamp&apos;: &apos;2009-03-26T14:27:19Z&apos;,
   &apos;uid&apos;: &apos;110489&apos;,
   &apos;user&apos;: &apos;Pouletic&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172436&apos;,
  &apos;pos&apos;: [42.376428, -71.089046],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:30Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172442&apos;,
  &apos;pos&apos;: [42.404334, -71.129133],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;1806622&apos;,
   &apos;timestamp&apos;: &apos;2009-07-12T13:32:33Z&apos;,
   &apos;uid&apos;: &apos;60604&apos;,
   &apos;user&apos;: &apos;cmurtaugh&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;id&apos;: &apos;61172443&apos;,
  &apos;pos&apos;: [42.3839018, -71.1036438],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:23:06Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172446&apos;,
  &apos;pos&apos;: [42.390894, -71.100735],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:54:50Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172457&apos;,
  &apos;pos&apos;: [42.398942, -71.109347],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:37:56Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172458&apos;,
  &apos;pos&apos;: [42.3876206, -71.0939963],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:11Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172460&apos;,
  &apos;pos&apos;: [42.3986993, -71.1086189],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:54:52Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172463&apos;,
  &apos;pos&apos;: [42.398928, -71.110909],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:54:53Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172464&apos;,
  &apos;pos&apos;: [42.399507, -71.111316],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:48:48Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172472&apos;,
  &apos;pos&apos;: [42.404015, -71.117199],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7425893&apos;,
   &apos;timestamp&apos;: &apos;2011-02-28T23:52:17Z&apos;,
   &apos;uid&apos;: &apos;23351&apos;,
   &apos;user&apos;: &apos;JasonWoof&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172479&apos;,
  &apos;pos&apos;: [42.4039634, -71.1199048],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16591452&apos;,
   &apos;timestamp&apos;: &apos;2013-06-17T15:52:03Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172482&apos;,
  &apos;pos&apos;: [42.404029, -71.1175103],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16591452&apos;,
   &apos;timestamp&apos;: &apos;2013-06-17T15:52:03Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172484&apos;,
  &apos;pos&apos;: [42.4042441, -71.1180185],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T21:50:08Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61172514&apos;,
  &apos;pos&apos;: [42.3975703, -71.0845903],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:48:51Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172524&apos;,
  &apos;pos&apos;: [42.404567, -71.12144],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12071447&apos;,
   &apos;timestamp&apos;: &apos;2012-07-01T01:58:04Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172530&apos;,
  &apos;pos&apos;: [42.4145691, -71.1322815],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12071447&apos;,
   &apos;timestamp&apos;: &apos;2012-07-01T01:58:04Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172531&apos;,
  &apos;pos&apos;: [42.4145678, -71.1324598],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12071828&apos;,
   &apos;timestamp&apos;: &apos;2012-07-01T05:41:27Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172533&apos;,
  &apos;pos&apos;: [42.4146019, -71.1318589],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:15Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172534&apos;,
  &apos;pos&apos;: [42.407822, -71.130624],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:16Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172536&apos;,
  &apos;pos&apos;: [42.407796, -71.130774],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:16Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172537&apos;,
  &apos;pos&apos;: [42.407809, -71.13073],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:17Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172538&apos;,
  &apos;pos&apos;: [42.407708, -71.130812],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:17Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172539&apos;,
  &apos;pos&apos;: [42.407772, -71.130793],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:18Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172540&apos;,
  &apos;pos&apos;: [42.407648, -71.130866],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:18Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172541&apos;,
  &apos;pos&apos;: [42.407668, -71.13082],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:19Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172542&apos;,
  &apos;pos&apos;: [42.40759, -71.131309],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845885&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:50:00Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172543&apos;,
  &apos;pos&apos;: [42.4076189, -71.131055],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:19Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172544&apos;,
  &apos;pos&apos;: [42.407575, -71.131616],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:20Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172545&apos;,
  &apos;pos&apos;: [42.407572, -71.131522],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:20Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172546&apos;,
  &apos;pos&apos;: [42.407583, -71.131818],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:21Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172547&apos;,
  &apos;pos&apos;: [42.407587, -71.131764],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:21Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172549&apos;,
  &apos;pos&apos;: [42.407498, -71.13205],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:15:50Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172550&apos;,
  &apos;pos&apos;: [42.385135, -71.109152],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:15:50Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172551&apos;,
  &apos;pos&apos;: [42.384987, -71.108998],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6020841&apos;,
   &apos;timestamp&apos;: &apos;2010-10-12T13:22:41Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172552&apos;,
  &apos;pos&apos;: [42.3848176, -71.1089011],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2090105&apos;,
   &apos;timestamp&apos;: &apos;2009-08-09T20:33:17Z&apos;,
   &apos;uid&apos;: &apos;42429&apos;,
   &apos;user&apos;: &apos;42429&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172556&apos;,
  &apos;pos&apos;: [42.390026, -71.075732],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:05:23Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172567&apos;,
  &apos;pos&apos;: [42.396713, -71.102385],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;8287220&apos;,
   &apos;timestamp&apos;: &apos;2011-05-29T23:16:41Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172574&apos;,
  &apos;pos&apos;: [42.3956682, -71.1030771],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:54:54Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172584&apos;,
  &apos;pos&apos;: [42.399112, -71.109331],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;485479&apos;,
   &apos;timestamp&apos;: &apos;2009-02-16T17:55:29Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172589&apos;,
  &apos;pos&apos;: [42.399113, -71.109041],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32037178&apos;,
   &apos;timestamp&apos;: &apos;2015-06-17T19:51:09Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172591&apos;,
  &apos;pos&apos;: [42.3966063, -71.0843863],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32032153&apos;,
   &apos;timestamp&apos;: &apos;2015-06-17T15:49:10Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61172592&apos;,
  &apos;pos&apos;: [42.3965386, -71.0846586],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32037178&apos;,
   &apos;timestamp&apos;: &apos;2015-06-17T19:51:09Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61172594&apos;,
  &apos;pos&apos;: [42.396755, -71.0844573],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T20:12:28Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172597&apos;,
  &apos;pos&apos;: [42.3971383, -71.0844441],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26584106&apos;,
   &apos;timestamp&apos;: &apos;2014-11-06T01:47:54Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61172598&apos;,
  &apos;pos&apos;: [42.3964098, -71.1036571],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T21:50:08Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61172621&apos;,
  &apos;pos&apos;: [42.3964243, -71.0850071],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T22:20:36Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172623&apos;,
  &apos;pos&apos;: [42.3955105, -71.0853285],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T22:20:36Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172626&apos;,
  &apos;pos&apos;: [42.3948538, -71.0856174],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:39Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172630&apos;,
  &apos;pos&apos;: [42.375623, -71.098249],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2255148&apos;,
   &apos;timestamp&apos;: &apos;2009-08-25T12:15:40Z&apos;,
   &apos;uid&apos;: &apos;38786&apos;,
   &apos;user&apos;: &apos;Ian McIntosh&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172635&apos;,
  &apos;pos&apos;: [42.4060884, -71.1329023],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2255148&apos;,
   &apos;timestamp&apos;: &apos;2009-08-25T12:15:40Z&apos;,
   &apos;uid&apos;: &apos;38786&apos;,
   &apos;user&apos;: &apos;Ian McIntosh&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172637&apos;,
  &apos;pos&apos;: [42.4063863, -71.1328422],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12071828&apos;,
   &apos;timestamp&apos;: &apos;2012-07-01T05:41:27Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172639&apos;,
  &apos;pos&apos;: [42.4145949, -71.1317809],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12071447&apos;,
   &apos;timestamp&apos;: &apos;2012-07-01T03:05:03Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172640&apos;,
  &apos;pos&apos;: [42.4065403, -71.1328065],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16591452&apos;,
   &apos;timestamp&apos;: &apos;2013-06-17T15:55:12Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172656&apos;,
  &apos;pos&apos;: [42.4015809, -71.116829],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;34152985&apos;,
   &apos;timestamp&apos;: &apos;2015-09-21T03:30:12Z&apos;,
   &apos;uid&apos;: &apos;485808&apos;,
   &apos;user&apos;: &apos;Alexey Lukin&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172657&apos;,
  &apos;pos&apos;: [42.3806562, -71.0886374],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20948023&apos;,
   &apos;timestamp&apos;: &apos;2014-03-06T11:39:43Z&apos;,
   &apos;uid&apos;: &apos;1670311&apos;,
   &apos;user&apos;: &apos;SophoM&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61172660&apos;,
  &apos;pos&apos;: [42.3736771, -71.0820567],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26734067&apos;,
   &apos;timestamp&apos;: &apos;2014-11-12T12:49:34Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61172687&apos;,
  &apos;pos&apos;: [42.381656, -71.0838914],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11220134&apos;,
   &apos;timestamp&apos;: &apos;2012-04-08T00:52:41Z&apos;,
   &apos;uid&apos;: &apos;54419&apos;,
   &apos;user&apos;: &apos;giovanni berlanda&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172697&apos;,
  &apos;pos&apos;: [42.375082, -71.0995717],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:35Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172701&apos;,
  &apos;pos&apos;: [42.379459, -71.088971],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:35Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172703&apos;,
  &apos;pos&apos;: [42.379142, -71.088646],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:36Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172705&apos;,
  &apos;pos&apos;: [42.3786313, -71.0881268],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:37Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172707&apos;,
  &apos;pos&apos;: [42.378017, -71.087579],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;25030803&apos;,
   &apos;timestamp&apos;: &apos;2014-08-26T15:26:39Z&apos;,
   &apos;uid&apos;: &apos;1829683&apos;,
   &apos;user&apos;: &apos;Luis36995&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61172709&apos;,
  &apos;pos&apos;: [42.3815813, -71.0845536],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:35Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172710&apos;,
  &apos;pos&apos;: [42.405376, -71.133282],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:36Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172712&apos;,
  &apos;pos&apos;: [42.405486, -71.133371],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:37Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172714&apos;,
  &apos;pos&apos;: [42.405141, -71.13328],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:37Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172716&apos;,
  &apos;pos&apos;: [42.405207, -71.13326],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:48:51Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172718&apos;,
  &apos;pos&apos;: [42.404271, -71.121622],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2255148&apos;,
   &apos;timestamp&apos;: &apos;2009-08-25T12:15:39Z&apos;,
   &apos;uid&apos;: &apos;38786&apos;,
   &apos;user&apos;: &apos;Ian McIntosh&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172720&apos;,
  &apos;pos&apos;: [42.4049033, -71.1335117],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2255148&apos;,
   &apos;timestamp&apos;: &apos;2009-08-25T12:15:40Z&apos;,
   &apos;uid&apos;: &apos;38786&apos;,
   &apos;user&apos;: &apos;Ian McIntosh&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172726&apos;,
  &apos;pos&apos;: [42.4061138, -71.1335117],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2255148&apos;,
   &apos;timestamp&apos;: &apos;2009-08-25T12:15:39Z&apos;,
   &apos;uid&apos;: &apos;38786&apos;,
   &apos;user&apos;: &apos;Ian McIntosh&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172730&apos;,
  &apos;pos&apos;: [42.4058919, -71.1338378],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2255148&apos;,
   &apos;timestamp&apos;: &apos;2009-08-25T12:15:39Z&apos;,
   &apos;uid&apos;: &apos;38786&apos;,
   &apos;user&apos;: &apos;Ian McIntosh&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172734&apos;,
  &apos;pos&apos;: [42.4057208, -71.1337949],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2255148&apos;,
   &apos;timestamp&apos;: &apos;2009-08-25T12:15:39Z&apos;,
   &apos;uid&apos;: &apos;38786&apos;,
   &apos;user&apos;: &apos;Ian McIntosh&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172736&apos;,
  &apos;pos&apos;: [42.4057905, -71.1338464],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16591452&apos;,
   &apos;timestamp&apos;: &apos;2013-06-17T15:52:03Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172838&apos;,
  &apos;pos&apos;: [42.4064899, -71.1251517],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:45Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172839&apos;,
  &apos;pos&apos;: [42.406362, -71.127677],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:48:52Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172842&apos;,
  &apos;pos&apos;: [42.406741, -71.121908],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:48:53Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172845&apos;,
  &apos;pos&apos;: [42.406964, -71.121752],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32032153&apos;,
   &apos;timestamp&apos;: &apos;2015-06-17T15:49:10Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61172847&apos;,
  &apos;pos&apos;: [42.3963017, -71.0842989],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:46Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61172856&apos;,
  &apos;pos&apos;: [42.407093, -71.129633],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:05:30Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172861&apos;,
  &apos;pos&apos;: [42.396692, -71.097517],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:22:05Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172967&apos;,
  &apos;pos&apos;: [42.379473, -71.106964],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:46:38Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172969&apos;,
  &apos;pos&apos;: [42.377845, -71.090633],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:32:16Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61172987&apos;,
  &apos;pos&apos;: [42.380056, -71.09032],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7140156&apos;,
   &apos;timestamp&apos;: &apos;2011-01-30T21:44:49Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173038&apos;,
  &apos;pos&apos;: [42.4047607, -71.129705],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:48:54Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173041&apos;,
  &apos;pos&apos;: [42.404953, -71.124692],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:48:54Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173043&apos;,
  &apos;pos&apos;: [42.403225, -71.115557],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:48:55Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173045&apos;,
  &apos;pos&apos;: [42.405123, -71.115861],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:48:57Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173049&apos;,
  &apos;pos&apos;: [42.402573, -71.115431],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:38:55Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173051&apos;,
  &apos;pos&apos;: [42.403998, -71.128658],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7140409&apos;,
   &apos;timestamp&apos;: &apos;2011-01-30T22:06:39Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173053&apos;,
  &apos;pos&apos;: [42.4059621, -71.1316405],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;1703682&apos;,
   &apos;timestamp&apos;: &apos;2009-07-01T19:59:29Z&apos;,
   &apos;uid&apos;: &apos;140746&apos;,
   &apos;user&apos;: &apos;mbourqui&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173055&apos;,
  &apos;pos&apos;: [42.40446, -71.123482],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7198633&apos;,
   &apos;timestamp&apos;: &apos;2011-02-05T23:26:37Z&apos;,
   &apos;uid&apos;: &apos;23351&apos;,
   &apos;user&apos;: &apos;JasonWoof&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173070&apos;,
  &apos;pos&apos;: [42.401851, -71.123739],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:44Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173071&apos;,
  &apos;pos&apos;: [42.40203, -71.124326],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:44Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173078&apos;,
  &apos;pos&apos;: [42.4023559, -71.1251174],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:57:56Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173171&apos;,
  &apos;pos&apos;: [42.407433, -71.124535],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:39Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173227&apos;,
  &apos;pos&apos;: [42.407975, -71.130658],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:57:56Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173244&apos;,
  &apos;pos&apos;: [42.407977, -71.124179],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497672&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:24:30Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173250&apos;,
  &apos;pos&apos;: [42.4076803, -71.1243748],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12181505&apos;,
   &apos;timestamp&apos;: &apos;2012-07-11T03:53:02Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173299&apos;,
  &apos;pos&apos;: [42.3884255, -71.1106355],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:11:58Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173303&apos;,
  &apos;pos&apos;: [42.3887189, -71.1042902],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;21189633&apos;,
   &apos;timestamp&apos;: &apos;2014-03-19T10:38:22Z&apos;,
   &apos;uid&apos;: &apos;1670311&apos;,
   &apos;user&apos;: &apos;SophoM&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61173310&apos;,
  &apos;pos&apos;: [42.3884252, -71.1034251],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:15:24Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173323&apos;,
  &apos;pos&apos;: [42.388634, -71.106054],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:15:25Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173331&apos;,
  &apos;pos&apos;: [42.388471, -71.105592],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:11:58Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173336&apos;,
  &apos;pos&apos;: [42.3890343, -71.1052269],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32085706&apos;,
   &apos;timestamp&apos;: &apos;2015-06-19T22:56:10Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173342&apos;,
  &apos;pos&apos;: [42.3884663, -71.0853155],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32085706&apos;,
   &apos;timestamp&apos;: &apos;2015-06-19T22:56:10Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61173400&apos;,
  &apos;pos&apos;: [42.3894405, -71.0878051],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12181505&apos;,
   &apos;timestamp&apos;: &apos;2012-07-11T03:53:02Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173414&apos;,
  &apos;pos&apos;: [42.3887924, -71.1112079],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26242718&apos;,
   &apos;timestamp&apos;: &apos;2014-10-21T20:50:32Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61173421&apos;,
  &apos;pos&apos;: [42.3891296, -71.1116822],
  &apos;traffic_signals&apos;: &apos;blinker&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;25971126&apos;,
   &apos;timestamp&apos;: &apos;2014-10-09T21:51:47Z&apos;,
   &apos;uid&apos;: &apos;2389162&apos;,
   &apos;user&apos;: &apos;mapper117&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173428&apos;,
  &apos;pos&apos;: [42.3883104, -71.0962857],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26584106&apos;,
   &apos;timestamp&apos;: &apos;2014-11-06T01:47:54Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61173441&apos;,
  &apos;pos&apos;: [42.3891393, -71.097161],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:34:42Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173447&apos;,
  &apos;pos&apos;: [42.388662, -71.096658],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:44Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173484&apos;,
  &apos;pos&apos;: [42.3744, -71.099475],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2271795&apos;,
   &apos;timestamp&apos;: &apos;2009-08-26T21:14:16Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173516&apos;,
  &apos;pos&apos;: [42.374703, -71.097196],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2271795&apos;,
   &apos;timestamp&apos;: &apos;2009-08-26T21:14:17Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173519&apos;,
  &apos;pos&apos;: [42.375143, -71.096888],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3293152&apos;,
   &apos;timestamp&apos;: &apos;2009-12-05T04:43:21Z&apos;,
   &apos;uid&apos;: &apos;158555&apos;,
   &apos;user&apos;: &apos;Prithason&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173523&apos;,
  &apos;pos&apos;: [42.374429, -71.097416],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12528124&apos;,
   &apos;timestamp&apos;: &apos;2012-07-28T20:43:03Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173610&apos;,
  &apos;pos&apos;: [42.3862019, -71.1161272],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6020841&apos;,
   &apos;timestamp&apos;: &apos;2010-10-12T13:22:25Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173625&apos;,
  &apos;pos&apos;: [42.3886623, -71.112005],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;21189633&apos;,
   &apos;timestamp&apos;: &apos;2014-03-19T10:38:21Z&apos;,
   &apos;uid&apos;: &apos;1670311&apos;,
   &apos;user&apos;: &apos;SophoM&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61173631&apos;,
  &apos;pos&apos;: [42.3902058, -71.1079674],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:34:47Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173665&apos;,
  &apos;pos&apos;: [42.388265, -71.096242],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6642755&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T22:15:21Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61173691&apos;,
  &apos;pos&apos;: [42.3795465, -71.1079288],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:47:00Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173717&apos;,
  &apos;pos&apos;: [42.377698, -71.090209],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:47:01Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173724&apos;,
  &apos;pos&apos;: [42.377677, -71.090162],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:39:49Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173731&apos;,
  &apos;pos&apos;: [42.37953, -71.097427],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7681365&apos;,
   &apos;timestamp&apos;: &apos;2011-03-27T00:12:36Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173779&apos;,
  &apos;pos&apos;: [42.3815571, -71.0861986],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6692003&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T23:41:24Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173796&apos;,
  &apos;pos&apos;: [42.3874287, -71.0826636],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11694735&apos;,
   &apos;timestamp&apos;: &apos;2012-05-25T01:08:06Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;crossing&apos;,
  &apos;id&apos;: &apos;61173811&apos;,
  &apos;pos&apos;: [42.3814728, -71.0862198],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7681365&apos;,
   &apos;timestamp&apos;: &apos;2011-03-27T00:12:35Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173817&apos;,
  &apos;pos&apos;: [42.3813165, -71.0862143],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11220134&apos;,
   &apos;timestamp&apos;: &apos;2012-04-08T00:52:41Z&apos;,
   &apos;uid&apos;: &apos;54419&apos;,
   &apos;user&apos;: &apos;giovanni berlanda&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61173821&apos;,
  &apos;pos&apos;: [42.3747091, -71.0983838],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2271795&apos;,
   &apos;timestamp&apos;: &apos;2009-08-26T21:14:17Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173829&apos;,
  &apos;pos&apos;: [42.375644, -71.09654],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2273850&apos;,
   &apos;timestamp&apos;: &apos;2009-08-27T05:16:50Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173835&apos;,
  &apos;pos&apos;: [42.374429, -71.097644],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:32:20Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173863&apos;,
  &apos;pos&apos;: [42.380387, -71.089107],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:32:21Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61173886&apos;,
  &apos;pos&apos;: [42.380253, -71.089202],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6683804&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T07:00:17Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173892&apos;,
  &apos;pos&apos;: [42.3906657, -71.0824267],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T22:20:36Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173895&apos;,
  &apos;pos&apos;: [42.3943436, -71.0864769],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T22:20:36Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173901&apos;,
  &apos;pos&apos;: [42.3941343, -71.085909],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10153118&apos;,
   &apos;timestamp&apos;: &apos;2011-12-19T06:46:17Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61173940&apos;,
  &apos;pos&apos;: [42.395683, -71.115721],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:04:57Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61173953&apos;,
  &apos;pos&apos;: [42.394828, -71.116308],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T22:20:36Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61174056&apos;,
  &apos;pos&apos;: [42.3940951, -71.0858448],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6683804&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T07:00:17Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174062&apos;,
  &apos;pos&apos;: [42.393903, -71.0858704],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T22:20:36Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61174071&apos;,
  &apos;pos&apos;: [42.3943948, -71.0857758],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T22:20:36Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174078&apos;,
  &apos;pos&apos;: [42.3942186, -71.0858227],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31954058&apos;,
   &apos;timestamp&apos;: &apos;2015-06-14T02:36:30Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61174092&apos;,
  &apos;pos&apos;: [42.389832, -71.0813786],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T02:55:33Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;id&apos;: &apos;61174104&apos;,
  &apos;pos&apos;: [42.3908511, -71.0907767],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;34152985&apos;,
   &apos;timestamp&apos;: &apos;2015-09-21T03:30:12Z&apos;,
   &apos;uid&apos;: &apos;485808&apos;,
   &apos;user&apos;: &apos;Alexey Lukin&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174112&apos;,
  &apos;pos&apos;: [42.3805478, -71.0890728],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T02:55:33Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61174119&apos;,
  &apos;pos&apos;: [42.3909169, -71.090868],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T02:55:34Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61174126&apos;,
  &apos;pos&apos;: [42.3907828, -71.090667],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;19072675&apos;,
   &apos;timestamp&apos;: &apos;2013-11-23T14:45:07Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61174140&apos;,
  &apos;pos&apos;: [42.3905092, -71.0901332],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20129805&apos;,
   &apos;timestamp&apos;: &apos;2014-01-21T20:44:09Z&apos;,
   &apos;uid&apos;: &apos;163396&apos;,
   &apos;user&apos;: &apos;pokey&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174147&apos;,
  &apos;pos&apos;: [42.3803006, -71.0897497],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:32:23Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61174152&apos;,
  &apos;pos&apos;: [42.38034, -71.089631],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6683804&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T07:00:17Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174181&apos;,
  &apos;pos&apos;: [42.3936079, -71.0858838],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:02Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174205&apos;,
  &apos;pos&apos;: [42.404773, -71.117939],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:03Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174214&apos;,
  &apos;pos&apos;: [42.404755, -71.118292],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:04Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174231&apos;,
  &apos;pos&apos;: [42.405075, -71.116039],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;1716860&apos;,
   &apos;timestamp&apos;: &apos;2009-07-03T08:52:56Z&apos;,
   &apos;uid&apos;: &apos;58305&apos;,
   &apos;user&apos;: &apos;fiveisalive&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61174266&apos;,
  &apos;pos&apos;: [42.4055717, -71.1227139],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7140819&apos;,
   &apos;timestamp&apos;: &apos;2011-01-30T22:52:56Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61174274&apos;,
  &apos;pos&apos;: [42.405999, -71.1254647],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:05Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174300&apos;,
  &apos;pos&apos;: [42.405079, -71.116767],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32085706&apos;,
   &apos;timestamp&apos;: &apos;2015-06-19T22:56:10Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61174320&apos;,
  &apos;pos&apos;: [42.3900952, -71.0892431],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10771441&apos;,
   &apos;timestamp&apos;: &apos;2012-02-23T19:16:51Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61174328&apos;,
  &apos;pos&apos;: [42.3834299, -71.0915391],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T20:12:28Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;id&apos;: &apos;61174341&apos;,
  &apos;pos&apos;: [42.39881, -71.0840415],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:10:07Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174349&apos;,
  &apos;pos&apos;: [42.3837388, -71.0916954],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;15660960&apos;,
   &apos;timestamp&apos;: &apos;2013-04-09T00:54:29Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61174358&apos;,
  &apos;pos&apos;: [42.3985954, -71.0841262],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:06Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174389&apos;,
  &apos;pos&apos;: [42.40477, -71.118709],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:06Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174406&apos;,
  &apos;pos&apos;: [42.404948, -71.119577],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:42Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174434&apos;,
  &apos;pos&apos;: [42.400899, -71.119893],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:07Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61174549&apos;,
  &apos;pos&apos;: [42.406253, -71.12531],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;485479&apos;,
   &apos;timestamp&apos;: &apos;2009-02-16T14:24:13Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61174573&apos;,
  &apos;pos&apos;: [42.399858, -71.112022],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7032670&apos;,
   &apos;timestamp&apos;: &apos;2011-01-20T17:46:56Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61174601&apos;,
  &apos;pos&apos;: [42.3990326, -71.11344],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;8286916&apos;,
   &apos;timestamp&apos;: &apos;2011-05-29T22:36:54Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61174622&apos;,
  &apos;pos&apos;: [42.4016364, -71.122937],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:52:07Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174689&apos;,
  &apos;pos&apos;: [42.401712, -71.117931],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:52:07Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174692&apos;,
  &apos;pos&apos;: [42.401479, -71.117525],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:10Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174697&apos;,
  &apos;pos&apos;: [42.401985, -71.118749],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:11Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174700&apos;,
  &apos;pos&apos;: [42.40188, -71.118343],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:11Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174713&apos;,
  &apos;pos&apos;: [42.402109, -71.119249],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:42Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174721&apos;,
  &apos;pos&apos;: [42.401264, -71.121444],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:42Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174728&apos;,
  &apos;pos&apos;: [42.401096, -71.12073],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;8286916&apos;,
   &apos;timestamp&apos;: &apos;2011-05-29T22:36:54Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61174731&apos;,
  &apos;pos&apos;: [42.4014549, -71.1222189],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:12Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174743&apos;,
  &apos;pos&apos;: [42.402855, -71.120681],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:43Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61174749&apos;,
  &apos;pos&apos;: [42.401557, -71.122628],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;29934557&apos;,
   &apos;timestamp&apos;: &apos;2015-04-02T18:22:03Z&apos;,
   &apos;uid&apos;: &apos;703517&apos;,
   &apos;user&apos;: &apos;Iowa Kid&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61174766&apos;,
  &apos;pos&apos;: [42.4013714, -71.1173801],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:43Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174772&apos;,
  &apos;pos&apos;: [42.401329, -71.12175],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:08:51Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61174794&apos;,
  &apos;pos&apos;: [42.393896, -71.11442],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;5970253&apos;,
   &apos;timestamp&apos;: &apos;2010-10-06T15:19:12Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174835&apos;,
  &apos;pos&apos;: [42.3967236, -71.1064288],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;5970253&apos;,
   &apos;timestamp&apos;: &apos;2010-10-06T15:19:07Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174842&apos;,
  &apos;pos&apos;: [42.3965156, -71.1065977],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6992879&apos;,
   &apos;timestamp&apos;: &apos;2011-01-16T19:52:49Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61174939&apos;,
  &apos;pos&apos;: [42.3945836, -71.1229752],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:52:14Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61175189&apos;,
  &apos;pos&apos;: [42.397207, -71.120952],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:55:00Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61175241&apos;,
  &apos;pos&apos;: [42.397728, -71.108491],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;5970253&apos;,
   &apos;timestamp&apos;: &apos;2010-10-06T15:19:14Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61175361&apos;,
  &apos;pos&apos;: [42.3982884, -71.10733],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6619643&apos;,
   &apos;timestamp&apos;: &apos;2010-12-11T07:15:07Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61175388&apos;,
  &apos;pos&apos;: [42.37786, -71.1058476],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6619643&apos;,
   &apos;timestamp&apos;: &apos;2010-12-11T07:15:10Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61175392&apos;,
  &apos;pos&apos;: [42.3774415, -71.1053309],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6619643&apos;,
   &apos;timestamp&apos;: &apos;2010-12-11T07:15:06Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61175432&apos;,
  &apos;pos&apos;: [42.3773149, -71.1051776],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3169035&apos;,
   &apos;timestamp&apos;: &apos;2009-11-20T15:01:53Z&apos;,
   &apos;uid&apos;: &apos;175058&apos;,
   &apos;user&apos;: &apos;Tom Walsh&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61175435&apos;,
  &apos;pos&apos;: [42.379795, -71.108235],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6691095&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T21:56:15Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61175624&apos;,
  &apos;pos&apos;: [42.3879751, -71.0842396],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:46:04Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61175693&apos;,
  &apos;pos&apos;: [42.398124, -71.128264],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T21:42:01Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61175782&apos;,
  &apos;pos&apos;: [42.3984456, -71.0851848],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:08Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61175825&apos;,
  &apos;pos&apos;: [42.3984975, -71.1079708],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;5970253&apos;,
   &apos;timestamp&apos;: &apos;2010-10-06T15:19:03Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61175833&apos;,
  &apos;pos&apos;: [42.3984171, -71.1077484],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:06:11Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61175938&apos;,
  &apos;pos&apos;: [42.396535, -71.101803],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:55:08Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61175990&apos;,
  &apos;pos&apos;: [42.397175, -71.111178],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:52:29Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61176009&apos;,
  &apos;pos&apos;: [42.396757, -71.119835],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6993097&apos;,
   &apos;timestamp&apos;: &apos;2011-01-16T20:09:40Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61176069&apos;,
  &apos;pos&apos;: [42.3969433, -71.1244841],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T21:37:27Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61176107&apos;,
  &apos;pos&apos;: [42.3977464, -71.0861113],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T21:25:06Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61176115&apos;,
  &apos;pos&apos;: [42.3973203, -71.0866928],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:55:09Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61176169&apos;,
  &apos;pos&apos;: [42.397775, -71.105706],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6993097&apos;,
   &apos;timestamp&apos;: &apos;2011-01-16T20:09:40Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61176182&apos;,
  &apos;pos&apos;: [42.396402, -71.1232508],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6993097&apos;,
   &apos;timestamp&apos;: &apos;2011-01-16T20:09:37Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61176207&apos;,
  &apos;pos&apos;: [42.3960101, -71.1260639],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T21:09:39Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61176216&apos;,
  &apos;pos&apos;: [42.3968946, -71.0872719],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T21:09:39Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61176225&apos;,
  &apos;pos&apos;: [42.3964714, -71.0878499],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:55:10Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61176231&apos;,
  &apos;pos&apos;: [42.397693, -71.110035],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32032153&apos;,
   &apos;timestamp&apos;: &apos;2015-06-17T15:49:10Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61176237&apos;,
  &apos;pos&apos;: [42.3960809, -71.084834],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32061008&apos;,
   &apos;timestamp&apos;: &apos;2015-06-18T22:41:06Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61176284&apos;,
  &apos;pos&apos;: [42.395731, -71.0849639],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10153118&apos;,
   &apos;timestamp&apos;: &apos;2011-12-19T06:46:18Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61176290&apos;,
  &apos;pos&apos;: [42.396045, -71.116633],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:05:05Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61176300&apos;,
  &apos;pos&apos;: [42.395856, -71.115602],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:52:36Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61176304&apos;,
  &apos;pos&apos;: [42.396283, -71.115309],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;21189633&apos;,
   &apos;timestamp&apos;: &apos;2014-03-19T10:38:21Z&apos;,
   &apos;uid&apos;: &apos;1670311&apos;,
   &apos;user&apos;: &apos;SophoM&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61176326&apos;,
  &apos;pos&apos;: [42.396489, -71.122309],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:55:12Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61176356&apos;,
  &apos;pos&apos;: [42.397172, -71.110385],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6993097&apos;,
   &apos;timestamp&apos;: &apos;2011-01-16T20:09:36Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61176365&apos;,
  &apos;pos&apos;: [42.3961786, -71.1257937],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6993097&apos;,
   &apos;timestamp&apos;: &apos;2011-01-16T20:09:39Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61176460&apos;,
  &apos;pos&apos;: [42.396488, -71.1252682],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6582595&apos;,
   &apos;timestamp&apos;: &apos;2010-12-08T08:16:26Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61176647&apos;,
  &apos;pos&apos;: [42.3791651, -71.102802],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26653037&apos;,
   &apos;timestamp&apos;: &apos;2014-11-08T22:26:23Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61176726&apos;,
  &apos;pos&apos;: [42.3889969, -71.0867769],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6690197&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T20:07:24Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61176737&apos;,
  &apos;pos&apos;: [42.3893527, -71.0875979],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6690197&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T20:07:25Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61176744&apos;,
  &apos;pos&apos;: [42.3892621, -71.0873831],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:52:39Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61177197&apos;,
  &apos;pos&apos;: [42.3863502, -71.0899106],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:05:07Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61177224&apos;,
  &apos;pos&apos;: [42.3955902, -71.1169447],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;5970253&apos;,
   &apos;timestamp&apos;: &apos;2010-10-06T15:19:15Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61177234&apos;,
  &apos;pos&apos;: [42.3961254, -71.106874],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6995552&apos;,
   &apos;timestamp&apos;: &apos;2011-01-17T00:53:10Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61177298&apos;,
  &apos;pos&apos;: [42.3890947, -71.1021167],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6995552&apos;,
   &apos;timestamp&apos;: &apos;2011-01-17T00:53:11Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61177308&apos;,
  &apos;pos&apos;: [42.3888438, -71.102282],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7678578&apos;,
   &apos;timestamp&apos;: &apos;2011-03-26T18:24:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61177497&apos;,
  &apos;pos&apos;: [42.3815195, -71.0849675],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:34:55Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61177514&apos;,
  &apos;pos&apos;: [42.388722, -71.101302],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:32:41Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61177546&apos;,
  &apos;pos&apos;: [42.38369, -71.084823],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7678578&apos;,
   &apos;timestamp&apos;: &apos;2011-03-26T18:24:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61177566&apos;,
  &apos;pos&apos;: [42.3831336, -71.0851763],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6932046&apos;,
   &apos;timestamp&apos;: &apos;2011-01-10T22:26:58Z&apos;,
   &apos;uid&apos;: &apos;23351&apos;,
   &apos;user&apos;: &apos;JasonWoof&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61177577&apos;,
  &apos;pos&apos;: [42.3811601, -71.0994829],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:10:07Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61177586&apos;,
  &apos;pos&apos;: [42.3837932, -71.0918048],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702541&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:22:28Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61177606&apos;,
  &apos;pos&apos;: [42.384095, -71.0921013],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:10:07Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61177615&apos;,
  &apos;pos&apos;: [42.383856, -71.0918878],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:52:44Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61177661&apos;,
  &apos;pos&apos;: [42.397219, -71.124596],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:52:45Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61177663&apos;,
  &apos;pos&apos;: [42.397542, -71.124692],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:52:46Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61177664&apos;,
  &apos;pos&apos;: [42.39746, -71.124694],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:55:14Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61177666&apos;,
  &apos;pos&apos;: [42.397382, -71.105949],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:52:47Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61177667&apos;,
  &apos;pos&apos;: [42.397187, -71.114689],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:52:47Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61177668&apos;,
  &apos;pos&apos;: [42.39686, -71.114913],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:52:49Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61177677&apos;,
  &apos;pos&apos;: [42.397662, -71.124635],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:55:15Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61177681&apos;,
  &apos;pos&apos;: [42.397178, -71.112091],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3169035&apos;,
   &apos;timestamp&apos;: &apos;2009-11-20T15:01:46Z&apos;,
   &apos;uid&apos;: &apos;175058&apos;,
   &apos;user&apos;: &apos;Tom Walsh&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61177808&apos;,
  &apos;pos&apos;: [42.37478, -71.102106],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632518&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T06:18:55Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61177816&apos;,
  &apos;pos&apos;: [42.3744236, -71.1016653],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:50:55Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61177968&apos;,
  &apos;pos&apos;: [42.3897926, -71.1171573],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:51:02Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61177979&apos;,
  &apos;pos&apos;: [42.3883482, -71.115787],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16209538&apos;,
   &apos;timestamp&apos;: &apos;2013-05-20T14:27:24Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61178062&apos;,
  &apos;pos&apos;: [42.3915703, -71.1190933],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632518&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T06:18:58Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61178078&apos;,
  &apos;pos&apos;: [42.3743694, -71.1015958],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:50:55Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61178149&apos;,
  &apos;pos&apos;: [42.3902704, -71.1176506],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:11:46Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61178171&apos;,
  &apos;pos&apos;: [42.390561, -71.117952],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:50:52Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61178192&apos;,
  &apos;pos&apos;: [42.3896304, -71.1169904],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32061008&apos;,
   &apos;timestamp&apos;: &apos;2015-06-18T22:51:55Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61178404&apos;,
  &apos;pos&apos;: [42.3948724, -71.0853172],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32061008&apos;,
   &apos;timestamp&apos;: &apos;2015-06-18T22:51:55Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61178412&apos;,
  &apos;pos&apos;: [42.3943518, -71.0854574],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6699154&apos;,
   &apos;timestamp&apos;: &apos;2010-12-18T19:47:37Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61178429&apos;,
  &apos;pos&apos;: [42.3916733, -71.0832819],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32061008&apos;,
   &apos;timestamp&apos;: &apos;2015-06-18T22:51:55Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61178454&apos;,
  &apos;pos&apos;: [42.393972, -71.0855342],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6582595&apos;,
   &apos;timestamp&apos;: &apos;2010-12-08T08:16:21Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61178650&apos;,
  &apos;pos&apos;: [42.3793412, -71.099292],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6582595&apos;,
   &apos;timestamp&apos;: &apos;2010-12-08T08:16:34Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61178652&apos;,
  &apos;pos&apos;: [42.3793292, -71.0994631],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13435916&apos;,
   &apos;timestamp&apos;: &apos;2012-10-10T03:18:08Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61178654&apos;,
  &apos;pos&apos;: [42.3793259, -71.0996786],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6582595&apos;,
   &apos;timestamp&apos;: &apos;2010-12-08T08:16:25Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61178663&apos;,
  &apos;pos&apos;: [42.3793891, -71.0988672],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:15:38Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61178771&apos;,
  &apos;pos&apos;: [42.386001, -71.108583],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:15:39Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61178778&apos;,
  &apos;pos&apos;: [42.385378, -71.108999],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:15:39Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61178794&apos;,
  &apos;pos&apos;: [42.386412, -71.108319],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:16:01Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61178806&apos;,
  &apos;pos&apos;: [42.385001, -71.108785],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11109635&apos;,
   &apos;timestamp&apos;: &apos;2012-03-26T19:28:56Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61178852&apos;,
  &apos;pos&apos;: [42.3856914, -71.0833816],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:40:00Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61178858&apos;,
  &apos;pos&apos;: [42.385309, -71.083676],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7681666&apos;,
   &apos;timestamp&apos;: &apos;2011-03-27T01:55:50Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61178875&apos;,
  &apos;pos&apos;: [42.3821495, -71.0808776],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7681666&apos;,
   &apos;timestamp&apos;: &apos;2011-03-27T01:55:50Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61178885&apos;,
  &apos;pos&apos;: [42.3821785, -71.0806813],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31954058&apos;,
   &apos;timestamp&apos;: &apos;2015-06-14T03:03:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61178890&apos;,
  &apos;pos&apos;: [42.3871951, -71.0779029],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;862336&apos;,
   &apos;timestamp&apos;: &apos;2009-03-26T14:27:20Z&apos;,
   &apos;uid&apos;: &apos;110489&apos;,
   &apos;user&apos;: &apos;Pouletic&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61178893&apos;,
  &apos;pos&apos;: [42.373768, -71.087647],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;862336&apos;,
   &apos;timestamp&apos;: &apos;2009-03-26T14:27:20Z&apos;,
   &apos;uid&apos;: &apos;110489&apos;,
   &apos;user&apos;: &apos;Pouletic&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61178897&apos;,
  &apos;pos&apos;: [42.373276, -71.086987],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:05Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61178932&apos;,
  &apos;pos&apos;: [42.3970738, -71.1089473],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6868742&apos;,
   &apos;timestamp&apos;: &apos;2011-01-05T06:59:08Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61178942&apos;,
  &apos;pos&apos;: [42.397296, -71.1087945],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T22:20:36Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61178946&apos;,
  &apos;pos&apos;: [42.39466, -71.0875618],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T22:20:36Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61179010&apos;,
  &apos;pos&apos;: [42.394737, -71.0877703],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:34:57Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61179068&apos;,
  &apos;pos&apos;: [42.388176, -71.102696],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:12:25Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61179105&apos;,
  &apos;pos&apos;: [42.384956, -71.114613],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:34:58Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61179114&apos;,
  &apos;pos&apos;: [42.388288, -71.101637],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6120857&apos;,
   &apos;timestamp&apos;: &apos;2010-10-20T23:37:19Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179128&apos;,
  &apos;pos&apos;: [42.3993875, -71.1106062],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6120857&apos;,
   &apos;timestamp&apos;: &apos;2010-10-20T23:37:25Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179131&apos;,
  &apos;pos&apos;: [42.3992236, -71.1101272],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6120857&apos;,
   &apos;timestamp&apos;: &apos;2010-10-20T23:37:20Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179151&apos;,
  &apos;pos&apos;: [42.3993278, -71.1104419],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:11:49Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61179152&apos;,
  &apos;pos&apos;: [42.386875, -71.115188],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12181505&apos;,
   &apos;timestamp&apos;: &apos;2012-07-11T03:53:01Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179342&apos;,
  &apos;pos&apos;: [42.3872158, -71.1085021],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12181505&apos;,
   &apos;timestamp&apos;: &apos;2012-07-11T03:53:01Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179350&apos;,
  &apos;pos&apos;: [42.3870013, -71.1079417],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6692003&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T23:41:24Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179360&apos;,
  &apos;pos&apos;: [42.3868039, -71.0805685],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845995&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T03:36:10Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179364&apos;,
  &apos;pos&apos;: [42.3959902, -71.1222568],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:39:01Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61179450&apos;,
  &apos;pos&apos;: [42.403451, -71.12762],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6008217&apos;,
   &apos;timestamp&apos;: &apos;2010-10-11T02:29:53Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61179493&apos;,
  &apos;pos&apos;: [42.3779598, -71.0948845],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6008217&apos;,
   &apos;timestamp&apos;: &apos;2010-10-11T02:29:53Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61179497&apos;,
  &apos;pos&apos;: [42.3772525, -71.0953754],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6582595&apos;,
   &apos;timestamp&apos;: &apos;2010-12-08T08:16:32Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179527&apos;,
  &apos;pos&apos;: [42.3794121, -71.0986389],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13435407&apos;,
   &apos;timestamp&apos;: &apos;2012-10-10T02:03:51Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61179530&apos;,
  &apos;pos&apos;: [42.3776568, -71.0957955],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6582595&apos;,
   &apos;timestamp&apos;: &apos;2010-12-08T08:16:21Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179539&apos;,
  &apos;pos&apos;: [42.3794342, -71.0984362],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6582595&apos;,
   &apos;timestamp&apos;: &apos;2010-12-08T08:16:39Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179549&apos;,
  &apos;pos&apos;: [42.3794264, -71.0985079],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6664722&apos;,
   &apos;timestamp&apos;: &apos;2010-12-15T05:57:24Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179595&apos;,
  &apos;pos&apos;: [42.3815145, -71.1005265],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:44Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179615&apos;,
  &apos;pos&apos;: [42.407433, -71.130385],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:39:02Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61179616&apos;,
  &apos;pos&apos;: [42.404375, -71.12919],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:44Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179623&apos;,
  &apos;pos&apos;: [42.407885, -71.130644],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32032153&apos;,
   &apos;timestamp&apos;: &apos;2015-06-17T15:49:10Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179671&apos;,
  &apos;pos&apos;: [42.3963223, -71.0844998],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T23:11:20Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61179676&apos;,
  &apos;pos&apos;: [42.3980499, -71.0844077],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T23:11:20Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179680&apos;,
  &apos;pos&apos;: [42.3983522, -71.0842576],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32032153&apos;,
   &apos;timestamp&apos;: &apos;2015-06-17T15:49:10Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61179686&apos;,
  &apos;pos&apos;: [42.3961361, -71.0841063],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32032153&apos;,
   &apos;timestamp&apos;: &apos;2015-06-17T15:49:10Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179690&apos;,
  &apos;pos&apos;: [42.3962364, -71.0842035],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32032153&apos;,
   &apos;timestamp&apos;: &apos;2015-06-17T15:49:10Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61179693&apos;,
  &apos;pos&apos;: [42.3962816, -71.0846089],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:15:49Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61179788&apos;,
  &apos;pos&apos;: [42.388245, -71.104938],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:15:49Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61179790&apos;,
  &apos;pos&apos;: [42.387918, -71.103973],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:15:50Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61179792&apos;,
  &apos;pos&apos;: [42.386422, -71.106248],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:15:51Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61179795&apos;,
  &apos;pos&apos;: [42.386176, -71.105526],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12181505&apos;,
   &apos;timestamp&apos;: &apos;2012-07-11T03:53:02Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179805&apos;,
  &apos;pos&apos;: [42.3866153, -71.10681],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:44Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179809&apos;,
  &apos;pos&apos;: [42.3740926, -71.0914592],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:44Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179829&apos;,
  &apos;pos&apos;: [42.3740423, -71.0908357],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:44Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179834&apos;,
  &apos;pos&apos;: [42.3753113, -71.0907408],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:44Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61179835&apos;,
  &apos;pos&apos;: [42.3750365, -71.0907987],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:44Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61179836&apos;,
  &apos;pos&apos;: [42.3745854, -71.0908896],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:44Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179839&apos;,
  &apos;pos&apos;: [42.374438, -71.0908246],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:44Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179840&apos;,
  &apos;pos&apos;: [42.3745676, -71.0912951],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:45Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61179842&apos;,
  &apos;pos&apos;: [42.3743977, -71.0913945],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632518&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T06:19:10Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179869&apos;,
  &apos;pos&apos;: [42.3763548, -71.1004828],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632518&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T06:19:00Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179870&apos;,
  &apos;pos&apos;: [42.3762702, -71.1006778],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6591204&apos;,
   &apos;timestamp&apos;: &apos;2010-12-09T00:28:34Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179871&apos;,
  &apos;pos&apos;: [42.3760861, -71.101058],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632518&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T06:19:19Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179872&apos;,
  &apos;pos&apos;: [42.3763812, -71.1003816],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632518&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T06:18:53Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179876&apos;,
  &apos;pos&apos;: [42.3761304, -71.1009841],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:13Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179884&apos;,
  &apos;pos&apos;: [42.405944, -71.122267],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:14Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179886&apos;,
  &apos;pos&apos;: [42.406724, -71.12192],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:14Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179888&apos;,
  &apos;pos&apos;: [42.406303, -71.122223],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12135181&apos;,
   &apos;timestamp&apos;: &apos;2012-07-06T21:44:57Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;crossing&apos;,
  &apos;id&apos;: &apos;61179910&apos;,
  &apos;pos&apos;: [42.3818319, -71.0980802],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12135181&apos;,
   &apos;timestamp&apos;: &apos;2012-07-06T21:44:57Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179916&apos;,
  &apos;pos&apos;: [42.3817115, -71.0981803],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12135181&apos;,
   &apos;timestamp&apos;: &apos;2012-07-06T21:44:58Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61179920&apos;,
  &apos;pos&apos;: [42.3817816, -71.0980925],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179996&apos;,
  &apos;pos&apos;: [42.379519, -71.0937988],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61179998&apos;,
  &apos;pos&apos;: [42.3794665, -71.0938516],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180003&apos;,
  &apos;pos&apos;: [42.3795426, -71.0937138],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6670798&apos;,
   &apos;timestamp&apos;: &apos;2010-12-15T19:40:56Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;crossing&apos;: &apos;traffic_signals&apos;,
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61180006&apos;,
  &apos;pos&apos;: [42.3790987, -71.0941056],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61180008&apos;,
  &apos;pos&apos;: [42.3796391, -71.0949283],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:35:06Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180152&apos;,
  &apos;pos&apos;: [42.389884, -71.097952],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12899968&apos;,
   &apos;timestamp&apos;: &apos;2012-08-29T02:16:01Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180160&apos;,
  &apos;pos&apos;: [42.3756576, -71.0848521],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;21637560&apos;,
   &apos;timestamp&apos;: &apos;2014-04-12T00:08:35Z&apos;,
   &apos;uid&apos;: &apos;837425&apos;,
   &apos;user&apos;: &apos;Jonathan ZHAO&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61180161&apos;,
  &apos;pos&apos;: [42.3755328, -71.0850779],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12899968&apos;,
   &apos;timestamp&apos;: &apos;2012-08-29T02:16:01Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180162&apos;,
  &apos;pos&apos;: [42.3755026, -71.0851506],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12899968&apos;,
   &apos;timestamp&apos;: &apos;2012-08-29T02:16:02Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180167&apos;,
  &apos;pos&apos;: [42.3755254, -71.0852161],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180237&apos;,
  &apos;pos&apos;: [42.3794973, -71.0930609],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13435882&apos;,
   &apos;timestamp&apos;: &apos;2012-10-10T03:08:59Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61180240&apos;,
  &apos;pos&apos;: [42.3795809, -71.0939834],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32061008&apos;,
   &apos;timestamp&apos;: &apos;2015-06-18T22:07:52Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180296&apos;,
  &apos;pos&apos;: [42.3917136, -71.0827274],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32061008&apos;,
   &apos;timestamp&apos;: &apos;2015-06-18T22:07:52Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61180297&apos;,
  &apos;pos&apos;: [42.3920154, -71.0828539],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32061008&apos;,
   &apos;timestamp&apos;: &apos;2015-06-18T22:41:05Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61180298&apos;,
  &apos;pos&apos;: [42.3937884, -71.0833623],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:05:17Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180316&apos;,
  &apos;pos&apos;: [42.392764, -71.122175],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:15Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180326&apos;,
  &apos;pos&apos;: [42.405833, -71.117425],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:51:02Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180349&apos;,
  &apos;pos&apos;: [42.3931591, -71.1204874],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:23:31Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180365&apos;,
  &apos;pos&apos;: [42.392006, -71.097239],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;21699861&apos;,
   &apos;timestamp&apos;: &apos;2014-04-14T23:55:58Z&apos;,
   &apos;uid&apos;: &apos;2031562&apos;,
   &apos;user&apos;: &apos;lckr&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61180371&apos;,
  &apos;pos&apos;: [42.38197, -71.110932],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:51:02Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180373&apos;,
  &apos;pos&apos;: [42.3927717, -71.1202116],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:23:33Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180386&apos;,
  &apos;pos&apos;: [42.392812, -71.096817],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:57:58Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180463&apos;,
  &apos;pos&apos;: [42.408931, -71.123537],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:57:59Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180522&apos;,
  &apos;pos&apos;: [42.409192, -71.12336],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:15Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180527&apos;,
  &apos;pos&apos;: [42.403893, -71.122235],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:16Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180543&apos;,
  &apos;pos&apos;: [42.404058, -71.122569],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:39:12Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180574&apos;,
  &apos;pos&apos;: [42.405623, -71.130943],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:39:12Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180575&apos;,
  &apos;pos&apos;: [42.403877, -71.128488],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:39:14Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180587&apos;,
  &apos;pos&apos;: [42.403914, -71.12854],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:16Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180588&apos;,
  &apos;pos&apos;: [42.403637, -71.121716],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7140801&apos;,
   &apos;timestamp&apos;: &apos;2011-01-30T22:50:43Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180589&apos;,
  &apos;pos&apos;: [42.4036892, -71.1281255],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:39:16Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180596&apos;,
  &apos;pos&apos;: [42.405539, -71.126041],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:39:18Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180608&apos;,
  &apos;pos&apos;: [42.405516, -71.130706],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:17Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180611&apos;,
  &apos;pos&apos;: [42.405561, -71.118131],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:18Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180614&apos;,
  &apos;pos&apos;: [42.405554, -71.118282],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;15683292&apos;,
   &apos;timestamp&apos;: &apos;2013-04-10T21:40:43Z&apos;,
   &apos;uid&apos;: &apos;28705&apos;,
   &apos;user&apos;: &apos;marnen&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61180630&apos;,
  &apos;pos&apos;: [42.4058186, -71.1313322],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:18Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180631&apos;,
  &apos;pos&apos;: [42.405881, -71.119637],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:19Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180634&apos;,
  &apos;pos&apos;: [42.405663, -71.119102],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:45Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180725&apos;,
  &apos;pos&apos;: [42.402638, -71.125749],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:42Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180728&apos;,
  &apos;pos&apos;: [42.40091, -71.119958],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:20Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180738&apos;,
  &apos;pos&apos;: [42.402877, -71.121713],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:21Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180746&apos;,
  &apos;pos&apos;: [42.40341, -71.121346],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:55:29Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180752&apos;,
  &apos;pos&apos;: [42.397151, -71.104238],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:55:29Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180753&apos;,
  &apos;pos&apos;: [42.396898, -71.104047],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:40:43Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180799&apos;,
  &apos;pos&apos;: [42.374337, -71.094762],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:40:44Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61180800&apos;,
  &apos;pos&apos;: [42.374302, -71.094752],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6642755&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T22:15:53Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61180812&apos;,
  &apos;pos&apos;: [42.3780823, -71.1072517],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6642755&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T22:15:13Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180813&apos;,
  &apos;pos&apos;: [42.3781367, -71.1070016],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16591452&apos;,
   &apos;timestamp&apos;: &apos;2013-06-17T15:52:03Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180825&apos;,
  &apos;pos&apos;: [42.4084619, -71.123845],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T11:08:42Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180874&apos;,
  &apos;pos&apos;: [42.373519, -71.084655],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13877136&apos;,
   &apos;timestamp&apos;: &apos;2012-11-14T21:35:36Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61180879&apos;,
  &apos;pos&apos;: [42.3734304, -71.0832214],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13877136&apos;,
   &apos;timestamp&apos;: &apos;2012-11-14T21:35:36Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61180881&apos;,
  &apos;pos&apos;: [42.3742483, -71.0850273],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13877136&apos;,
   &apos;timestamp&apos;: &apos;2012-11-14T21:35:36Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61180885&apos;,
  &apos;pos&apos;: [42.374305, -71.085252],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13877136&apos;,
   &apos;timestamp&apos;: &apos;2012-11-14T21:35:36Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61180887&apos;,
  &apos;pos&apos;: [42.3742938, -71.0851397],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632518&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T06:19:32Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180909&apos;,
  &apos;pos&apos;: [42.3759957, -71.1024885],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13877136&apos;,
   &apos;timestamp&apos;: &apos;2012-11-14T21:35:36Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180910&apos;,
  &apos;pos&apos;: [42.3737547, -71.0824481],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13877136&apos;,
   &apos;timestamp&apos;: &apos;2012-11-14T21:35:36Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180912&apos;,
  &apos;pos&apos;: [42.3737013, -71.0824186],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13877136&apos;,
   &apos;timestamp&apos;: &apos;2012-11-14T21:35:36Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180914&apos;,
  &apos;pos&apos;: [42.3736014, -71.0824239],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13877136&apos;,
   &apos;timestamp&apos;: &apos;2012-11-14T21:35:36Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180916&apos;,
  &apos;pos&apos;: [42.3734784, -71.0824806],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16591452&apos;,
   &apos;timestamp&apos;: &apos;2013-06-17T15:55:12Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61180953&apos;,
  &apos;pos&apos;: [42.4008592, -71.1173226],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:42Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180960&apos;,
  &apos;pos&apos;: [42.4008, -71.119089],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:41Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180968&apos;,
  &apos;pos&apos;: [42.400794, -71.118762],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:42Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180972&apos;,
  &apos;pos&apos;: [42.400845, -71.119576],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2497741&apos;,
   &apos;timestamp&apos;: &apos;2009-09-15T23:38:38Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61180974&apos;,
  &apos;pos&apos;: [42.400824, -71.118084],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7032701&apos;,
   &apos;timestamp&apos;: &apos;2011-01-20T17:50:38Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61180980&apos;,
  &apos;pos&apos;: [42.4007977, -71.1190124],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16591452&apos;,
   &apos;timestamp&apos;: &apos;2013-06-17T15:55:12Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61180991&apos;,
  &apos;pos&apos;: [42.4008783, -71.115079],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16591452&apos;,
   &apos;timestamp&apos;: &apos;2013-06-17T15:55:12Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61181027&apos;,
  &apos;pos&apos;: [42.4010395, -71.1158185],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;16591452&apos;,
   &apos;timestamp&apos;: &apos;2013-06-17T15:55:12Z&apos;,
   &apos;uid&apos;: &apos;104962&apos;,
   &apos;user&apos;: &apos;techlady&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61181029&apos;,
  &apos;pos&apos;: [42.4010224, -71.1155681],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6589476&apos;,
   &apos;timestamp&apos;: &apos;2010-12-08T21:10:45Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61181038&apos;,
  &apos;pos&apos;: [42.3811572, -71.102281],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;442758&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T03:51:59Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181046&apos;,
  &apos;pos&apos;: [42.408488, -71.131024],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;9652599&apos;,
   &apos;timestamp&apos;: &apos;2011-10-25T14:12:43Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61181081&apos;,
  &apos;pos&apos;: [42.4090692, -71.130589],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;9652599&apos;,
   &apos;timestamp&apos;: &apos;2011-10-25T14:12:43Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61181083&apos;,
  &apos;pos&apos;: [42.4090488, -71.1304874],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:45Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61181091&apos;,
  &apos;pos&apos;: [42.3757277, -71.0927359],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13877136&apos;,
   &apos;timestamp&apos;: &apos;2012-11-14T21:35:36Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61181099&apos;,
  &apos;pos&apos;: [42.3740554, -71.0858023],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13877136&apos;,
   &apos;timestamp&apos;: &apos;2012-11-14T21:35:37Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61181103&apos;,
  &apos;pos&apos;: [42.3742077, -71.0856194],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;13877136&apos;,
   &apos;timestamp&apos;: &apos;2012-11-14T21:35:37Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61181105&apos;,
  &apos;pos&apos;: [42.3741468, -71.0857118],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:11:53Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181175&apos;,
  &apos;pos&apos;: [42.385734, -71.115572],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:11:53Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181179&apos;,
  &apos;pos&apos;: [42.385806, -71.115663],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:45Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61181192&apos;,
  &apos;pos&apos;: [42.3742084, -71.0928475],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:45Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61181205&apos;,
  &apos;pos&apos;: [42.3746177, -71.092968],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:45Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61181207&apos;,
  &apos;pos&apos;: [42.3745627, -71.0929695],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:45Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61181210&apos;,
  &apos;pos&apos;: [42.3743371, -71.0928573],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:45Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61181213&apos;,
  &apos;pos&apos;: [42.3742313, -71.0928431],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:45Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61181225&apos;,
  &apos;pos&apos;: [42.3751272, -71.0928585],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:45Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61181228&apos;,
  &apos;pos&apos;: [42.3749471, -71.092913],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:52:38Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61181237&apos;,
  &apos;pos&apos;: [42.3835648, -71.0863964],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702541&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:22:27Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61181240&apos;,
  &apos;pos&apos;: [42.3843005, -71.0921681],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632151&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T03:34:03Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61181257&apos;,
  &apos;pos&apos;: [42.3794039, -71.1014146],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:41:08Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181278&apos;,
  &apos;pos&apos;: [42.37645, -71.095401],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T02:55:33Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61181281&apos;,
  &apos;pos&apos;: [42.3902204, -71.0891154],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T02:55:33Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61181283&apos;,
  &apos;pos&apos;: [42.3903433, -71.0893679],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632151&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T03:34:12Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61181406&apos;,
  &apos;pos&apos;: [42.3765674, -71.09886],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632151&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T03:33:44Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61181410&apos;,
  &apos;pos&apos;: [42.37659, -71.0985836],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T03:37:54Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61181457&apos;,
  &apos;pos&apos;: [42.3868189, -71.0914082],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:05:22Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181518&apos;,
  &apos;pos&apos;: [42.39188, -71.118358],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32061008&apos;,
   &apos;timestamp&apos;: &apos;2015-06-18T22:07:52Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61181528&apos;,
  &apos;pos&apos;: [42.3905291, -71.082278],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:05:23Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181529&apos;,
  &apos;pos&apos;: [42.391365, -71.116064],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:05:24Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181530&apos;,
  &apos;pos&apos;: [42.390937, -71.116358],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:23:39Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181542&apos;,
  &apos;pos&apos;: [42.391575, -71.099214],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:23:41Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181563&apos;,
  &apos;pos&apos;: [42.391828, -71.099023],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:11:57Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181574&apos;,
  &apos;pos&apos;: [42.390545, -71.116623],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:11:58Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181588&apos;,
  &apos;pos&apos;: [42.390146, -71.116905],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:05:27Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181648&apos;,
  &apos;pos&apos;: [42.392378, -71.122987],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T02:55:33Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61181745&apos;,
  &apos;pos&apos;: [42.3956699, -71.0995624],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:23:48Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181770&apos;,
  &apos;pos&apos;: [42.393585, -71.101439],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12146044&apos;,
   &apos;timestamp&apos;: &apos;2012-07-08T05:10:07Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61181773&apos;,
  &apos;pos&apos;: [42.3933684, -71.1148402],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2255197&apos;,
   &apos;timestamp&apos;: &apos;2009-08-25T12:30:04Z&apos;,
   &apos;uid&apos;: &apos;38786&apos;,
   &apos;user&apos;: &apos;Ian McIntosh&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61181790&apos;,
  &apos;pos&apos;: [42.3935444, -71.1180764],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:05:31Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181794&apos;,
  &apos;pos&apos;: [42.393437, -71.119034],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6845888&apos;,
   &apos;timestamp&apos;: &apos;2011-01-03T02:51:03Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61181798&apos;,
  &apos;pos&apos;: [42.3937303, -71.1208232],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:23:51Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181864&apos;,
  &apos;pos&apos;: [42.393285, -71.101188],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:05:33Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181890&apos;,
  &apos;pos&apos;: [42.394634, -71.125223],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:23:54Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181929&apos;,
  &apos;pos&apos;: [42.395985, -71.100331],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6993097&apos;,
   &apos;timestamp&apos;: &apos;2011-01-16T20:09:36Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61181950&apos;,
  &apos;pos&apos;: [42.3968787, -71.1234731],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T08:16:13Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61181963&apos;,
  &apos;pos&apos;: [42.381911, -71.110844],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6020841&apos;,
   &apos;timestamp&apos;: &apos;2010-10-12T13:22:27Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182026&apos;,
  &apos;pos&apos;: [42.3882682, -71.1122796],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;8287182&apos;,
   &apos;timestamp&apos;: &apos;2011-05-29T23:12:55Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182035&apos;,
  &apos;pos&apos;: [42.3969708, -71.1031762],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:55:32Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182040&apos;,
  &apos;pos&apos;: [42.397149, -71.103717],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:55:33Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182041&apos;,
  &apos;pos&apos;: [42.397116, -71.103608],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:06:22Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182042&apos;,
  &apos;pos&apos;: [42.396334, -71.101187],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:46:12Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182045&apos;,
  &apos;pos&apos;: [42.397096, -71.127361],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:10:06Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182171&apos;,
  &apos;pos&apos;: [42.383935, -71.0917998],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:10:06Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182172&apos;,
  &apos;pos&apos;: [42.3840602, -71.0919309],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31992277&apos;,
   &apos;timestamp&apos;: &apos;2015-06-15T20:12:28Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61182184&apos;,
  &apos;pos&apos;: [42.398774, -71.083873],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12307546&apos;,
   &apos;timestamp&apos;: &apos;2012-07-19T04:01:42Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61182194&apos;,
  &apos;pos&apos;: [42.3789027, -71.0935689],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6702293&apos;,
   &apos;timestamp&apos;: &apos;2010-12-19T04:10:06Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182212&apos;,
  &apos;pos&apos;: [42.3838667, -71.09169],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632151&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T03:33:55Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61182293&apos;,
  &apos;pos&apos;: [42.3794374, -71.1007815],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;457421&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T17:26:02Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61182294&apos;,
  &apos;pos&apos;: [42.378486, -71.096054],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6591204&apos;,
   &apos;timestamp&apos;: &apos;2010-12-09T00:28:34Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182300&apos;,
  &apos;pos&apos;: [42.3792882, -71.1021484],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T11:08:56Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182303&apos;,
  &apos;pos&apos;: [42.373517, -71.087911],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T11:08:57Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182307&apos;,
  &apos;pos&apos;: [42.373499, -71.087917],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6993097&apos;,
   &apos;timestamp&apos;: &apos;2011-01-16T20:09:38Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182308&apos;,
  &apos;pos&apos;: [42.3959226, -71.1262188],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:41:40Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182315&apos;,
  &apos;pos&apos;: [42.37944, -71.101078],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6632151&apos;,
   &apos;timestamp&apos;: &apos;2010-12-12T03:34:12Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182317&apos;,
  &apos;pos&apos;: [42.379425, -71.1004818],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:41:42Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182318&apos;,
  &apos;pos&apos;: [42.379358, -71.101717],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:41:43Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182322&apos;,
  &apos;pos&apos;: [42.37923, -71.102496],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61182324&apos;,
  &apos;pos&apos;: [42.3796317, -71.0955674],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:45Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61182325&apos;,
  &apos;pos&apos;: [42.3742732, -71.0895646],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:46Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61182339&apos;,
  &apos;pos&apos;: [42.3739992, -71.0903078],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:46Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61182344&apos;,
  &apos;pos&apos;: [42.3741247, -71.0882669],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:46Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61182353&apos;,
  &apos;pos&apos;: [42.3741502, -71.0885041],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:46Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61182360&apos;,
  &apos;pos&apos;: [42.3741563, -71.0880606],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T11:09:03Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61182366&apos;,
  &apos;pos&apos;: [42.373632, -71.087835],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T11:09:03Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182370&apos;,
  &apos;pos&apos;: [42.37367, -71.088628],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:22Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182393&apos;,
  &apos;pos&apos;: [42.405181, -71.115643],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;11238608&apos;,
   &apos;timestamp&apos;: &apos;2012-04-09T13:42:46Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61182407&apos;,
  &apos;pos&apos;: [42.3744967, -71.0882066],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;12135181&apos;,
   &apos;timestamp&apos;: &apos;2012-07-06T21:44:58Z&apos;,
   &apos;uid&apos;: &apos;256900&apos;,
   &apos;user&apos;: &apos;probiscus&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;crossing&apos;,
  &apos;id&apos;: &apos;61182441&apos;,
  &apos;pos&apos;: [42.3817474, -71.0978509],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32171768&apos;,
   &apos;timestamp&apos;: &apos;2015-06-23T23:25:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61182503&apos;,
  &apos;pos&apos;: [42.3811254, -71.0870222],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:33:31Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182511&apos;,
  &apos;pos&apos;: [42.381193, -71.086744],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6582595&apos;,
   &apos;timestamp&apos;: &apos;2010-12-08T08:16:48Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182536&apos;,
  &apos;pos&apos;: [42.3789953, -71.1034623],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;13435407&apos;,
   &apos;timestamp&apos;: &apos;2012-10-10T02:03:51Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182580&apos;,
  &apos;pos&apos;: [42.377667, -71.097915],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008141127&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:26:38Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182600&apos;,
  &apos;pos&apos;: [42.382043, -71.100178],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:26:41Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182612&apos;,
  &apos;pos&apos;: [42.382696, -71.099729],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;2986285&apos;,
   &apos;timestamp&apos;: &apos;2009-10-30T02:02:38Z&apos;,
   &apos;uid&apos;: &apos;40242&apos;,
   &apos;user&apos;: &apos;wfox&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182617&apos;,
  &apos;pos&apos;: [42.381416, -71.085675],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3802028&apos;,
   &apos;timestamp&apos;: &apos;2010-02-06T00:43:35Z&apos;,
   &apos;uid&apos;: &apos;23351&apos;,
   &apos;user&apos;: &apos;JasonWoof&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182670&apos;,
  &apos;pos&apos;: [42.380988, -71.087559],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6670798&apos;,
   &apos;timestamp&apos;: &apos;2010-12-15T19:40:59Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182682&apos;,
  &apos;pos&apos;: [42.3800601, -71.0966788],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6670798&apos;,
   &apos;timestamp&apos;: &apos;2010-12-15T19:40:32Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182691&apos;,
  &apos;pos&apos;: [42.3799353, -71.0965205],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:33:38Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182700&apos;,
  &apos;pos&apos;: [42.379868, -71.090676],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;7681591&apos;,
   &apos;timestamp&apos;: &apos;2011-03-27T01:22:24Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61182857&apos;,
  &apos;pos&apos;: [42.3839186, -71.0818303],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:33:46Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182871&apos;,
  &apos;pos&apos;: [42.38413, -71.084518],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31954058&apos;,
   &apos;timestamp&apos;: &apos;2015-06-14T03:03:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61182931&apos;,
  &apos;pos&apos;: [42.3865685, -71.0786403],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:41:09Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182941&apos;,
  &apos;pos&apos;: [42.385887, -71.081785],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;31954058&apos;,
   &apos;timestamp&apos;: &apos;2015-06-14T03:03:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61182943&apos;,
  &apos;pos&apos;: [42.3865098, -71.0786874],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26653802&apos;,
   &apos;timestamp&apos;: &apos;2014-11-08T23:14:33Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61182955&apos;,
  &apos;pos&apos;: [42.385182, -71.116126],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:33:50Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182981&apos;,
  &apos;pos&apos;: [42.384965, -71.08392],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:33:51Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61182983&apos;,
  &apos;pos&apos;: [42.384826, -71.08506],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6664722&apos;,
   &apos;timestamp&apos;: &apos;2010-12-15T05:57:02Z&apos;,
   &apos;uid&apos;: &apos;221294&apos;,
   &apos;user&apos;: &apos;morganwahl&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61183064&apos;,
  &apos;pos&apos;: [42.3810734, -71.1007802],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32085706&apos;,
   &apos;timestamp&apos;: &apos;2015-06-19T23:18:19Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61183093&apos;,
  &apos;pos&apos;: [42.3931003, -71.084558],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32085706&apos;,
   &apos;timestamp&apos;: &apos;2015-06-19T23:18:19Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61183094&apos;,
  &apos;pos&apos;: [42.3929669, -71.0844113],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32085706&apos;,
   &apos;timestamp&apos;: &apos;2015-06-19T23:18:19Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61183100&apos;,
  &apos;pos&apos;: [42.3926939, -71.0841512],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6692363&apos;,
   &apos;timestamp&apos;: &apos;2010-12-18T00:58:57Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61183103&apos;,
  &apos;pos&apos;: [42.3923778, -71.0838788],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;32085706&apos;,
   &apos;timestamp&apos;: &apos;2015-06-19T23:18:19Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61183111&apos;,
  &apos;pos&apos;: [42.3933742, -71.0848931],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:33:55Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61183118&apos;,
  &apos;pos&apos;: [42.3808, -71.088184],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T10:33:57Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61183131&apos;,
  &apos;pos&apos;: [42.380706, -71.088501],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61183132&apos;,
  &apos;pos&apos;: [42.3794618, -71.0924709],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10297816&apos;,
   &apos;timestamp&apos;: &apos;2012-01-05T06:42:22Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;crossing&apos;,
  &apos;id&apos;: &apos;61183134&apos;,
  &apos;pos&apos;: [42.3795336, -71.0917024],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6691095&apos;,
   &apos;timestamp&apos;: &apos;2010-12-17T21:56:15Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61183161&apos;,
  &apos;pos&apos;: [42.3878309, -71.0838637],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T09:23:58Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61183182&apos;,
  &apos;pos&apos;: [42.395867, -71.100039],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:22Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61183221&apos;,
  &apos;pos&apos;: [42.403336, -71.11709],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:23Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61183227&apos;,
  &apos;pos&apos;: [42.403877, -71.117178],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:49:24Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61183233&apos;,
  &apos;pos&apos;: [42.403843, -71.117173],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3169035&apos;,
   &apos;timestamp&apos;: &apos;2009-11-20T15:01:47Z&apos;,
   &apos;uid&apos;: &apos;175058&apos;,
   &apos;user&apos;: &apos;Tom Walsh&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61183302&apos;,
  &apos;pos&apos;: [42.375656, -71.103182],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;6995552&apos;,
   &apos;timestamp&apos;: &apos;2011-01-17T00:53:10Z&apos;,
   &apos;uid&apos;: &apos;389825&apos;,
   &apos;user&apos;: &apos;synack&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;61263665&apos;,
  &apos;pos&apos;: [42.3888015, -71.1012527],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20684189&apos;,
   &apos;timestamp&apos;: &apos;2014-02-20T22:05:50Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;21&apos;},
  &apos;id&apos;: &apos;61283119&apos;,
  &apos;pos&apos;: [42.3558945, -71.1095733],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;3156865&apos;,
   &apos;timestamp&apos;: &apos;2009-11-19T04:47:37Z&apos;,
   &apos;uid&apos;: &apos;158555&apos;,
   &apos;user&apos;: &apos;Prithason&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61283126&apos;,
  &apos;pos&apos;: [42.3566298, -71.108803],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20696481&apos;,
   &apos;timestamp&apos;: &apos;2014-02-21T16:59:07Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61283218&apos;,
  &apos;pos&apos;: [42.3559928, -71.1033176],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;3156728&apos;,
   &apos;timestamp&apos;: &apos;2009-11-19T03:42:49Z&apos;,
   &apos;uid&apos;: &apos;158555&apos;,
   &apos;user&apos;: &apos;Prithason&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;61283267&apos;,
  &apos;pos&apos;: [42.3600639, -71.0950343],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;21330773&apos;,
   &apos;timestamp&apos;: &apos;2014-03-26T19:08:43Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61283269&apos;,
  &apos;pos&apos;: [42.3601506, -71.0948847],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20665505&apos;,
   &apos;timestamp&apos;: &apos;2014-02-19T23:02:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;id&apos;: &apos;61283273&apos;,
  &apos;pos&apos;: [42.3568683, -71.1135582],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20684189&apos;,
   &apos;timestamp&apos;: &apos;2014-02-20T21:56:42Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61283287&apos;,
  &apos;pos&apos;: [42.3559879, -71.1120124],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20814242&apos;,
   &apos;timestamp&apos;: &apos;2014-02-27T18:55:47Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61283293&apos;,
  &apos;pos&apos;: [42.3561028, -71.0965425],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;390709&apos;,
   &apos;timestamp&apos;: &apos;2008-07-04T19:31:10Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;created_by&apos;: &apos;JOSM&apos;,
  &apos;id&apos;: &apos;61283300&apos;,
  &apos;pos&apos;: [42.3565062, -71.1114735],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20684189&apos;,
   &apos;timestamp&apos;: &apos;2014-02-20T21:56:42Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61283305&apos;,
  &apos;pos&apos;: [42.3564065, -71.1104454],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20814242&apos;,
   &apos;timestamp&apos;: &apos;2014-02-27T18:55:47Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61283311&apos;,
  &apos;pos&apos;: [42.35663, -71.0968722],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;64956&apos;,
   &apos;timestamp&apos;: &apos;2007-10-08T22:22:21Z&apos;,
   &apos;uid&apos;: &apos;15750&apos;,
   &apos;user&apos;: &apos;MassGIS Import&apos;,
   &apos;version&apos;: &apos;1&apos;},
  &apos;created_by&apos;: &apos;JOSM&apos;,
  &apos;id&apos;: &apos;61283315&apos;,
  &apos;pos&apos;: [42.356868, -71.109219],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20684189&apos;,
   &apos;timestamp&apos;: &apos;2014-02-20T21:56:42Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61283322&apos;,
  &apos;pos&apos;: [42.3561359, -71.1099777],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20665505&apos;,
   &apos;timestamp&apos;: &apos;2014-02-19T23:02:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61283333&apos;,
  &apos;pos&apos;: [42.3562777, -71.1142097],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20665505&apos;,
   &apos;timestamp&apos;: &apos;2014-02-19T23:02:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61283340&apos;,
  &apos;pos&apos;: [42.3573774, -71.1129966],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20684189&apos;,
   &apos;timestamp&apos;: &apos;2014-02-20T21:56:42Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61283345&apos;,
  &apos;pos&apos;: [42.3568122, -71.1111466],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;6722174&apos;,
   &apos;timestamp&apos;: &apos;2010-12-21T04:39:16Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;id&apos;: &apos;61283350&apos;,
  &apos;pos&apos;: [42.3628555, -71.0920012],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;390709&apos;,
   &apos;timestamp&apos;: &apos;2008-07-04T19:30:41Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;2&apos;},
  &apos;created_by&apos;: &apos;JOSM&apos;,
  &apos;id&apos;: &apos;61283355&apos;,
  &apos;pos&apos;: [42.3567853, -71.1119628],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;10655450&apos;,
   &apos;timestamp&apos;: &apos;2012-02-11T17:55:37Z&apos;,
   &apos;uid&apos;: &apos;81285&apos;,
   &apos;user&apos;: &apos;Ahlzen&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;crossing&apos;: &apos;traffic_signals&apos;,
  &apos;highway&apos;: &apos;crossing&apos;,
  &apos;id&apos;: &apos;61283361&apos;,
  &apos;pos&apos;: [42.3624442, -71.088182],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;32233903&apos;,
   &apos;timestamp&apos;: &apos;2015-06-26T23:01:56Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;id&apos;: &apos;61283366&apos;,
  &apos;pos&apos;: [42.3628096, -71.0913445],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;6721006&apos;,
   &apos;timestamp&apos;: &apos;2010-12-20T22:28:37Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61283373&apos;,
  &apos;pos&apos;: [42.362326, -71.085167],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20435267&apos;,
   &apos;timestamp&apos;: &apos;2014-02-07T19:28:16Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61283383&apos;,
  &apos;pos&apos;: [42.3713075, -71.1337188],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;6721006&apos;,
   &apos;timestamp&apos;: &apos;2010-12-20T22:37:56Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61283385&apos;,
  &apos;pos&apos;: [42.3624726, -71.0870814],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;27386121&apos;,
   &apos;timestamp&apos;: &apos;2014-12-10T20:48:23Z&apos;,
   &apos;uid&apos;: &apos;2462466&apos;,
   &apos;user&apos;: &apos;EvanMula&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61283393&apos;,
  &apos;pos&apos;: [42.3624033, -71.0861795],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20435267&apos;,
   &apos;timestamp&apos;: &apos;2014-02-07T18:18:50Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61283403&apos;,
  &apos;pos&apos;: [42.3713935, -71.133555],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20435267&apos;,
   &apos;timestamp&apos;: &apos;2014-02-07T19:28:16Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61316729&apos;,
  &apos;pos&apos;: [42.3713588, -71.133626],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20435267&apos;,
   &apos;timestamp&apos;: &apos;2014-02-07T19:28:16Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61316731&apos;,
  &apos;pos&apos;: [42.3710486, -71.1343724],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20435267&apos;,
   &apos;timestamp&apos;: &apos;2014-02-07T19:28:16Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61316732&apos;,
  &apos;pos&apos;: [42.3710574, -71.1341896],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;26733891&apos;,
   &apos;timestamp&apos;: &apos;2014-11-12T12:40:24Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61316733&apos;,
  &apos;pos&apos;: [42.3710804, -71.1345704],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20435267&apos;,
   &apos;timestamp&apos;: &apos;2014-02-07T19:39:48Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61316734&apos;,
  &apos;pos&apos;: [42.3710533, -71.1344428],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20435267&apos;,
   &apos;timestamp&apos;: &apos;2014-02-07T19:28:16Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61316735&apos;,
  &apos;pos&apos;: [42.3712028, -71.1338818],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20416563&apos;,
   &apos;timestamp&apos;: &apos;2014-02-06T20:32:43Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;id&apos;: &apos;61316736&apos;,
  &apos;pos&apos;: [42.3747032, -71.1305838],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20435267&apos;,
   &apos;timestamp&apos;: &apos;2014-02-07T19:28:16Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61316737&apos;,
  &apos;pos&apos;: [42.3710714, -71.1341269],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20435267&apos;,
   &apos;timestamp&apos;: &apos;2014-02-07T19:28:16Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61316738&apos;,
  &apos;pos&apos;: [42.3711032, -71.1340391],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20416563&apos;,
   &apos;timestamp&apos;: &apos;2014-02-06T20:32:43Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;id&apos;: &apos;61316739&apos;,
  &apos;pos&apos;: [42.3745746, -71.1284354],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20833574&apos;,
   &apos;timestamp&apos;: &apos;2014-02-28T19:20:39Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317281&apos;,
  &apos;pos&apos;: [42.359239, -71.0871446],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20814242&apos;,
   &apos;timestamp&apos;: &apos;2014-02-27T19:42:46Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317284&apos;,
  &apos;pos&apos;: [42.3581119, -71.0905168],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;121564&apos;,
   &apos;timestamp&apos;: &apos;2008-06-10T19:10:47Z&apos;,
   &apos;uid&apos;: &apos;14293&apos;,
   &apos;user&apos;: &apos;KindredCoda&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;created_by&apos;: &apos;JOSM&apos;,
  &apos;id&apos;: &apos;61317286&apos;,
  &apos;pos&apos;: [42.3611637, -71.0927647],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;2970505&apos;,
   &apos;timestamp&apos;: &apos;2009-10-28T02:52:16Z&apos;,
   &apos;uid&apos;: &apos;158555&apos;,
   &apos;user&apos;: &apos;Prithason&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317287&apos;,
  &apos;pos&apos;: [42.3607137, -71.0936993],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;32233903&apos;,
   &apos;timestamp&apos;: &apos;2015-06-26T23:01:56Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61317290&apos;,
  &apos;pos&apos;: [42.3626102, -71.0899921],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;32233903&apos;,
   &apos;timestamp&apos;: &apos;2015-06-26T23:01:56Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;13&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61317291&apos;,
  &apos;pos&apos;: [42.3627201, -71.0899428],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20696481&apos;,
   &apos;timestamp&apos;: &apos;2014-02-21T16:59:07Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317292&apos;,
  &apos;pos&apos;: [42.355025, -71.1052874],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20696481&apos;,
   &apos;timestamp&apos;: &apos;2014-02-21T16:59:07Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317293&apos;,
  &apos;pos&apos;: [42.3551458, -71.1050417],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;32233903&apos;,
   &apos;timestamp&apos;: &apos;2015-06-26T23:01:56Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317296&apos;,
  &apos;pos&apos;: [42.3624979, -71.0901346],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;32233903&apos;,
   &apos;timestamp&apos;: &apos;2015-06-26T23:01:56Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317297&apos;,
  &apos;pos&apos;: [42.3625782, -71.0900185],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20607595&apos;,
   &apos;timestamp&apos;: &apos;2014-02-17T02:16:50Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;6&apos;},
  &apos;id&apos;: &apos;61317298&apos;,
  &apos;pos&apos;: [42.3697119, -71.1218632],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20607595&apos;,
   &apos;timestamp&apos;: &apos;2014-02-17T02:16:50Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61317300&apos;,
  &apos;pos&apos;: [42.3697113, -71.1215668],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20696481&apos;,
   &apos;timestamp&apos;: &apos;2014-02-21T16:59:07Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317302&apos;,
  &apos;pos&apos;: [42.3554427, -71.1044373],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20607595&apos;,
   &apos;timestamp&apos;: &apos;2014-02-17T01:57:16Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;14&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61317303&apos;,
  &apos;pos&apos;: [42.3697969, -71.1224585],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20607595&apos;,
   &apos;timestamp&apos;: &apos;2014-02-17T01:57:16Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61317309&apos;,
  &apos;pos&apos;: [42.3697678, -71.122315],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20646514&apos;,
   &apos;timestamp&apos;: &apos;2014-02-18T22:26:57Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61317316&apos;,
  &apos;pos&apos;: [42.3697331, -71.1212386],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20665505&apos;,
   &apos;timestamp&apos;: &apos;2014-02-19T23:02:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317319&apos;,
  &apos;pos&apos;: [42.357373, -71.1151485],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;24198210&apos;,
   &apos;timestamp&apos;: &apos;2014-07-17T10:22:22Z&apos;,
   &apos;uid&apos;: &apos;1670311&apos;,
   &apos;user&apos;: &apos;SophoM&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61317320&apos;,
  &apos;pos&apos;: [42.3691441, -71.117266],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20665505&apos;,
   &apos;timestamp&apos;: &apos;2014-02-19T23:02:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317321&apos;,
  &apos;pos&apos;: [42.3576696, -71.1152866],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20665505&apos;,
   &apos;timestamp&apos;: &apos;2014-02-19T23:02:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317322&apos;,
  &apos;pos&apos;: [42.3575219, -71.1152215],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20646514&apos;,
   &apos;timestamp&apos;: &apos;2014-02-18T22:26:56Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61317323&apos;,
  &apos;pos&apos;: [42.3695963, -71.1181448],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20646514&apos;,
   &apos;timestamp&apos;: &apos;2014-02-18T22:26:57Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317325&apos;,
  &apos;pos&apos;: [42.3692644, -71.1174356],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20646514&apos;,
   &apos;timestamp&apos;: &apos;2014-02-18T22:26:57Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317326&apos;,
  &apos;pos&apos;: [42.3695531, -71.1180116],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20665505&apos;,
   &apos;timestamp&apos;: &apos;2014-02-19T23:02:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317327&apos;,
  &apos;pos&apos;: [42.3572173, -71.1150632],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20665505&apos;,
   &apos;timestamp&apos;: &apos;2014-02-19T23:02:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317329&apos;,
  &apos;pos&apos;: [42.3568149, -71.1147697],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20665505&apos;,
   &apos;timestamp&apos;: &apos;2014-02-19T23:02:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317332&apos;,
  &apos;pos&apos;: [42.3570777, -71.1149728],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20665505&apos;,
   &apos;timestamp&apos;: &apos;2014-02-19T22:33:27Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61317333&apos;,
  &apos;pos&apos;: [42.3588461, -71.1155893],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20665505&apos;,
   &apos;timestamp&apos;: &apos;2014-02-19T23:02:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317334&apos;,
  &apos;pos&apos;: [42.3566223, -71.1145967],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;20665505&apos;,
   &apos;timestamp&apos;: &apos;2014-02-19T23:02:32Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317336&apos;,
  &apos;pos&apos;: [42.3581113, -71.1154243],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T11:14:12Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317337&apos;,
  &apos;pos&apos;: [42.3680388, -71.0907622],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;9573541&apos;,
   &apos;timestamp&apos;: &apos;2011-10-16T15:44:11Z&apos;,
   &apos;uid&apos;: &apos;92937&apos;,
   &apos;user&apos;: &apos;DavidZ&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317338&apos;,
  &apos;pos&apos;: [42.3683758, -71.0905783],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;attribution&apos;: &apos;Office of Geographic and Environmental Information (MassGIS)&apos;,
  &apos;created&apos;: {&apos;changeset&apos;: &apos;32233903&apos;,
   &apos;timestamp&apos;: &apos;2015-06-26T22:54:56Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61317340&apos;,
  &apos;pos&apos;: [42.3623447, -71.0839262],
  &apos;source&apos;: &apos;massgis_import_v0.1_20071008165629&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;10258437&apos;,
   &apos;timestamp&apos;: &apos;2011-12-31T22:46:13Z&apos;,
   &apos;uid&apos;: &apos;354704&apos;,
   &apos;user&apos;: &apos;OceanVortex&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317341&apos;,
  &apos;pos&apos;: [42.3935492, -71.1339722],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T11:06:11Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317355&apos;,
  &apos;pos&apos;: [42.36913, -71.100538],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T06:58:11Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317356&apos;,
  &apos;pos&apos;: [42.393558, -71.134161],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20607595&apos;,
   &apos;timestamp&apos;: &apos;2014-02-17T03:40:25Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61317358&apos;,
  &apos;pos&apos;: [42.3717065, -71.1178538],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20967538&apos;,
   &apos;timestamp&apos;: &apos;2014-03-07T11:24:56Z&apos;,
   &apos;uid&apos;: &apos;1670311&apos;,
   &apos;user&apos;: &apos;SophoM&apos;,
   &apos;version&apos;: &apos;7&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61317359&apos;,
  &apos;pos&apos;: [42.3723549, -71.0794638],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T11:15:56Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317360&apos;,
  &apos;pos&apos;: [42.3721079, -71.0795883],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;21330829&apos;,
   &apos;timestamp&apos;: &apos;2014-03-26T19:12:23Z&apos;,
   &apos;uid&apos;: &apos;967119&apos;,
   &apos;user&apos;: &apos;jwass&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61317361&apos;,
  &apos;pos&apos;: [42.36838, -71.108778],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;794510&apos;,
   &apos;timestamp&apos;: &apos;2009-03-11T23:20:27Z&apos;,
   &apos;uid&apos;: &apos;30891&apos;,
   &apos;user&apos;: &apos;wiso&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61317362&apos;,
  &apos;pos&apos;: [42.367853, -71.107714],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;794510&apos;,
   &apos;timestamp&apos;: &apos;2009-03-11T23:20:27Z&apos;,
   &apos;uid&apos;: &apos;30891&apos;,
   &apos;user&apos;: &apos;wiso&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317363&apos;,
  &apos;pos&apos;: [42.368041, -71.108056],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;1081823&apos;,
   &apos;timestamp&apos;: &apos;2009-05-05T03:36:21Z&apos;,
   &apos;uid&apos;: &apos;23351&apos;,
   &apos;user&apos;: &apos;JasonWoof&apos;,
   &apos;version&apos;: &apos;5&apos;},
  &apos;id&apos;: &apos;61317364&apos;,
  &apos;pos&apos;: [42.3682009, -71.1083835],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T11:11:03Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317365&apos;,
  &apos;pos&apos;: [42.368115, -71.101223],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;3398633&apos;,
   &apos;timestamp&apos;: &apos;2009-12-18T07:11:46Z&apos;,
   &apos;uid&apos;: &apos;23351&apos;,
   &apos;user&apos;: &apos;JasonWoof&apos;,
   &apos;version&apos;: &apos;8&apos;},
  &apos;crossing&apos;: &apos;traffic_signals&apos;,
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61317367&apos;,
  &apos;pos&apos;: [42.3682951, -71.1017379],
  &apos;traffic_signals:sound&apos;: &apos;yes&apos;,
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;29075634&apos;,
   &apos;timestamp&apos;: &apos;2015-02-24T19:29:00Z&apos;,
   &apos;uid&apos;: &apos;2655992&apos;,
   &apos;user&apos;: &apos;steverumizen&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61317368&apos;,
  &apos;pos&apos;: [42.389269, -71.132635],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:02:42Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317369&apos;,
  &apos;pos&apos;: [42.390262, -71.132694],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:02:43Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317370&apos;,
  &apos;pos&apos;: [42.389627, -71.132664],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;20607595&apos;,
   &apos;timestamp&apos;: &apos;2014-02-17T03:40:25Z&apos;,
   &apos;uid&apos;: &apos;326503&apos;,
   &apos;user&apos;: &apos;wambag&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;id&apos;: &apos;61317371&apos;,
  &apos;pos&apos;: [42.3714192, -71.1170584],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:29:43Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317373&apos;,
  &apos;pos&apos;: [42.380254, -71.152818],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:29:43Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317374&apos;,
  &apos;pos&apos;: [42.380448, -71.153074],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;29074230&apos;,
   &apos;timestamp&apos;: &apos;2015-02-24T18:48:58Z&apos;,
   &apos;uid&apos;: &apos;2655992&apos;,
   &apos;user&apos;: &apos;steverumizen&apos;,
   &apos;version&apos;: &apos;4&apos;},
  &apos;highway&apos;: &apos;traffic_signals&apos;,
  &apos;id&apos;: &apos;61317375&apos;,
  &apos;pos&apos;: [42.380055, -71.152441],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:29:44Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317376&apos;,
  &apos;pos&apos;: [42.380138, -71.15263],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:29:45Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317377&apos;,
  &apos;pos&apos;: [42.382151, -71.157597],
  &apos;type&apos;: &apos;node&apos;},
 {&apos;created&apos;: {&apos;changeset&apos;: &apos;448837&apos;,
   &apos;timestamp&apos;: &apos;2009-02-15T07:29:46Z&apos;,
   &apos;uid&apos;: &apos;1034&apos;,
   &apos;user&apos;: &apos;crschmidt&apos;,
   &apos;version&apos;: &apos;3&apos;},
  &apos;id&apos;: &apos;61317378&apos;,
  &apos;pos&apos;: [42.382212, -71.157792],
  &apos;type&apos;: &apos;node&apos;},
 ...]</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="5.-Data-Overview">5. Data Overview<a class="anchor-link" href="#5.-Data-Overview">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Check the size of XML and JSON files</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[33]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">import</span> <span class="nn">os</span>
<span class="k">print</span> <span class="s">&quot;The downloaded XML file is {} MB&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">getsize</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span><span class="o">/</span><span class="mf">1.0e6</span><span class="p">)</span> <span class="c"># convert from bytes to megabytes</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>The downloaded XML file is 421.230253 MB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[34]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">print</span> <span class="s">&quot;The json file is {} MB&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">getsize</span><span class="p">(</span><span class="n">filename</span> <span class="o">+</span> <span class="s">&quot;.json&quot;</span><span class="p">)</span><span class="o">/</span><span class="mf">1.0e6</span><span class="p">)</span> <span class="c"># convert from bytes to megabytes</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>The json file is 484.237902 MB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Execute-mongod-to-run-MongoDB">Execute mongod to run MongoDB<a class="anchor-link" href="#Execute-mongod-to-run-MongoDB">&#182;</a></h4><p>Use the subprocess module to run shell commands.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">import</span> <span class="nn">signal</span>
<span class="kn">import</span> <span class="nn">subprocess</span>

<span class="c"># The os.setsid() is passed in the argument preexec_fn so</span>
<span class="c"># it&#39;s run after the fork() and before  exec() to run the shell.</span>
<span class="n">pro</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">(</span><span class="s">&quot;mongod&quot;</span><span class="p">,</span> <span class="n">preexec_fn</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">setsid</span><span class="p">)</span> 
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><a href="http://sharats.me/the-ever-useful-and-neat-subprocess-module.html">http://sharats.me/the-ever-useful-and-neat-subprocess-module.html</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Connect-database-with-pymongo">Connect database with pymongo<a class="anchor-link" href="#Connect-database-with-pymongo">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[36]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">from</span> <span class="nn">pymongo</span> <span class="kn">import</span> <span class="n">MongoClient</span>

<span class="n">db_name</span> <span class="o">=</span> <span class="s">&quot;osm&quot;</span>

<span class="n">client</span> <span class="o">=</span> <span class="n">MongoClient</span><span class="p">(</span><span class="s">&#39;localhost:27017&#39;</span><span class="p">)</span>
<span class="n">db</span> <span class="o">=</span> <span class="n">client</span><span class="p">[</span><span class="n">db_name</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>When we have to import a large amounts of data, mongoimport is recommended.</p>
<p>First build a mongoimport command, then use subprocess.call to execute</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[37]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="c"># Build mongoimport command</span>
<span class="n">collection</span> <span class="o">=</span> <span class="n">filename</span><span class="p">[:</span><span class="n">filename</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s">&quot;.&quot;</span><span class="p">)]</span>
<span class="c">#print collection</span>
<span class="n">working_directory</span> <span class="o">=</span> <span class="s">&quot;/Users/ducvu/Documents/ud032-master/final_project/&quot;</span>

<span class="n">json_file</span> <span class="o">=</span> <span class="n">filename</span> <span class="o">+</span> <span class="s">&quot;.json&quot;</span>
<span class="c">#print json_file</span>
<span class="n">mongoimport_cmd</span> <span class="o">=</span> <span class="s">&quot;mongoimport --db &quot;</span> <span class="o">+</span> <span class="n">db_name</span> <span class="o">+</span> \
                  <span class="s">&quot; --collection &quot;</span> <span class="o">+</span> <span class="n">collection</span> <span class="o">+</span> \
                  <span class="s">&quot; --file &quot;</span> <span class="o">+</span> <span class="n">working_directory</span> <span class="o">+</span> <span class="n">json_file</span>
<span class="c">#print mongoimport_cmd </span>

<span class="c"># Before importing, drop collection if it exists</span>
<span class="k">if</span> <span class="n">collection</span> <span class="ow">in</span> <span class="n">db</span><span class="o">.</span><span class="n">collection_names</span><span class="p">():</span>
    <span class="k">print</span> <span class="s">&quot;dropping collection&quot;</span>
    <span class="n">db</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">drop</span><span class="p">()</span>

<span class="c"># Execute the command</span>
<span class="k">print</span> <span class="s">&quot;Executing: &quot;</span> <span class="o">+</span> <span class="n">mongoimport_cmd</span>
<span class="n">subprocess</span><span class="o">.</span><span class="n">call</span><span class="p">(</span><span class="n">mongoimport_cmd</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>dropping collection
Executing: mongoimport --db osm --collection boston_massachusetts --file /Users/ducvu/Documents/ud032-master/final_project/boston_massachusetts.osm.json
</pre>
</div>
</div>

<div class="output_area"><div class="prompt output_prompt">Out[37]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>0</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Get-the-collection-from-the-database">Get the collection from the database<a class="anchor-link" href="#Get-the-collection-from-the-database">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">boston_db</span> <span class="o">=</span> <span class="n">db</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Number-of-Documents">Number of Documents<a class="anchor-link" href="#Number-of-Documents">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[39]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">boston_db</span><span class="o">.</span><span class="n">find</span><span class="p">()</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[39]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>2180637</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Number-of-Unique-Users">Number of Unique Users<a class="anchor-link" href="#Number-of-Unique-Users">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[40]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="nb">len</span><span class="p">(</span><span class="n">boston_db</span><span class="o">.</span><span class="n">distinct</span><span class="p">(</span><span class="s">&#39;created.user&#39;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[40]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>1001</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Number-of-Nodes-and-Ways">Number of Nodes and Ways<a class="anchor-link" href="#Number-of-Nodes-and-Ways">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[41]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">node_way</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
        <span class="p">{</span><span class="s">&quot;$group&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;_id&quot;</span> <span class="p">:</span> <span class="s">&quot;$type&quot;</span><span class="p">,</span> <span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$sum&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}}])</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">node_way</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: u&apos;multipolygon&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;video&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;chain_link&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;way&apos;, u&apos;count&apos;: 294189},
 {u&apos;_id&apos;: u&apos;Collaborative Program&apos;, u&apos;count&apos;: 6},
 {u&apos;_id&apos;: u&apos;charter&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;special&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;Approved Special Education&apos;, u&apos;count&apos;: 12},
 {u&apos;_id&apos;: u&apos;Academic&apos;, u&apos;count&apos;: 34},
 {u&apos;_id&apos;: u&apos;Special-Law&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;civil&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;node&apos;, u&apos;count&apos;: 1885954},
 {u&apos;_id&apos;: u&apos;Special&apos;, u&apos;count&apos;: 49},
 {u&apos;_id&apos;: u&apos;Charter&apos;, u&apos;count&apos;: 17},
 {u&apos;_id&apos;: u&apos;Public&apos;, u&apos;count&apos;: 182},
 {u&apos;_id&apos;: u&apos;broad_leaved&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;School&apos;, u&apos;count&apos;: 77},
 {u&apos;_id&apos;: u&apos;private&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;County&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;Private&apos;, u&apos;count&apos;: 87},
 {u&apos;_id&apos;: u&apos;State&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;Special-Medical&apos;, u&apos;count&apos;: 7},
 {u&apos;_id&apos;: u&apos;Special-Institutional&apos;, u&apos;count&apos;: 2}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Number-of-Nodes">Number of Nodes<a class="anchor-link" href="#Number-of-Nodes">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[42]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">boston_db</span><span class="o">.</span><span class="n">find</span><span class="p">({</span><span class="s">&quot;type&quot;</span><span class="p">:</span><span class="s">&quot;node&quot;</span><span class="p">})</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[42]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>1885954</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Number-of-Ways">Number of Ways<a class="anchor-link" href="#Number-of-Ways">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[43]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">boston_db</span><span class="o">.</span><span class="n">find</span><span class="p">({</span><span class="s">&quot;type&quot;</span><span class="p">:</span><span class="s">&quot;way&quot;</span><span class="p">})</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[43]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>294189</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Top-Contributing-User">Top Contributing User<a class="anchor-link" href="#Top-Contributing-User">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[44]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">top_user</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
    <span class="p">{</span><span class="s">&quot;$match&quot;</span><span class="p">:{</span><span class="s">&quot;type&quot;</span><span class="p">:</span><span class="s">&quot;node&quot;</span><span class="p">}},</span>
    <span class="p">{</span><span class="s">&quot;$group&quot;</span><span class="p">:{</span><span class="s">&quot;_id&quot;</span><span class="p">:</span><span class="s">&quot;$created.user&quot;</span><span class="p">,</span><span class="s">&quot;count&quot;</span><span class="p">:{</span><span class="s">&quot;$sum&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">}}},</span>
    <span class="p">{</span><span class="s">&quot;$sort&quot;</span><span class="p">:{</span><span class="s">&quot;count&quot;</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">}},</span>
    <span class="p">{</span><span class="s">&quot;$limit&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">}</span>
<span class="p">])</span>

<span class="c">#print(list(top_user))</span>
<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">top_user</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: u&apos;crschmidt&apos;, u&apos;count&apos;: 1229402}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Number-of-users-having-only-1-post">Number of users having only 1 post<a class="anchor-link" href="#Number-of-users-having-only-1-post">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[45]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">type_buildings</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
    <span class="p">{</span><span class="s">&quot;$group&quot;</span><span class="p">:{</span><span class="s">&quot;_id&quot;</span><span class="p">:</span><span class="s">&quot;$created.user&quot;</span><span class="p">,</span><span class="s">&quot;count&quot;</span><span class="p">:{</span><span class="s">&quot;$sum&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">}}},</span>
    <span class="p">{</span><span class="s">&quot;$group&quot;</span><span class="p">:{</span><span class="s">&quot;_id&quot;</span><span class="p">:{</span><span class="s">&quot;postcount&quot;</span><span class="p">:</span><span class="s">&quot;$count&quot;</span><span class="p">},</span><span class="s">&quot;num_users&quot;</span><span class="p">:{</span><span class="s">&quot;$sum&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">}}},</span>
    <span class="p">{</span><span class="s">&quot;$project&quot;</span><span class="p">:{</span><span class="s">&quot;_id&quot;</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span><span class="s">&quot;postcount&quot;</span><span class="p">:</span><span class="s">&quot;$_id.postcount&quot;</span><span class="p">,</span><span class="s">&quot;num_users&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">}},</span>
    <span class="p">{</span><span class="s">&quot;$sort&quot;</span><span class="p">:{</span><span class="s">&quot;postcount&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">}},</span>
    <span class="p">{</span><span class="s">&quot;$limit&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">}</span>
<span class="p">])</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">type_buildings</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;num_users&apos;: 244, u&apos;postcount&apos;: 1}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Number-of-Documents-Containing-a-Street-Address">Number of Documents Containing a Street Address<a class="anchor-link" href="#Number-of-Documents-Containing-a-Street-Address">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[46]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">boston_db</span><span class="o">.</span><span class="n">find</span><span class="p">({</span><span class="s">&quot;address.street&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$exists&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}})</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[46]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>3026</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Zip-codes">Zip codes<a class="anchor-link" href="#Zip-codes">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[47]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">zipcodes</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
        <span class="p">{</span><span class="s">&quot;$match&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;address.postcode&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$exists&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
        <span class="p">{</span><span class="s">&quot;$group&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;_id&quot;</span> <span class="p">:</span> <span class="s">&quot;$address.postcode&quot;</span><span class="p">,</span> <span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$sum&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
        <span class="p">{</span><span class="s">&quot;$sort&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}}])</span>

<span class="c">#for document in zipcodes:</span>
<span class="c">#    print(document)</span>
    
<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">zipcodes</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: u&apos;02135&apos;, u&apos;count&apos;: 250},
 {u&apos;_id&apos;: u&apos;02139&apos;, u&apos;count&apos;: 230},
 {u&apos;_id&apos;: u&apos;02144&apos;, u&apos;count&apos;: 92},
 {u&apos;_id&apos;: u&apos;02215&apos;, u&apos;count&apos;: 61},
 {u&apos;_id&apos;: u&apos;02114&apos;, u&apos;count&apos;: 59},
 {u&apos;_id&apos;: u&apos;02143&apos;, u&apos;count&apos;: 52},
 {u&apos;_id&apos;: u&apos;02169&apos;, u&apos;count&apos;: 52},
 {u&apos;_id&apos;: u&apos;02134&apos;, u&apos;count&apos;: 49},
 {u&apos;_id&apos;: u&apos;02138&apos;, u&apos;count&apos;: 49},
 {u&apos;_id&apos;: u&apos;02130&apos;, u&apos;count&apos;: 44},
 {u&apos;_id&apos;: u&apos;02116&apos;, u&apos;count&apos;: 41},
 {u&apos;_id&apos;: u&apos;02446&apos;, u&apos;count&apos;: 38},
 {u&apos;_id&apos;: u&apos;02142&apos;, u&apos;count&apos;: 31},
 {u&apos;_id&apos;: u&apos;02472&apos;, u&apos;count&apos;: 30},
 {u&apos;_id&apos;: u&apos;02134-1307&apos;, u&apos;count&apos;: 29},
 {u&apos;_id&apos;: u&apos;02210&apos;, u&apos;count&apos;: 28},
 {u&apos;_id&apos;: u&apos;02467&apos;, u&apos;count&apos;: 26},
 {u&apos;_id&apos;: u&apos;02155&apos;, u&apos;count&apos;: 23},
 {u&apos;_id&apos;: u&apos;02474&apos;, u&apos;count&apos;: 22},
 {u&apos;_id&apos;: u&apos;02128&apos;, u&apos;count&apos;: 22},
 {u&apos;_id&apos;: u&apos;02145&apos;, u&apos;count&apos;: 20},
 {u&apos;_id&apos;: u&apos;02132&apos;, u&apos;count&apos;: 17},
 {u&apos;_id&apos;: u&apos;02141&apos;, u&apos;count&apos;: 16},
 {u&apos;_id&apos;: u&apos;02111&apos;, u&apos;count&apos;: 16},
 {u&apos;_id&apos;: u&apos;02149&apos;, u&apos;count&apos;: 15},
 {u&apos;_id&apos;: u&apos;02140&apos;, u&apos;count&apos;: 14},
 {u&apos;_id&apos;: u&apos;02108&apos;, u&apos;count&apos;: 11},
 {u&apos;_id&apos;: u&apos;02134-1433&apos;, u&apos;count&apos;: 11},
 {u&apos;_id&apos;: u&apos;02127&apos;, u&apos;count&apos;: 11},
 {u&apos;_id&apos;: u&apos;02445&apos;, u&apos;count&apos;: 11},
 {u&apos;_id&apos;: u&apos;02115&apos;, u&apos;count&apos;: 9},
 {u&apos;_id&apos;: u&apos;02134-1420&apos;, u&apos;count&apos;: 9},
 {u&apos;_id&apos;: u&apos;02478&apos;, u&apos;count&apos;: 9},
 {u&apos;_id&apos;: u&apos;02134-1305&apos;, u&apos;count&apos;: 9},
 {u&apos;_id&apos;: u&apos;02150&apos;, u&apos;count&apos;: 8},
 {u&apos;_id&apos;: u&apos;02109&apos;, u&apos;count&apos;: 8},
 {u&apos;_id&apos;: u&apos;02124&apos;, u&apos;count&apos;: 8},
 {u&apos;_id&apos;: u&apos;02476&apos;, u&apos;count&apos;: 8},
 {u&apos;_id&apos;: u&apos;02138-2903&apos;, u&apos;count&apos;: 8},
 {u&apos;_id&apos;: u&apos;02131&apos;, u&apos;count&apos;: 8},
 {u&apos;_id&apos;: u&apos;02186&apos;, u&apos;count&apos;: 8},
 {u&apos;_id&apos;: u&apos;02138-2701&apos;, u&apos;count&apos;: 8},
 {u&apos;_id&apos;: u&apos;02126&apos;, u&apos;count&apos;: 7},
 {u&apos;_id&apos;: u&apos;02110&apos;, u&apos;count&apos;: 7},
 {u&apos;_id&apos;: u&apos;02122&apos;, u&apos;count&apos;: 6},
 {u&apos;_id&apos;: u&apos;02459&apos;, u&apos;count&apos;: 6},
 {u&apos;_id&apos;: u&apos;02134-1322&apos;, u&apos;count&apos;: 6},
 {u&apos;_id&apos;: u&apos;02118&apos;, u&apos;count&apos;: 6},
 {u&apos;_id&apos;: u&apos;02136&apos;, u&apos;count&apos;: 6},
 {u&apos;_id&apos;: u&apos;MA&apos;, u&apos;count&apos;: 6},
 {u&apos;_id&apos;: u&apos;02134-1319&apos;, u&apos;count&apos;: 5},
 {u&apos;_id&apos;: u&apos;02171&apos;, u&apos;count&apos;: 5},
 {u&apos;_id&apos;: u&apos;02125&apos;, u&apos;count&apos;: 5},
 {u&apos;_id&apos;: u&apos;02134-1442&apos;, u&apos;count&apos;: 5},
 {u&apos;_id&apos;: u&apos;02138-2901&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;02134-1311&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;02138-2801&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;02134-1321&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;02458&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;02134-1313&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;02134-1409&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;MA 02116&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;02134-1317&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;02151&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;02138-2933&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;02134-1316&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;02138-2706&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;02170&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;02120&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;02184&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;02043&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;02138-2736&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;02134-1306&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;02152&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;02134-1318&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;02129&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;02131-3025&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;02121&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;02119&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;02134-1312&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;01250&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02138-2735&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02138-2763&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02138-2762&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02174&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;01821&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02134-1327&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02130-4803&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02131-4931&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;01125&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02140-2215&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02474-8735&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02138-2742&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02138-3003&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02445-5841&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02138-3824&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02138-1901&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02284-6028&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02140-1340&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;01238&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02110-1301&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02132-3226&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;01240&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02026-5036&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;01944&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;MA 02186&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02113&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;Mass Ave&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02205&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos; 02472&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02136-2460&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02132-1239&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02159&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02114-3203&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02228&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02138-2724&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02148&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;02026&apos;, u&apos;count&apos;: 1}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Top-5-Most-Common-Cities">Top 5 Most Common Cities<a class="anchor-link" href="#Top-5-Most-Common-Cities">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[48]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">cities</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([{</span><span class="s">&quot;$match&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;address.city&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$exists&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
                           <span class="p">{</span><span class="s">&quot;$group&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;_id&quot;</span> <span class="p">:</span> <span class="s">&quot;$address.city&quot;</span><span class="p">,</span> <span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$sum&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
                           <span class="p">{</span><span class="s">&quot;$sort&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}},</span> \
                           <span class="p">{</span><span class="s">&quot;$limit&quot;</span> <span class="p">:</span> <span class="mi">5</span><span class="p">}])</span>

<span class="c">#for city in cities :</span>
<span class="c">#    print city</span>
    
<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">cities</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: u&apos;Boston&apos;, u&apos;count&apos;: 594},
 {u&apos;_id&apos;: u&apos;Malden&apos;, u&apos;count&apos;: 413},
 {u&apos;_id&apos;: u&apos;Cambridge&apos;, u&apos;count&apos;: 323},
 {u&apos;_id&apos;: u&apos;Somerville&apos;, u&apos;count&apos;: 153},
 {u&apos;_id&apos;: u&apos;Quincy&apos;, u&apos;count&apos;: 51}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Top-10-Amenities">Top 10 Amenities<a class="anchor-link" href="#Top-10-Amenities">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[49]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">amenities</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
        <span class="p">{</span><span class="s">&quot;$match&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;amenity&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$exists&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
        <span class="p">{</span><span class="s">&quot;$group&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;_id&quot;</span> <span class="p">:</span> <span class="s">&quot;$amenity&quot;</span><span class="p">,</span> <span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$sum&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
        <span class="p">{</span><span class="s">&quot;$sort&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}},</span> \
        <span class="p">{</span><span class="s">&quot;$limit&quot;</span> <span class="p">:</span> <span class="mi">10</span><span class="p">}])</span>

<span class="c">#for document in amenities:</span>
<span class="c">#    print document</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">amenities</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: u&apos;parking&apos;, u&apos;count&apos;: 1192},
 {u&apos;_id&apos;: u&apos;bench&apos;, u&apos;count&apos;: 946},
 {u&apos;_id&apos;: u&apos;school&apos;, u&apos;count&apos;: 774},
 {u&apos;_id&apos;: u&apos;restaurant&apos;, u&apos;count&apos;: 532},
 {u&apos;_id&apos;: u&apos;parking_space&apos;, u&apos;count&apos;: 444},
 {u&apos;_id&apos;: u&apos;place_of_worship&apos;, u&apos;count&apos;: 407},
 {u&apos;_id&apos;: u&apos;library&apos;, u&apos;count&apos;: 342},
 {u&apos;_id&apos;: u&apos;bicycle_parking&apos;, u&apos;count&apos;: 238},
 {u&apos;_id&apos;: u&apos;cafe&apos;, u&apos;count&apos;: 199},
 {u&apos;_id&apos;: u&apos;fast_food&apos;, u&apos;count&apos;: 169}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[50]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">amenities</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
    <span class="p">{</span><span class="s">&quot;$match&quot;</span><span class="p">:{</span><span class="s">&quot;amenity&quot;</span><span class="p">:{</span><span class="s">&quot;$exists&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">},</span><span class="s">&quot;type&quot;</span><span class="p">:</span><span class="s">&quot;node&quot;</span><span class="p">}},</span>
    <span class="p">{</span><span class="s">&quot;$group&quot;</span><span class="p">:{</span><span class="s">&quot;_id&quot;</span><span class="p">:</span><span class="s">&quot;$amenity&quot;</span><span class="p">,</span><span class="s">&quot;count&quot;</span><span class="p">:{</span><span class="s">&quot;$sum&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">}}},</span>
    <span class="p">{</span><span class="s">&quot;$sort&quot;</span><span class="p">:{</span><span class="s">&quot;count&quot;</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">}},</span>
    <span class="p">{</span><span class="s">&quot;$limit&quot;</span><span class="p">:</span><span class="mi">10</span><span class="p">}</span>
<span class="p">])</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">amenities</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: u&apos;bench&apos;, u&apos;count&apos;: 938},
 {u&apos;_id&apos;: u&apos;restaurant&apos;, u&apos;count&apos;: 493},
 {u&apos;_id&apos;: u&apos;school&apos;, u&apos;count&apos;: 370},
 {u&apos;_id&apos;: u&apos;place_of_worship&apos;, u&apos;count&apos;: 317},
 {u&apos;_id&apos;: u&apos;bicycle_parking&apos;, u&apos;count&apos;: 238},
 {u&apos;_id&apos;: u&apos;cafe&apos;, u&apos;count&apos;: 182},
 {u&apos;_id&apos;: u&apos;fast_food&apos;, u&apos;count&apos;: 154},
 {u&apos;_id&apos;: u&apos;library&apos;, u&apos;count&apos;: 141},
 {u&apos;_id&apos;: u&apos;bicycle_rental&apos;, u&apos;count&apos;: 141},
 {u&apos;_id&apos;: u&apos;fire_station&apos;, u&apos;count&apos;: 96}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Most-common-building-types">Most common building types<a class="anchor-link" href="#Most-common-building-types">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[51]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">type_buildings</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
    <span class="p">{</span><span class="s">&#39;$match&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s">&#39;building&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s">&#39;$exists&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> 
    <span class="p">{</span><span class="s">&#39;$group&#39;</span><span class="p">:</span> <span class="p">{</span> <span class="s">&#39;_id&#39;</span><span class="p">:</span> <span class="s">&#39;$building&#39;</span><span class="p">,</span><span class="s">&#39;count&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s">&#39;$sum&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span>
    <span class="p">{</span><span class="s">&#39;$sort&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s">&#39;count&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}},</span> <span class="p">{</span><span class="s">&#39;$limit&#39;</span><span class="p">:</span> <span class="mi">20</span><span class="p">}</span>
<span class="p">])</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">type_buildings</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: u&apos;yes&apos;, u&apos;count&apos;: 248378},
 {u&apos;_id&apos;: u&apos;garage&apos;, u&apos;count&apos;: 673},
 {u&apos;_id&apos;: u&apos;house&apos;, u&apos;count&apos;: 629},
 {u&apos;_id&apos;: u&apos;apartments&apos;, u&apos;count&apos;: 422},
 {u&apos;_id&apos;: u&apos;university&apos;, u&apos;count&apos;: 295},
 {u&apos;_id&apos;: u&apos;shed&apos;, u&apos;count&apos;: 131},
 {u&apos;_id&apos;: u&apos;roof&apos;, u&apos;count&apos;: 109},
 {u&apos;_id&apos;: u&apos;dormitory&apos;, u&apos;count&apos;: 98},
 {u&apos;_id&apos;: u&apos;school&apos;, u&apos;count&apos;: 88},
 {u&apos;_id&apos;: u&apos;residential&apos;, u&apos;count&apos;: 76},
 {u&apos;_id&apos;: u&apos;commercial&apos;, u&apos;count&apos;: 69},
 {u&apos;_id&apos;: u&apos;retail&apos;, u&apos;count&apos;: 53},
 {u&apos;_id&apos;: u&apos;entrance&apos;, u&apos;count&apos;: 37},
 {u&apos;_id&apos;: u&apos;storage_tank&apos;, u&apos;count&apos;: 30},
 {u&apos;_id&apos;: u&apos;church&apos;, u&apos;count&apos;: 27},
 {u&apos;_id&apos;: u&apos;home&apos;, u&apos;count&apos;: 26},
 {u&apos;_id&apos;: u&apos;office&apos;, u&apos;count&apos;: 20},
 {u&apos;_id&apos;: u&apos;industrial&apos;, u&apos;count&apos;: 16},
 {u&apos;_id&apos;: u&apos;hospital&apos;, u&apos;count&apos;: 7},
 {u&apos;_id&apos;: u&apos;hotel&apos;, u&apos;count&apos;: 5}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Top-Religions-with-Denominations">Top Religions with Denominations<a class="anchor-link" href="#Top-Religions-with-Denominations">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[52]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">religions</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
        <span class="p">{</span><span class="s">&quot;$match&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;amenity&quot;</span> <span class="p">:</span> <span class="s">&quot;place_of_worship&quot;</span><span class="p">}},</span> \
        <span class="p">{</span><span class="s">&quot;$group&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;_id&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;religion&quot;</span> <span class="p">:</span> <span class="s">&quot;$religion&quot;</span><span class="p">,</span> <span class="s">&quot;denomination&quot;</span> <span class="p">:</span> <span class="s">&quot;$denomination&quot;</span><span class="p">},</span> <span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$sum&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
        <span class="p">{</span><span class="s">&quot;$sort&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}}])</span>

<span class="c">#for document in religions:</span>
<span class="c">#    print document</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">religions</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: {u&apos;religion&apos;: u&apos;christian&apos;}, u&apos;count&apos;: 189},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;baptist&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 53},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;methodist&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 22},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;catholic&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 22},
 {u&apos;_id&apos;: {}, u&apos;count&apos;: 16},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;roman_catholic&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 10},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;presbyterian&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 10},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;lutheran&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 9},
 {u&apos;_id&apos;: {u&apos;religion&apos;: u&apos;jewish&apos;}, u&apos;count&apos;: 9},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;pentecostal&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 8},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;episcopal&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 8},
 {u&apos;_id&apos;: {u&apos;religion&apos;: u&apos;unitarian&apos;}, u&apos;count&apos;: 6},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;orthodox&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 4},
 {u&apos;_id&apos;: {u&apos;religion&apos;: u&apos;unitarian_universalist&apos;}, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;mormon&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 3},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;anglican&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;zen&apos;, u&apos;religion&apos;: u&apos;buddhist&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;congregational&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;reform&apos;, u&apos;religion&apos;: u&apos;jewish&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;reformed&apos;, u&apos;religion&apos;: u&apos;jewish&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;jehovahs_witness&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;evangelical&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;non-denominational&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;seventh_day_adventist&apos;,
           u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;greek_orthodox&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;conservative&apos;, u&apos;religion&apos;: u&apos;jewish&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;union church of christ&apos;,
           u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;Congregational&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;sunni&apos;, u&apos;religion&apos;: u&apos;muslim&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;UUA&apos;, u&apos;religion&apos;: u&apos;christian&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;united_church_of_christ&apos;,
           u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;salvation_army&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;christ_scientist&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;quaker&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;swedenborgian&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;hasidic&apos;, u&apos;religion&apos;: u&apos;jewish&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;roman_catholic&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;greek_catholic&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;religion&apos;: u&apos;buddhist&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;religion&apos;: u&apos;muslim&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;orthodox&apos;, u&apos;religion&apos;: u&apos;jewish&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;non-denominational&apos;, u&apos;religion&apos;: u&apos;jewish&apos;},
  u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;denomination&apos;: u&apos;unitarian&apos;, u&apos;religion&apos;: u&apos;christian&apos;},
  u&apos;count&apos;: 1}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Top-10-Leisures">Top 10 Leisures<a class="anchor-link" href="#Top-10-Leisures">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[53]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">leisures</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([{</span><span class="s">&quot;$match&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;leisure&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$exists&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
                           <span class="p">{</span><span class="s">&quot;$group&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;_id&quot;</span> <span class="p">:</span> <span class="s">&quot;$leisure&quot;</span><span class="p">,</span> <span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$sum&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
                           <span class="p">{</span><span class="s">&quot;$sort&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}},</span> \
                           <span class="p">{</span><span class="s">&quot;$limit&quot;</span> <span class="p">:</span> <span class="mi">10</span><span class="p">}])</span>

<span class="c">#for document in leisures:</span>
<span class="c">#    print document</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">leisures</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: u&apos;park&apos;, u&apos;count&apos;: 750},
 {u&apos;_id&apos;: u&apos;pitch&apos;, u&apos;count&apos;: 545},
 {u&apos;_id&apos;: u&apos;recreation_ground&apos;, u&apos;count&apos;: 350},
 {u&apos;_id&apos;: u&apos;playground&apos;, u&apos;count&apos;: 334},
 {u&apos;_id&apos;: u&apos;nature_reserve&apos;, u&apos;count&apos;: 105},
 {u&apos;_id&apos;: u&apos;garden&apos;, u&apos;count&apos;: 35},
 {u&apos;_id&apos;: u&apos;sports_centre&apos;, u&apos;count&apos;: 33},
 {u&apos;_id&apos;: u&apos;picnic_table&apos;, u&apos;count&apos;: 33},
 {u&apos;_id&apos;: u&apos;swimming_pool&apos;, u&apos;count&apos;: 28},
 {u&apos;_id&apos;: u&apos;common&apos;, u&apos;count&apos;: 19}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Top-15-Universities">Top 15 Universities<a class="anchor-link" href="#Top-15-Universities">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[54]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">universities</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
        <span class="p">{</span><span class="s">&quot;$match&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;amenity&quot;</span> <span class="p">:</span> <span class="s">&quot;university&quot;</span><span class="p">}},</span> \
        <span class="p">{</span><span class="s">&quot;$group&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;_id&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;name&quot;</span> <span class="p">:</span> <span class="s">&quot;$name&quot;</span><span class="p">},</span> <span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$sum&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
        <span class="p">{</span><span class="s">&quot;$sort&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}},</span>
        <span class="p">{</span><span class="s">&quot;$limit&quot;</span><span class="p">:</span><span class="mi">15</span><span class="p">}</span>
    <span class="p">])</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">universities</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Boston University&apos;}, u&apos;count&apos;: 41},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Massachusetts Institute of Technology&apos;}, u&apos;count&apos;: 10},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Suffolk University&apos;}, u&apos;count&apos;: 8},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Harvard University&apos;}, u&apos;count&apos;: 6},
 {u&apos;_id&apos;: {u&apos;name&apos;: None}, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;University of Massachusetts Boston&apos;}, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Boston University Medical Campus&apos;}, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;University Hall&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Harvard Medical School&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Benjamin Franklin Institute of Technology&apos;},
  u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Littauer Center&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Northeastern University&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Boston College&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Radcliffe Gym&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Agassiz House&apos;}, u&apos;count&apos;: 1}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Top-10-Schools">Top 10 Schools<a class="anchor-link" href="#Top-10-Schools">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[55]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">schools</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
        <span class="p">{</span><span class="s">&quot;$match&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;amenity&quot;</span> <span class="p">:</span> <span class="s">&quot;school&quot;</span><span class="p">}},</span> \
        <span class="p">{</span><span class="s">&quot;$group&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;_id&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;name&quot;</span> <span class="p">:</span> <span class="s">&quot;$name&quot;</span><span class="p">},</span> <span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$sum&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
        <span class="p">{</span><span class="s">&quot;$sort&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}},</span>
        <span class="p">{</span><span class="s">&quot;$limit&quot;</span><span class="p">:</span><span class="mi">10</span><span class="p">}</span>
    <span class="p">])</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">schools</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: {u&apos;name&apos;: None}, u&apos;count&apos;: 13},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Milton Academy&apos;}, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Lincoln School&apos;}, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Boston Community Leadership Academy&apos;}, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;New Mission High School&apos;}, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Dexter School&apos;}, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Boston Middle School Academy&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Clark Avenue School&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Kennedy Day School&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Phillips School&apos;}, u&apos;count&apos;: 2}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Top-Prisons">Top Prisons<a class="anchor-link" href="#Top-Prisons">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[56]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">prisons</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
        <span class="p">{</span><span class="s">&quot;$match&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;amenity&quot;</span> <span class="p">:</span> <span class="s">&quot;prison&quot;</span><span class="p">}},</span> \
        <span class="p">{</span><span class="s">&quot;$group&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;_id&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;name&quot;</span> <span class="p">:</span> <span class="s">&quot;$name&quot;</span><span class="p">},</span> <span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$sum&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
        <span class="p">{</span><span class="s">&quot;$sort&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}}])</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">prisons</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Norfolk County Jail&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Middlesex County Jail (Cambridge)&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Suffolk County House of Correction&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Suffolk County Jail&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Boston Pre-Release Center&apos;}, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Lemuel Shattuck Hospital Correctional Unit&apos;},
  u&apos;count&apos;: 1}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Top-10-Hospitals">Top 10 Hospitals<a class="anchor-link" href="#Top-10-Hospitals">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[57]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">hospitals</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
        <span class="p">{</span><span class="s">&quot;$match&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;amenity&quot;</span> <span class="p">:</span> <span class="s">&quot;hospital&quot;</span><span class="p">}},</span> \
        <span class="p">{</span><span class="s">&quot;$group&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;_id&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;name&quot;</span> <span class="p">:</span> <span class="s">&quot;$name&quot;</span><span class="p">},</span> <span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;$sum&quot;</span> <span class="p">:</span> <span class="mi">1</span><span class="p">}}},</span> \
        <span class="p">{</span><span class="s">&quot;$sort&quot;</span> <span class="p">:</span> <span class="p">{</span><span class="s">&quot;count&quot;</span> <span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}},</span>
        <span class="p">{</span><span class="s">&quot;$limit&quot;</span><span class="p">:</span><span class="mi">10</span><span class="p">}</span>
    <span class="p">])</span>


<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">hospitals</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Carney Hospital&apos;}, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: {u&apos;name&apos;: None}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&quot;St. Elizabeth&apos;s Medical Center&quot;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Arbour Hospital&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Bournewood Hospital&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Arbour-Hri Hospital&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Cambridge Health Alliance-Whidden Memorial Hospital&apos;},
  u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Faulkner Hospital&apos;}, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Steward Satellite Emergency Facility - Quincy&apos;},
  u&apos;count&apos;: 2},
 {u&apos;_id&apos;: {u&apos;name&apos;: u&apos;Central Street Health Center&apos;}, u&apos;count&apos;: 2}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Most-popular-cuisines-in-fast-foods">Most popular cuisines in fast foods<a class="anchor-link" href="#Most-popular-cuisines-in-fast-foods">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>fast_food = boston_db.aggregate([
    {"$match":{"cuisine":{"$exists":1},"amenity":"fast_food"}},
    {"$group":{"_id":"$cuisine","count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":10}
])</p>
<p>pprint.pprint(list(fast_food))</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Most-popular-gas-station-brands">Most popular gas station brands<a class="anchor-link" href="#Most-popular-gas-station-brands">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[59]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">gas_station_brands</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
    <span class="p">{</span><span class="s">&quot;$match&quot;</span><span class="p">:{</span><span class="s">&quot;brand&quot;</span><span class="p">:{</span><span class="s">&quot;$exists&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">},</span><span class="s">&quot;amenity&quot;</span><span class="p">:</span><span class="s">&quot;fuel&quot;</span><span class="p">}},</span>
    <span class="p">{</span><span class="s">&quot;$group&quot;</span><span class="p">:{</span><span class="s">&quot;_id&quot;</span><span class="p">:</span><span class="s">&quot;$brand&quot;</span><span class="p">,</span><span class="s">&quot;count&quot;</span><span class="p">:{</span><span class="s">&quot;$sum&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">}}},</span>
    <span class="p">{</span><span class="s">&quot;$sort&quot;</span><span class="p">:{</span><span class="s">&quot;count&quot;</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">}},</span>
    <span class="p">{</span><span class="s">&quot;$limit&quot;</span><span class="p">:</span><span class="mi">10</span><span class="p">}</span>
<span class="p">])</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">gas_station_brands</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: u&apos;Gulf&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;Shell&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;Hess&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;Super Petroleum&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&quot;Eli&apos;s&quot;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;APrime Energy&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;US Petroleum&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;Cumberland Farm&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;Valvoline Oil Change&apos;, u&apos;count&apos;: 1},
 {u&apos;_id&apos;: u&apos;Sunoco&apos;, u&apos;count&apos;: 1}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Most-popular-banks">Most popular banks<a class="anchor-link" href="#Most-popular-banks">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[60]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">banks</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
    <span class="p">{</span><span class="s">&quot;$match&quot;</span><span class="p">:{</span><span class="s">&quot;name&quot;</span><span class="p">:{</span><span class="s">&quot;$exists&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">},</span><span class="s">&quot;amenity&quot;</span><span class="p">:</span><span class="s">&quot;bank&quot;</span><span class="p">}},</span>
    <span class="p">{</span><span class="s">&quot;$group&quot;</span><span class="p">:{</span><span class="s">&quot;_id&quot;</span><span class="p">:</span><span class="s">&quot;$name&quot;</span><span class="p">,</span><span class="s">&quot;count&quot;</span><span class="p">:{</span><span class="s">&quot;$sum&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">}}},</span>
    <span class="p">{</span><span class="s">&quot;$sort&quot;</span><span class="p">:{</span><span class="s">&quot;count&quot;</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">}},</span>
    <span class="p">{</span><span class="s">&quot;$limit&quot;</span><span class="p">:</span><span class="mi">10</span><span class="p">}</span>
<span class="p">])</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">banks</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: u&apos;Bank of America&apos;, u&apos;count&apos;: 11},
 {u&apos;_id&apos;: u&apos;Citizens Bank&apos;, u&apos;count&apos;: 7},
 {u&apos;_id&apos;: u&apos;TD Bank&apos;, u&apos;count&apos;: 6},
 {u&apos;_id&apos;: u&apos;Eastern Bank&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;Cambridge Savings Bank&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;Santander&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;Sovereign Bank&apos;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;Brookline Bank&apos;, u&apos;count&apos;: 3},
 {u&apos;_id&apos;: u&apos;East Cambridge Savings Bank&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;Cambridge Trust Company&apos;, u&apos;count&apos;: 2}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Most-popular-restaurants">Most popular restaurants<a class="anchor-link" href="#Most-popular-restaurants">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[61]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">restaurants</span> <span class="o">=</span> <span class="n">boston_db</span><span class="o">.</span><span class="n">aggregate</span><span class="p">([</span>
    <span class="p">{</span><span class="s">&quot;$match&quot;</span><span class="p">:{</span><span class="s">&quot;name&quot;</span><span class="p">:{</span><span class="s">&quot;$exists&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">},</span><span class="s">&quot;amenity&quot;</span><span class="p">:</span><span class="s">&quot;restaurant&quot;</span><span class="p">}},</span>
    <span class="p">{</span><span class="s">&quot;$group&quot;</span><span class="p">:{</span><span class="s">&quot;_id&quot;</span><span class="p">:</span><span class="s">&quot;$name&quot;</span><span class="p">,</span><span class="s">&quot;count&quot;</span><span class="p">:{</span><span class="s">&quot;$sum&quot;</span><span class="p">:</span><span class="mi">1</span><span class="p">}}},</span>
    <span class="p">{</span><span class="s">&quot;$sort&quot;</span><span class="p">:{</span><span class="s">&quot;count&quot;</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">}},</span>
    <span class="p">{</span><span class="s">&quot;$limit&quot;</span><span class="p">:</span><span class="mi">10</span><span class="p">}</span>
<span class="p">])</span>

<span class="n">pprint</span><span class="o">.</span><span class="n">pprint</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">restaurants</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[{u&apos;_id&apos;: u&apos;Panera Bread&apos;, u&apos;count&apos;: 6},
 {u&apos;_id&apos;: u&quot;Bertucci&apos;s&quot;, u&apos;count&apos;: 4},
 {u&apos;_id&apos;: u&apos;Dunkin Donuts&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;Olecito&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;The Elephant Walk&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;Chipotle&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;Boloco&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&quot;Crazy Dough&apos;s&quot;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;Ninety Nine&apos;, u&apos;count&apos;: 2},
 {u&apos;_id&apos;: u&apos;Boca Grande&apos;, u&apos;count&apos;: 2}]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="6.-Additional-Ideas">6. Additional Ideas<a class="anchor-link" href="#6.-Additional-Ideas">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Analyzing the data of Boston I found out that not all nodes or ways include this information since its geographical position is represented within regions of a city. What could be done in this case, is check if each node or way belongs to a city based on the latitude and longitude and ensure that the property "address.city" is properly informed. By doing so, we could get statistics related to cities in a much more reliable way. In fact, I think this is the biggest benefit to anticipate problems and implement improvements to the data you want to analyze. Real world data are very susceptible to being incomplete, noisy and inconsistent which means that if you have low-quality of data the results of their analysis will also be of poor quality.</p>
<p>I think that extending this open source project to include data such as user reviews of establishments, subjective areas of what bound a good and bad neighborhood, housing price data, school reviews, walkability/bikeability, quality of mass transit, and on would form a solid foundation of robust recommender systems. These recommender systems could aid users in anything from finding a new home or apartment to helping a user decide where to spend a weekend afternoon.</p>
<p>Another alternative to help in the absence of information in the region would be the use of gamification or crowdsource information to make more people help in the map contribution. Something like the mobile apps similar to Waze and Minutely have already done to make the users responsible for improving the app and  social network around the app.</p>
<p>A different application of this project is that it can be helpful on the problem of how the city boundaries well-defined. The transportation networks (street networks), the built environment can be good indicators of metropolitan area and combining an elementary clustering technique, we consider two street intersections to belong to the same cluster if they have a distance below a given distance threshold (in metres). The geospatial information gives us a good definition of city boundaries through spatial urban networks.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>An interesting fact that we can use the geospatial coordinates information to find out country/city name (search OSM data by name and address and to generate synthetic addresses of OSM points). This problem is called reverse geocoding which  maps geospatial coordinates to location name. And the <a href="http://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding">Nominatim</a> from Open Street Map enables us to do that.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[71]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">from</span> <span class="nn">geopy.geocoders</span> <span class="kn">import</span> <span class="n">Nominatim</span>
<span class="n">geolocator</span> <span class="o">=</span> <span class="n">Nominatim</span><span class="p">()</span>
<span class="n">location</span> <span class="o">=</span> <span class="n">geolocator</span><span class="o">.</span><span class="n">reverse</span><span class="p">(</span><span class="s">&quot;42.3725677, -71.1193068&quot;</span><span class="p">)</span>
<span class="k">print</span><span class="p">(</span><span class="n">location</span><span class="o">.</span><span class="n">address</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>The Garage, Mount Auburn Street, Harvard Square, Cambridge, Middlesex County, Massachusetts, 02138, United States of America
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>However, potential problems associated with reverse geocoding is that it may give us weird results near the poles and the international date line or for cities within cities, for example certain locations in Rome may return "Vatican City" - depending on the lat/lon specified in the database for each</p>
<p>For example :  Pontificio Collegio Teutonico di Santa Maria in Campo Santo (Collegio Teutonico) is located in Vatican City but the result of given set of coordinates gives us the location in Roma, Italia.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[78]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">from</span> <span class="nn">geopy.geocoders</span> <span class="kn">import</span> <span class="n">Nominatim</span>
<span class="n">geolocator</span> <span class="o">=</span> <span class="n">Nominatim</span><span class="p">()</span>
<span class="n">vatican</span><span class="o">=</span><span class="p">(</span><span class="mf">41.89888433</span><span class="p">,</span> <span class="mf">12.45376451</span><span class="p">)</span>
<span class="n">location</span> <span class="o">=</span> <span class="n">geolocator</span><span class="o">.</span><span class="n">reverse</span><span class="p">(</span><span class="n">vatican</span><span class="p">)</span>
<span class="k">print</span><span class="p">(</span><span class="n">location</span><span class="o">.</span><span class="n">address</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Sotto La Cupola - Guest House, 15, Via Cardinal Agliardi, Aurelio, Municipio Roma XIII, Roma, RM, LAZ, 00165, Italia
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[79]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">from</span> <span class="nn">geopy.geocoders</span> <span class="kn">import</span> <span class="n">Nominatim</span>
<span class="n">geolocator</span> <span class="o">=</span> <span class="n">Nominatim</span><span class="p">()</span>
<span class="n">artic</span><span class="o">=</span><span class="p">(</span><span class="o">-</span><span class="mf">86.06303611</span><span class="p">,</span><span class="mf">6.81517107</span><span class="p">)</span>
<span class="n">location</span> <span class="o">=</span> <span class="n">geolocator</span><span class="o">.</span><span class="n">reverse</span><span class="p">(</span><span class="n">artic</span><span class="p">)</span>
<span class="k">print</span><span class="p">(</span><span class="n">location</span><span class="o">.</span><span class="n">address</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>None
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Despite the many issues with the reverse coding, I think another benefits of this project that it can be applied in disease mapping which facilitates us use the longitudes and latitudes information to find the plaintext addresses of patients for identifying patterns, correlates, and predictors of disease in academia, government and private sector with the widespread availability of geographic information.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="7.--Conclusion">7.  Conclusion<a class="anchor-link" href="#7.--Conclusion">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This review of the data is cursory, but it seems that the Boston area is incomplete, though I believe it has been well cleaned and represented after this project.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="8.--References">8.  References<a class="anchor-link" href="#8.--References">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><a href="http://wiki.openstreetmap.org/wiki/Main_Page">OpenStreetMap Wiki Page</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/OSM_XML">OpenStreetMap Wiki Page - OSM XML
</a></p>
<p><a href="http://wiki.openstreetmap.org/wiki/Map_Features">OpenStreetMap Map Features</a></p>
<p><a href="https://docs.python.org/2/library/re.html#search-vs-match">Python Regular Expressions</a></p>
<p><a href="https://docs.mongodb.org/v2.4/reference/operator/">MongoDB Operators</a></p>
<p><a href="http://www.choskim.me/how-to-install-mongodb-on-apples-mac-os-x/">Install MongoDB on Apple's Mac OS X</a></p>
<p><a href="https://books.google.com/books?id=_VkrAQAAQBAJ&pg=PA241&lpg=PA241&dq=execute+mongodb+command+in+ipython&source=bl&ots=JqnwlwRvkN&sig=h-TrwspKAmHt1g1ELItnWkDmRHs&hl=en&sa=X&ved=0ahUKEwiJnaiikIrLAhUM8CYKHZ8mBrcQ6AEILzAD#v=onepage&q=execute%20mongodb%20command%20in%20ipython&f=false/">Install MongoDB</a></p>
<p><a href="http://michaelcrump.net/how-to-run-html-files-in-your-browser-from-github/"> Run HTML files in your Browser from GitHub </a></p>
<p><a href="http://eberlitz.github.io/2015/09/18/data-wrangle-openstreetmaps-data/">Data Wrangling OpenStreetMap 1</a></p>
<p><a href="https://htmlpreview.github.io/?https://github.com/jdamiani27/Data-Wrangling-with-MongoDB/blob/master/Final_Project/OSM_wrangling.html#Top-Contributing-User">Data Wrangling OpenStreetMap 2</a></p>
<p><a href="http://stackoverflow.com/questions/6159074/given-the-lat-long-coordinates-how-can-we-find-out-the-city-country">Find the city from lat-long coordinates</a></p>
<p><a href="http://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-5-56">Disease Mapping</a></p>
<p><a href="https://myadventuresincoding.wordpress.com/2011/10/02/mongodb-geospatial-queries/">Mongodb geospatial queries</a></p>
<p><a href="http://tugdualgrall.blogspot.com/2014/08/introduction-to-mongodb-geospatial.html">Intro to mongodb geospatial</a></p>
<p><a href="http://www.longitude-latitude-maps.com/city/231_0,Vatican+City,Vatican+City">Long Lat Maps</a></p>
<p><a href="http://www.spatialcomplexity.info/files/2015/10/BATTY-JRSInterface-2015.pdf">City Boundaries</a></p>
<p><a href="http://www.innovation-cities.com/how-do-you-define-a-city-4-definitions-of-city-boundaries/1314">City Boundaries 2</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">os</span><span class="o">.</span><span class="n">killpg</span><span class="p">(</span><span class="n">pro</span><span class="o">.</span><span class="n">pid</span><span class="p">,</span> <span class="n">signal</span><span class="o">.</span><span class="n">SIGTERM</span><span class="p">)</span>  <span class="c"># Send the signal to all the process groups, killing the MongoDB instance</span>
</pre></div>

</div>
</div>
</div>

</div>
    </div>
  </div>
</body>
</html>
