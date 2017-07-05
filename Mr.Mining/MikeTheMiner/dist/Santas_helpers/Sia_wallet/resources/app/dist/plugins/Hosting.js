webpackJsonp([3],{10:function(e,t){e.exports=require("crypto")},101:function(e,t){e.exports=require("buffer")},102:function(e,t){e.exports=require("dgram")},103:function(e,t){e.exports=require("dns")},104:function(e,t){e.exports=require("events")},105:function(e,t){e.exports=require("string_decoder")},106:function(e,t){e.exports=require("zlib")},122:function(e,t,n){"use strict";t.b="UPDATE_MODAL";t.d="PUSH_SETTINGS";t.c="UPDATE_SETTINGS";t.a="UPDATE_DEFAULT_SETTINGS";t.e="FETCH_DATA";t.f="FETCH_DATA_SUCCESS";t.g="SHOW_TOGGLE_ACCEPTING_MODAL";t.h="HIDE_TOGGLE_ACCEPTING_MODAL";t.i="RESET_HOST";t.j="ADD_FOLDER";t.k="ADD_FOLDER_ASK";t.m="REMOVE_FOLDER";t.l="UPDATE_FOLDER_TO_REMOVE";t.n="RESIZE_FOLDER";t.o="SHOW_RESIZE_DIALOG";t.p="HIDE_RESIZE_DIALOG";t.q="ANNOUNCE_HOST";t.r="SHOW_ANNOUNCE_DIALOG";t.s="HIDE_ANNOUNCE_DIALOG";t.t="REQUEST_DEFAULT_SETTINGS";t.u="RECEIVE_DEFAULT_SETTINGS";t.v="GET_HOST_STATUS";t.w="SET_HOST_STATUS"},13:function(e,t){e.exports=require("util")},14:function(e,t){e.exports=require("path")},18:function(e,t){e.exports=require("electron")},23:function(e,t){e.exports=require("url")},26:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=n(79),o=(n.n(a),n(18)),i=(n.n(o),n(1)),s=n.n(i),c=n(49),r=n(14),l=n.n(r);const u=o.remote.dialog,d=o.remote.getCurrentWindow(),g=o.remote.getGlobal("config"),m=g.siad,f=o.remote.require("fs");let p=!1;const h=(e=0)=>new Promise(t=>setTimeout(t,e));window.onload=function(e){return function(){var t=e.apply(this,arguments);return new Promise(function(e,n){function a(o,i){try{var s=t[o](i),c=s.value}catch(e){return void n(e)}if(!s.done)return Promise.resolve(c).then(function(e){a("next",e)},function(e){a("throw",e)});e(c)}return a("next")})}}(function*(){const e=n(47);let t=function(){};const o=function(){let n="Siad exited unexpectedly for an unknown reason.";try{n=f.readFileSync(l.a.join(m.datadir,"siad-output.log"),{encoding:"utf-8"})}catch(e){console.error("error reading error log: "+e.toString())}document.body.innerHTML='<div style="width:100%;height:100%;" id="crashdiv"></div>',e.render(s.a.createElement(c.a,{errorMsg:n,startSiad:t}),document.getElementById("crashdiv"))};for(t=function(){const e=a.launch(m.path,{"sia-directory":m.datadir,"rpc-addr":m.rpcaddr,"host-addr":m.hostaddr,"api-addr":m.address,modules:"cghrtw"});e.on("error",o),e.on("close",o),e.on("exit",o),window.siadProcess=e};;){const e=yield a.isRunning(m.address);e&&p&&(p=!1,window.location.reload()),e||p||(p=!0,o()),yield h(2e3)}}),window.SiaAPI={call:function(e,t){a.call(m.address,e).then(e=>t(null,e)).catch(e=>t(e,null))},config:g,hastingsToSiacoins:a.hastingsToSiacoins,siacoinsToHastings:a.siacoinsToHastings,openFile:e=>u.showOpenDialog(d,e),saveFile:e=>u.showSaveDialog(d,e),showMessage:e=>u.showMessageBox(d,e),showError:e=>u.showErrorBox(e.title,e.content)}},264:function(e,t,n){"use strict";var a=n(1),o=n.n(a);const i=({title:title,message:message,actions:actions})=>{const e=()=>actions.acceptModal();const t=()=>actions.declineModal();return o.a.createElement("div",{className:"modal"},o.a.createElement("div",{className:"modal-message"},o.a.createElement("div",{className:"close-button",onClick:t},"X"),o.a.createElement("h3",null,title),o.a.createElement("p",null,message),o.a.createElement("p",null,o.a.createElement("input",{className:"button accept",type:"button",value:"Accept",onClick:e}),o.a.createElement("br",null),o.a.createElement("input",{className:"button cancel",type:"button",value:"Cancel",onClick:t}))))};t.a=i},265:function(e,t,n){"use strict";var a=n(107),o=n.n(a);const i=function(){const e=SiaAPI.openFile({title:"Choose new storage location.",properties:["openDirectory"]});return e?e[0]:void 0};t.a=i;const s=e=>SiaAPI.hastingsToSiacoins(e).times("1e12");t.g=s;const c=e=>SiaAPI.siacoinsToHastings(e).dividedBy("1e12");t.d=c;const r=e=>e.reduce((e,t)=>!isNaN(t.value)&&t.value>(t.min||0)&&e,!0);t.h=r;const l=e=>s(e).times("4320");t.f=l;const u=e=>c(e).dividedBy("4320");t.c=u;const d=e=>new o.a(e).dividedBy("1008");t.e=d;const g=e=>new o.a(e).times("1008");t.b=g},35:function(e,t){e.exports=require("http")},36:function(e,t){e.exports=require("stream")},377:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=n(1),o=n.n(a),i=n(47),s=n.n(i),c=n(4),r=n(121),l=n.n(r),u=n(3),d=(n.n(u),n(492)),g=n(495),m=n(475),f=n(87);const p=l()(),h=n.i(c.createStore)(d.a,n.i(c.applyMiddleware)(p)),E=o.a.createElement(u.Provider,{store:h},o.a.createElement(m.a,null));s.a.render(E,document.getElementById("react-root")),p.run(g.a),h.dispatch(f.a()),h.dispatch(f.b()),setInterval(()=>{h.dispatch(f.b());h.dispatch(f.c())},5e3),window.onfocus=(()=>{h.dispatch(f.b());h.dispatch(f.c())})},43:function(e,t){e.exports=require("assert")},474:function(e,t,n){"use strict";var a=n(1),o=n.n(a);const i=({announceAddress:announceAddress,actions:actions})=>{const e=e=>actions.updateModal("announceAddress",e.target.value);const t=e=>actions.hideAnnounceDialog(e);const n=()=>t("");const a=()=>{""!==announceAddress&&t(announceAddress)};const i=e=>{13===e.keyCode&&(a(),e.preventDefault())};return o.a.createElement("div",{className:"hosting-options-modal modal"+(void 0!==announceAddress?"":" hidden")},o.a.createElement("form",{className:"hosting-options modal-message",onSubmit:""},o.a.createElement("div",{className:"close-button",onClick:n},"X"),o.a.createElement("h3",null,"Announce Host"),o.a.createElement("p",null,o.a.createElement("label",null,"Address to announce."),o.a.createElement("input",{onChange:e,onKeyDown:i,value:announceAddress||"",type:"text"})),o.a.createElement("span",null,"Click to announce your host to the network. This will incur a small transaction fee and only needs to be done once per host."),o.a.createElement("p",null,o.a.createElement("input",{className:"button accept"+(""!==announceAddress?"":" disabled"),type:"button",value:"Announce",onClick:a}))))};t.a=i},475:function(e,t,n){"use strict";var a=n(1),o=n.n(a),i=n(487),s=n(485),c=n(488),r=n(484),l=n(490);const u=()=>o.a.createElement("div",{className:"app"},o.a.createElement(i.a,null),o.a.createElement(s.a,null),o.a.createElement(c.a,null),o.a.createElement(r.a,null),o.a.createElement(l.a,null));t.a=u},476:function(e,t,n){"use strict";var a=n(1),o=n.n(a),i=n(486),s=n(489);const c=({actions:actions})=>{const e=()=>actions.announceHost();return o.a.createElement("div",{className:"hosting"},o.a.createElement("div",{className:"help section"},o.a.createElement("div",{className:"property row"},o.a.createElement("div",{className:"title"},"Help"),o.a.createElement("div",{className:"controls"},o.a.createElement("div",{className:"button",id:"announce",onClick:e},o.a.createElement("i",{className:"fa fa-bullhorn"}),"Announce"))),o.a.createElement("div",{className:"property"},o.a.createElement("div",{className:"instructions"},"To start hosting:",o.a.createElement("ol",null,o.a.createElement("li",null,"Add a storage folder."),o.a.createElement("li",null,"Set your prefered price, bandwidth cost, collateral, and duration."),o.a.createElement("li",null,"Set 'Accepting Contracts' to 'Yes'"),o.a.createElement("li",null,"Announce your host by clicking the above 'Announce' button."))))),o.a.createElement(s.a,null),o.a.createElement(i.a,null))};t.a=c},477:function(e,t,n){"use strict";var a=n(2),o=n.n(a),i=n(1),s=n.n(i),c=n(7),r=(n.n(c),n(264)),l=n(14),u=n.n(l);const d=({folders:folders,folderPathToRemove:folderPathToRemove,actions:actions})=>{const e=()=>actions.addFolderAskPathSize();const t=e=>()=>{actions.removeFolder(e);actions.updateFolderToRemove()};const n=e=>()=>actions.resizeFolder(e);const a=e=>()=>actions.updateFolderToRemove(e.get("path"));const o=()=>actions.updateFolderToRemove();const i=folders.sortBy(e=>e.get("path"));const c=i.map((e,i)=>s.a.createElement("div",{className:"property pure-g",key:i},s.a.createElement("div",{className:"pure-u-3-4"},s.a.createElement("div",{className:"name"},e.get("path"))),s.a.createElement("div",{className:"pure-u-1-12"},s.a.createElement("div",null,Math.floor(e.get("free")).toString()," GB")),s.a.createElement("div",{className:"pure-u-1-12"},s.a.createElement("div",null,Math.floor(e.get("size")).toString()," GB")),s.a.createElement("div",{className:"pure-u-1-24",onClick:n(e)},s.a.createElement("div",null,s.a.createElement("i",{className:"fa fa-edit button"}))),s.a.createElement("div",{className:"pure-u-1-24",onClick:a(e)},s.a.createElement("div",null,s.a.createElement("i",{className:"fa fa-remove button"}))),folderPathToRemove&&folderPathToRemove===e.get("path")?s.a.createElement(r.a,{title:`Remove "${u.a.basename(e.get("path"))}"?`,message:"No longer use this folder for storage? You may lose collateral if you do not have enough space to fill all contracts.",actions:{acceptModal:t(e),declineModal:o}}):null));return s.a.createElement("div",{className:"files section"},s.a.createElement("div",{className:"property row"},s.a.createElement("div",{className:"title"}),s.a.createElement("div",{className:"controls full"},s.a.createElement("div",{className:"button left",id:"edit",onClick:e},s.a.createElement("i",{className:"fa fa-folder-open"}),"Add Storage Folder"),s.a.createElement("div",{className:"pure-u-1-12",style:{textAlign:"left"}},"Free"),s.a.createElement("div",{className:"pure-u-1-12",style:{textAlign:"left"}},"Max"),s.a.createElement("div",{className:"pure-u-1-12"}))),c)};d.propTypes={folderPathToRemove:o.a.string,folders:o.a.instanceOf(c.List).isRequired},t.a=d},478:function(e,t,n){"use strict";var a=n(1),o=n.n(a),i=n(107),s=n.n(i),c=n(483),r=n(479);const l=({numContracts:numContracts,earned:earned,expected:expected,walletsize:walletsize,walletLocked:walletLocked,workingstatus:workingstatus,connectabilitystatus:connectabilitystatus})=>o.a.createElement("header",{className:"header"},o.a.createElement("div",{className:"title"},"Hosting"),o.a.createElement("div",{className:"capsule"},o.a.createElement("div",{className:"pod"},o.a.createElement(r.a,{workingstatus:workingstatus,connectabilitystatus:connectabilitystatus})),o.a.createElement("div",{className:"pod",id:"contacts"},numContracts," active contracts"),o.a.createElement("div",{className:"pod",id:"money"},earned," SC earned"),o.a.createElement("div",{className:"pod",id:"expected"},expected," SC expected")),new s.a(walletsize).lessThan("2000")&&!walletLocked?o.a.createElement(c.a,{title:"Wallet balance too low.",message:"You must have at least 2,000 SC to host files."}):null);t.a=l},479:function(e,t,n){"use strict";var a=n(2),o=n.n(a),i=n(1),s=n.n(i);const c=({connectabilitystatus:connectabilitystatus,workingstatus:workingstatus})=>{if("checking"===connectabilitystatus&&"checking"===workingstatus)return s.a.createElement("div",{className:"host-status"},s.a.createElement("i",{className:"fa fa-refresh fa-spin inactive-icon"}),s.a.createElement("span",null," Checking Host Status... "),s.a.createElement("div",{className:"host-status-info"},"Sia-UI is determining the status of your Host."));if("not connectable"===connectabilitystatus&&"not working"===workingstatus)return s.a.createElement("div",{className:"host-status"},s.a.createElement("i",{className:"fa fa-times offline-icon"}),s.a.createElement("span",null," Host Unreachable "),s.a.createElement("div",{className:"host-status-info"},"Your host is not connectable at the configured net address. Check your UPNP or NAT settings."));if("connectable"===connectabilitystatus&&"not working"===workingstatus)return s.a.createElement("div",{className:"host-status"},s.a.createElement("i",{className:"fa fa-times inactive-icon"}),s.a.createElement("span",null," Host Inactive "),s.a.createElement("div",{className:"host-status-info"},"Your host is connectable, but it is not being used by any renters."));return s.a.createElement("div",{className:"host-status"},s.a.createElement("i",{className:"fa fa-check online-icon"}),s.a.createElement("span",null," Host Online "),s.a.createElement("div",{className:"host-status-info"},"Your host is connectable and is being contacted by renters."))};c.propTypes={connectabilitystatus:o.a.string.isRequired,workingstatus:o.a.string.isRequired},t.a=c},48:function(e,t){e.exports=require("querystring")},480:function(e,t,n){"use strict";var a=n(1),o=n.n(a),i=n(7),s=(n.n(i),n(14)),c=n.n(s);const r=({resizePath:resizePath,resizeSize:resizeSize,initialSize:initialSize,actions:actions})=>{const e=e=>actions.updateModal("resizeSize",e.target.value);const t=e=>actions.hideResizeDialog(n.i(i.Map)({path:resizePath,size:e}));const a=()=>t(0);const s=()=>{resizeSize>=35&&resizeSize!==initialSize.toString()&&t(resizeSize)};const r=e=>{13===e.keyCode&&(s(),e.preventDefault())};return o.a.createElement("div",{className:"hosting-options-modal modal"+(resizePath?"":" hidden")},o.a.createElement("form",{className:"hosting-options modal-message",onSubmit:""},o.a.createElement("div",{className:"close-button",onClick:a},"X"),o.a.createElement("h3",null,'Resize "',c.a.basename(resizePath),'"'),o.a.createElement("p",null,o.a.createElement("label",null,"Size in GB (Min is 35 GB)"),o.a.createElement("input",{type:"number",onChange:e,onKeyDown:r,value:resizeSize,min:"35"})),o.a.createElement("span",{className:"error"+(resizeSize<35?"":" hidden")},"Storage folder must be at least 35 GB."),o.a.createElement("p",null,o.a.createElement("input",{className:"button accept"+(resizeSize!==initialSize.toString()&&resizeSize>=35?"":" disabled"),type:"button",value:"Save",onClick:s}))))};t.a=r},481:function(e,t,n){"use strict";var a=n(1),o=n.n(a),i=n(265),s=n(264);const c=({acceptingContracts:acceptingContracts,usersettings:usersettings,defaultsettings:defaultsettings,settingsChanged:settingsChanged,shouldShowToggleAcceptingModal:shouldShowToggleAcceptingModal,actions:actions})=>{const e=e=>{if(e.target.value>=0){const t=e.target.attributes.getNamedItem("data-setting").value;actions.updateSettings(usersettings.map((n,a)=>a===t?e.target.value:n.get("value")))}};const t=(e,t)=>t.map(e=>e.get("value")).set("acceptingContracts",e);const n=()=>i.h(usersettings.toList().toJSON())&&settingsChanged;const a=()=>actions.pushSettings(defaultsettings.set("acceptingContracts",acceptingContracts));const c=()=>{n()&&actions.pushSettings(t(acceptingContracts,usersettings))};const r=()=>actions.showToggleAcceptingModal();const l=()=>actions.hideToggleAcceptingModal();const u=()=>{actions.pushSettings(t(!acceptingContracts,usersettings));l()};const d=usersettings.map((t,n)=>o.a.createElement("div",{className:"property pure-g",key:n},o.a.createElement("div",{className:"pure-u-1-2"},o.a.createElement("div",{className:"name"},t.get("name"))),o.a.createElement("div",{className:"pure-u-1-2"},o.a.createElement("div",{className:"value"},o.a.createElement("input",{type:"number","data-setting":n,onChange:e,className:"value",value:t.get("value")}))),o.a.createElement("div",{className:"error pure-u-1-1"+(t.get("value")<=Number(t.get("min")||0)||isNaN(t.get("value"))?"":" hidden")},o.a.createElement("span",null,"Must be a number greater than ",t.get("min")||"zero",".")))).toList();return o.a.createElement("div",{className:"settings section"},o.a.createElement("div",{className:"property row"},o.a.createElement("div",{className:"title"},"Configurations"),o.a.createElement("div",{className:"controls"},o.a.createElement("div",{className:"button"+(n()?"":" disable"),onClick:c},o.a.createElement("i",{className:"fa fa-save"}),"Save"),o.a.createElement("div",{className:"button",onClick:a},o.a.createElement("i",{className:"fa fa-refresh"}),"Reset"))),d,o.a.createElement("div",{className:"property pure-g"},o.a.createElement("div",{className:"pure-u-1-2"},o.a.createElement("div",{className:"name"},"Accepting Contracts")),o.a.createElement("div",{className:"pure-u-1-2"},o.a.createElement("div",{className:"value"},o.a.createElement("div",{className:"toggle-switch"+(acceptingContracts?"":" off"),onClick:r},o.a.createElement("div",{className:"toggle-inner"}))))),shouldShowToggleAcceptingModal&&acceptingContracts?o.a.createElement(s.a,{title:"Stop accepting contracts?",message:"You must still keep Sia-UI open until the existing contracts have expired otherwise you will lose collateral.",actions:{acceptModal:u,declineModal:l}}):null,shouldShowToggleAcceptingModal&&!acceptingContracts?o.a.createElement(s.a,{title:"Start accepting contracts?",message:"To host files you must keep the Sia-UI open. Collateral will also be locked and you will be unable to spend that SC until the contract is expired.",actions:{acceptModal:u,declineModal:l}}):null)};t.a=c},482:function(e,t,n){"use strict";var a=n(1),o=n.n(a);const i=({walletLocked:walletLocked})=>o.a.createElement("div",{className:"hosting-options-modal modal"+(walletLocked?"":" hidden")},o.a.createElement("div",{className:"hosting-options modal-message"},o.a.createElement("h3",null,"You must unlock the wallet to host files."),o.a.createElement("i",{className:"fa fa-lock fa-4x"})));t.a=i},483:function(e,t,n){"use strict";var a=n(1),o=n.n(a);const i=({title:title,message:message})=>o.a.createElement("div",{className:"warning-bar"},o.a.createElement("div",{className:"warning-bar-modal-message"},o.a.createElement("h3",null,title),o.a.createElement("p",null,message)));t.a=i},484:function(e,t,n){"use strict";var a=n(474),o=n(3),i=(n.n(o),n(87)),s=n(4);const c=e=>({shouldShowAnnounceDialog:e.modalReducer.get("shouldShowAnnounceDialog"),announceAddress:e.modalReducer.get("announceAddress")}),r=e=>({actions:n.i(s.bindActionCreators)({hideAnnounceDialog:i.j,updateModal:i.k},e)}),l=n.i(o.connect)(c,r)(a.a);t.a=l},485:function(e,t,n){"use strict";var a=n(476),o=n(3),i=(n.n(o),n(87)),s=n(4);const c=e=>({actions:n.i(s.bindActionCreators)({updateSettings:i.m,announceHost:i.n},e)}),r=e=>({usersettings:e.hostingReducer.get("usersettings"),defaultsettings:e.hostingReducer.get("defaultsettings"),acceptingContracts:e.hostingReducer.get("acceptingContracts"),files:e.hostingReducer.get("files")}),l=n.i(o.connect)(r,c)(a.a);t.a=l},486:function(e,t,n){"use strict";var a=n(477),o=n(3),i=(n.n(o),n(87)),s=n(4);const c=e=>({actions:n.i(s.bindActionCreators)({addFolderAskPathSize:i.o,removeFolder:i.p,resizeFolder:i.q,updateFolderToRemove:i.r},e)}),r=e=>({folders:e.hostingReducer.get("files"),folderPathToRemove:e.modalReducer.get("folderPathToRemove")}),l=n.i(o.connect)(r,c)(a.a);t.a=l},487:function(e,t,n){"use strict";var a=n(478),o=n(3);n.n(o);const i=e=>({numContracts:e.hostingReducer.get("numContracts"),storage:e.hostingReducer.get("storage"),earned:e.hostingReducer.get("earned"),expected:e.hostingReducer.get("expected"),walletsize:e.hostingReducer.get("walletsize"),walletLocked:e.hostingReducer.get("walletLocked"),connectabilitystatus:e.hostingReducer.get("connectabilitystatus"),workingstatus:e.hostingReducer.get("workingstatus")}),s=n.i(o.connect)(i)(a.a);t.a=s},488:function(e,t,n){"use strict";var a=n(480),o=n(3),i=(n.n(o),n(87)),s=n(4);const c=e=>({resizePath:e.modalReducer.get("resizePath"),resizeSize:e.modalReducer.get("resizeSize"),initialSize:e.modalReducer.get("initialSize")}),r=e=>({actions:n.i(s.bindActionCreators)({hideResizeDialog:i.l,updateModal:i.k},e)}),l=n.i(o.connect)(c,r)(a.a);t.a=l},489:function(e,t,n){"use strict";var a=n(481),o=n(3),i=(n.n(o),n(87)),s=n(4),c=n(7);n.n(c);const r=e=>({actions:n.i(s.bindActionCreators)({showToggleAcceptingModal:i.s,hideToggleAcceptingModal:i.t,updateSettings:i.m,pushSettings:i.u},e)}),l=e=>({usersettings:n.i(c.Map)({maxduration:n.i(c.Map)({name:"Max Duration (Weeks)",value:e.settingsReducer.get("maxduration"),min:12}),collateral:n.i(c.Map)({name:"Collateral per TB per Month (SC)",value:e.settingsReducer.get("collateral")}),storageprice:n.i(c.Map)({name:"Price per TB per Month (SC)",value:e.settingsReducer.get("storageprice")}),downloadbandwidthprice:n.i(c.Map)({name:"Bandwidth Price (SC/TB)",value:e.settingsReducer.get("downloadbandwidthprice")})}),acceptingContracts:e.settingsReducer.get("acceptingContracts"),settingsChanged:e.settingsReducer.get("settingsChanged"),defaultsettings:e.settingsReducer.get("defaultsettings"),shouldShowToggleAcceptingModal:e.modalReducer.get("shouldShowToggleAcceptingModal")}),u=n.i(o.connect)(l,r)(a.a);t.a=u},49:function(e,t,n){"use strict";var a=n(2),o=n.n(a),i=n(1),s=n.n(i),c=n(18);n.n(c);const r={display:"flex",alignItems:"center",justifyContent:"center",flexDirection:"column",backgroundColor:"#C6C6C6",width:"100%",height:"100%"},l={height:"300px",width:"80%",overflow:"auto",marginBottom:"15px"},u={color:"blue",cursor:"pointer"},d=()=>{c.shell.openExternal("https://github.com/NebulousLabs/Sia/issues")},g=({errorMsg:errorMsg,startSiad:startSiad})=>s.a.createElement("div",{style:r},s.a.createElement("h2",null,"Siad has exited unexpectedly. Please submit a bug report including the error log ",s.a.createElement("a",{style:u,onClick:d},"here.")),s.a.createElement("h2",null," Error Log: "),s.a.createElement("textarea",{style:l,readOnly:!0},errorMsg),s.a.createElement("button",{onClick:startSiad},"Start Siad"));g.propTypes={errorMsg:o.a.string.isRequired,startSiad:o.a.func.isRequired},t.a=g},490:function(e,t,n){"use strict";var a=n(482),o=n(3);n.n(o);const i=e=>({walletLocked:e.hostingReducer.get("walletLocked")}),s=n.i(o.connect)(i)(a.a);t.a=s},491:function(e,t,n){"use strict";function a(e=s,t){switch(t.type){case i.w:return e.set("workingstatus",t.working).set("connectabilitystatus",t.connectable);case i.f:return e.merge(t.data);default:return e}}t.a=a;var o=n(7),i=(n.n(o),n(122));const s=n.i(o.Map)({numContracts:0,storage:0,earned:0,expected:0,walletLocked:!0,walletsize:0,files:n.i(o.List)([]),workingstatus:"checking",connectabilitystatus:"checking"})},492:function(e,t,n){"use strict";var a=n(4),o=n(491),i=n(494),s=n(493);const c=n.i(a.combineReducers)({hostingReducer:o.a,settingsReducer:i.a,modalReducer:s.a});t.a=c},493:function(e,t,n){"use strict";function a(e=s,t){switch(t.type){case i.b:return e.set(t.key,t.value);case i.g:return e.set("shouldShowToggleAcceptingModal",!0);case i.h:return e.set("shouldShowToggleAcceptingModal",!1);case i.o:return e.set("resizePath",t.folder.get("path")).set("resizeSize",t.folder.get("size")).set("initialSize",t.ignoreInitial?0:t.folder.get("size"));case i.p:return e.set("resizePath","");case i.s:return e.set("announceAddress",void 0);case i.r:return e.set("announceAddress",t.address||e.get("defaultAnnounceAddress"));case i.l:return e.set("folderPathToRemove",t.folder||"");case i.f:return e.merge(t.modals);default:return e}}t.a=a;var o=n(7),i=(n.n(o),n(122));const s=n.i(o.Map)({resizeSize:0,initialSize:0,resizePath:"",folderPathToRemove:"",announceAddress:void 0,defaultAnnounceAddress:"",shouldShowToggleAcceptingModal:!1})},494:function(e,t,n){"use strict";function a(e=s,t){switch(t.type){case i.c:return e.merge(t.settings).set("settingsChanged",!0);case i.d:return e.set("defaultsettings",t.settings).set("settingsChanged",!1);case i.u:return e.set("defaultsettings",t.settings).merge(t.settings);case i.f:return e.get("settingsChanged")?e:e.merge(t.settings);default:return e}}t.a=a;var o=n(7),i=(n.n(o),n(122));const s=n.i(o.Map)({maxduration:0,collateral:0,storageprice:0,downloadbandwidthprice:0,acceptingContracts:!1,defaultsettings:n.i(o.Map)(),settingsChanged:!1})},495:function(e,t,n){"use strict";function a(e){return function(){var t=e.apply(this,arguments);return new Promise(function(e,n){function a(o,i){try{var s=t[o](i),c=s.value}catch(e){return void n(e)}if(!s.done)return Promise.resolve(c).then(function(e){a("next",e)},function(e){a("throw",e)});e(c)}return a("next")})}}function*o(e){try{yield n.i(k.put)(A.d(e.address));const t=yield n.i(k.take)(C.s);""!==t.address&&(yield M({url:"/host/announce",timeout:3e4,method:"POST",qs:{netaddress:t.address}}))}catch(e){SiaAPI.showError({title:"Error Announcing Host",content:e.message})}}function*i(e){try{yield M({url:"/host/storage/folders/add",method:"POST",timeout:17e7,qs:{path:e.folder.get("path"),size:e.folder.get("size")}}),yield n.i(k.put)(A.b())}catch(e){SiaAPI.showError({title:"Error Adding Folder",content:e.message})}}function*s(){const e=T.a();if(e)try{yield n.i(k.put)(A.e(n.i(z.Map)({path:e,size:50}),!0));const t=yield n.i(k.take)(C.p),a=new R.a(t.folder.get("size")).times(1e9),o=yield _(a);t.folder.get("size")&&(yield n.i(k.put)(A.f(n.i(z.Map)({path:e,size:o}))))}catch(e){SiaAPI.showError({title:"Error Adding Folder",content:e.message})}}function*c(e){try{yield M({url:"/host/storage/folders/remove",timeout:17e7,method:"POST",qs:{path:e.folder.get("path")}}),yield n.i(k.put)(A.b())}catch(e){SiaAPI.showError({title:"Error Removing Folder",content:e.message})}}function*r(e){try{yield n.i(k.put)(A.e(e.folder,e.ignoreInitial));const t=yield n.i(k.take)(C.p),a=new R.a(t.folder.get("size")).times(1e9),o=yield _(a);t.folder.get("size")&&(yield M({url:"/host/storage/folders/resize",timeout:17e7,method:"POST",qs:{path:t.folder.get("path"),newsize:o}}),yield n.i(k.put)(A.b()))}catch(e){SiaAPI.showError({title:"Error Resizing Folder",content:e.message})}}function*l(e){try{yield M({url:"/host",method:"POST",qs:{acceptingcontracts:e.settings.get("acceptingContracts"),maxduration:T.b(e.settings.get("maxduration")).toString(),collateral:T.c(e.settings.get("collateral")).toString(),minstorageprice:T.c(e.settings.get("storageprice")).toString(),mindownloadbandwidthprice:T.d(e.settings.get("downloadbandwidthprice")).toString()}}),yield n.i(k.put)(A.b())}catch(e){SiaAPI.showError({title:"Error Updating Settings",content:e.message})}}function*u(){try{const e=yield M({url:"/host"}),t=yield M({url:"/wallet"}),a=n.i(z.Map)({numContracts:e.financialmetrics.contractcount,storage:new R.a(e.externalsettings.totalstorage).minus(new R.a(e.externalsettings.remainingstorage)).toString(),earned:SiaAPI.hastingsToSiacoins(O(e.financialmetrics)).round(2).toString(),expected:SiaAPI.hastingsToSiacoins(D(e.financialmetrics)).round(2).toString(),files:yield P(),walletLocked:!t.unlocked,walletsize:t.confirmedsiacoinbalance}),o=n.i(z.Map)({defaultAnnounceAddress:e.externalsettings.netaddress}),i=I(e);yield n.i(k.put)(A.g(a,i,o))}catch(e){console.error("error fetching host data: "+e.toString())}}function*d(){try{const e=yield M("/host");yield n.i(k.put)(A.h(I(e)))}catch(e){console.error("error fetching defaults: "+e.toString())}}function*g(){try{const e=yield M("/host");yield n.i(k.put)(A.i(e.connectabilitystatus,e.workingstatus))}catch(e){console.error("error fetching host status: "+e.toString())}}function*m(){yield*n.i(N.takeEvery)(C.d,l)}function*f(){yield*n.i(N.takeEvery)(C.e,u)}function*p(){yield*n.i(N.takeEvery)(C.j,i)}function*h(){yield*n.i(N.takeEvery)(C.k,s)}function*E(){yield*n.i(N.takeEvery)(C.m,c)}function*v(){yield*n.i(N.takeEvery)(C.n,r)}function*y(){yield*n.i(N.takeEvery)(C.q,o)}function*w(){yield*n.i(N.takeEvery)(C.t,d)}function*S(){yield*n.i(N.takeEvery)(C.v,g)}function*b(){yield[n.i(k.fork)(m),n.i(k.fork)(f),n.i(k.fork)(p),n.i(k.fork)(h),n.i(k.fork)(E),n.i(k.fork)(v),n.i(k.fork)(y),n.i(k.fork)(w),n.i(k.fork)(S)]}t.a=b;var N=n(121),k=(n.n(N),n(133)),A=(n.n(k),n(87)),C=n(122),T=n(265),z=n(7),x=(n.n(z),n(107)),R=n.n(x);const M=e=>new Promise((t,n)=>{SiaAPI.call(e,(e,a)=>{e?n(e):t(a)})}),P=()=>new Promise((e,t)=>{M({url:"/host/storage",method:"GET"}).then(t=>{e(n.i(z.List)((t.folders||[]).map(e=>n.i(z.Map)({path:e.path,size:new R.a(e.capacity).times("1e-9").toString(),free:new R.a(e.capacityremaining).times("1e-9").toString()}))))}).catch(t)}),_=(()=>{var e=a(function*(e){const t=yield M("/host"),n=e.minus(e.modulo(64*t.externalsettings.sectorsize));return n.isNegative()?"0":n.toString()});return function(t){return e.apply(this,arguments)}})(),I=e=>n.i(z.Map)({maxduration:T.e(e.externalsettings.maxduration).toFixed(0),collateral:T.f(e.externalsettings.collateral).toFixed(0),storageprice:T.f(e.externalsettings.storageprice).toFixed(0),downloadbandwidthprice:T.g(e.externalsettings.downloadbandwidthprice).toString(),acceptingContracts:e.externalsettings.acceptingcontracts}),D=e=>{const t=new R.a(e.potentialstoragerevenue);const n=new R.a(e.potentialdownloadbandwidthrevenue).add(e.potentialuploadbandwidthrevenue);const a=new R.a(e.potentialcontractcompensation);return t.add(n).add(a)},O=e=>{const t=new R.a(e.storagerevenue);const n=new R.a(e.downloadbandwidthrevenue).add(e.uploadbandwidthrevenue);const a=new R.a(e.contractcompensation);return t.add(n).add(a)}},55:function(e,t){e.exports=require("fs")},61:function(e,t){e.exports=require("https")},71:function(e,t){e.exports=require("net")},72:function(e,t){function n(e){throw new Error("Cannot find module '"+e+"'.")}n.keys=function(){return[]},n.resolve=n,e.exports=n,n.id=72},81:function(e,t){e.exports=require("child_process")},82:function(e,t){e.exports=require("punycode")},83:function(e,t){e.exports=require("tls")},84:function(e,t){function n(e){throw new Error("Cannot find module '"+e+"'.")}n.keys=function(){return[]},n.resolve=n,e.exports=n,n.id=84},87:function(e,t,n){"use strict";var a=n(122);const o=(e=>({type:a.a,newvalue:e}),(e,t)=>({type:a.b,key:e,value:t}));t.k=o;const i=e=>({type:a.c,settings:e});t.m=i;const s=e=>({type:a.d,settings:e});t.u=s;const c=e=>({type:a.e,ignoreSettings:e});t.b=c;const r=(e,t,n)=>({type:a.f,data:e,settings:t,modals:n});t.g=r;const l=()=>({type:a.g});t.s=l;const u=()=>({type:a.h});t.t=u;const d=(()=>({type:a.i}),e=>({type:a.j,folder:e}));t.f=d;const g=()=>({type:a.k});t.o=g;const m=e=>({type:a.l,folder:e});t.r=m;const f=e=>({type:a.m,folder:e});t.p=f;const p=(e,t)=>({type:a.n,folder:e,ignoreInitial:t});t.q=p;const h=(e,t)=>({type:a.o,folder:e,ignoreInitial:t});t.e=h;const E=e=>({type:a.p,folder:e});t.l=E;const v=e=>({type:a.q,address:e});t.n=v;const y=e=>({type:a.r,address:e});t.d=y;const w=e=>({type:a.s,address:e});t.j=w;const S=()=>({type:a.t});t.a=S;const b=e=>({type:a.u,settings:e});t.h=b;const N=()=>({type:a.v});t.c=N;const k=(e,t)=>({type:a.w,connectable:e,working:t});t.i=k},988:function(e,t,n){n(37),n(26),e.exports=n(377)}},[988]);