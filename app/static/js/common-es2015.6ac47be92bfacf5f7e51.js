(window.webpackJsonp=window.webpackJsonp||[]).push([[1],{ZjcB:function(e,n,s){"use strict";s.d(n,"a",(function(){return p}));var t=s("fXoL"),o=s("ZF+8"),g=s("ofXK");function c(e,n){if(1&e&&(t.Rb(0,"span"),t.zc(1),t.Qb()),2&e){const e=t.bc().$implicit;t.zb(1),t.Ac(e.title?e.title:"Error")}}function r(e,n){if(1&e&&(t.Rb(0,"span"),t.zc(1),t.Qb()),2&e){const e=t.bc().$implicit;t.zb(1),t.Ac(e.title?e.title:"Success")}}function i(e,n){if(1&e&&(t.Rb(0,"span"),t.zc(1),t.Qb()),2&e){const e=t.bc().$implicit;t.zb(1),t.Ac(e.title?e.title:"Info")}}function a(e,n){if(1&e&&(t.Rb(0,"span"),t.zc(1),t.Qb()),2&e){const e=t.bc().$implicit;t.zb(1),t.Ac(e.title?e.title:"Warning")}}function m(e,n){if(1&e){const e=t.Sb();t.Rb(0,"div"),t.Rb(1,"div",2),t.Rb(2,"strong",3),t.xc(3,c,2,1,"span",4),t.xc(4,r,2,1,"span",4),t.xc(5,i,2,1,"span",4),t.xc(6,a,2,1,"span",4),t.Qb(),t.Rb(7,"button",5),t.Zb("click",(function(){t.rc(e);const s=n.index;return t.bc(2).close(s)})),t.Rb(8,"span",6),t.zc(9,"\xd7"),t.Qb(),t.Qb(),t.Qb(),t.Rb(10,"div",7),t.zc(11),t.Qb(),t.Qb()}if(2&e){const e=n.$implicit;t.Cb("message message-",e.type,""),t.zb(3),t.hc("ngIf","error"===e.type),t.zb(1),t.hc("ngIf","success"===e.type),t.zb(1),t.hc("ngIf","info"===e.type),t.zb(1),t.hc("ngIf","warning"===e.type),t.zb(5),t.Bc(" ",e.message," ")}}function b(e,n){if(1&e&&(t.Rb(0,"div"),t.xc(1,m,12,8,"div",1),t.Qb()),2&e){const e=t.bc();t.Cb("message-group message-",e.position,""),t.zb(1),t.hc("ngForOf",e.messages)}}let p=(()=>{class e{constructor(e){this._ms=e,this.messages=[],this.position||(this.position="bottom-right"),this.msgSubscription=this._ms.getMessages().subscribe(e=>{this.messages=e})}ngOnDestroy(){this.msgSubscription.unsubscribe()}ngOnInit(){}close(e){this._ms.clearSingleMessage(e)}}return e.\u0275fac=function(n){return new(n||e)(t.Lb(o.b))},e.\u0275cmp=t.Fb({type:e,selectors:[["app-message"]],inputs:{position:"position"},decls:1,vars:1,consts:[[3,"class",4,"ngIf"],[3,"class",4,"ngFor","ngForOf"],[1,"message-header"],[1,"mr-auto"],[4,"ngIf"],["type","button",1,"ml-2","mb-1","close",3,"click"],["aria-hidden","true"],[1,"message-body"]],template:function(e,n){1&e&&t.xc(0,b,2,4,"div",0),2&e&&t.hc("ngIf",n.messages.length>0)},directives:[g.l,g.k],styles:[".message-group[_ngcontent-%COMP%]{max-width:350px;position:fixed;z-index:100000000000000}.message-group[_ngcontent-%COMP%]   .message[_ngcontent-%COMP%]{width:100%;overflow:hidden;box-shadow:0 .25rem .75rem rgba(0,0,0,.1);border-radius:.25rem;transition:opacity .15s linear;display:block;opacity:1;padding:.7rem;border:1px solid rgba(0,0,0,.1);border-left:10px solid #ccc;background-color:#fff}.message-group[_ngcontent-%COMP%]   .message[_ngcontent-%COMP%]:not(:last-child){margin-bottom:.75rem}.message-group[_ngcontent-%COMP%]   .message[_ngcontent-%COMP%]   .message-header[_ngcontent-%COMP%]{margin-bottom:.5rem}.message-group[_ngcontent-%COMP%]   .message[_ngcontent-%COMP%]   .message-header[_ngcontent-%COMP%]   strong[_ngcontent-%COMP%]{font-size:16px;font-weight:700}.message-group[_ngcontent-%COMP%]   .message[_ngcontent-%COMP%]   .message-body[_ngcontent-%COMP%]{line-height:1.6;font-size:14px}.message-group[_ngcontent-%COMP%]   .message.message-error[_ngcontent-%COMP%]{border-left-color:#ff5722}.message-group[_ngcontent-%COMP%]   .message.message-error[_ngcontent-%COMP%]   .message-header[_ngcontent-%COMP%]{color:#ff5722}.message-group[_ngcontent-%COMP%]   .message.message-success[_ngcontent-%COMP%]{border-left-color:#4caf50}.message-group[_ngcontent-%COMP%]   .message.message-success[_ngcontent-%COMP%]   .message-header[_ngcontent-%COMP%]{color:#4caf50}.message-group[_ngcontent-%COMP%]   .message.message-info[_ngcontent-%COMP%]{border-left-color:#4184f3}.message-group[_ngcontent-%COMP%]   .message.message-info[_ngcontent-%COMP%]   .message-header[_ngcontent-%COMP%]{color:#4184f3}.message-group[_ngcontent-%COMP%]   .message.message-warning[_ngcontent-%COMP%]{border-left-color:#ffbf00}.message-group[_ngcontent-%COMP%]   .message.message-warning[_ngcontent-%COMP%]   .message-header[_ngcontent-%COMP%]{color:#ffbf00}.message-group.message-bottom-right[_ngcontent-%COMP%]{bottom:1rem;right:1rem}.message-group.message-bottom-center[_ngcontent-%COMP%]{bottom:1rem;left:50%}.message-group.message-bottom-left[_ngcontent-%COMP%]{left:1rem;bottom:1rem}.message-group.message-top-right[_ngcontent-%COMP%]{top:5rem;right:1rem}.message-group.message-top-center[_ngcontent-%COMP%]{top:5rem;left:50%}.message-group.message-top-left[_ngcontent-%COMP%]{top:5rem;left:1rem}"]}),e})()}}]);