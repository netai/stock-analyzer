function _classCallCheck(e,n){if(!(e instanceof n))throw new TypeError("Cannot call a class as a function")}function _defineProperties(e,n){for(var t=0;t<n.length;t++){var s=n[t];s.enumerable=s.enumerable||!1,s.configurable=!0,"value"in s&&(s.writable=!0),Object.defineProperty(e,s.key,s)}}function _createClass(e,n,t){return n&&_defineProperties(e.prototype,n),t&&_defineProperties(e,t),e}(window.webpackJsonp=window.webpackJsonp||[]).push([[1],{ZjcB:function(e,n,t){"use strict";t.d(n,"a",(function(){return f}));var s=t("fXoL"),o=t("ZF+8"),g=t("ofXK");function r(e,n){if(1&e&&(s.Rb(0,"span"),s.zc(1),s.Qb()),2&e){var t=s.bc().$implicit;s.zb(1),s.Ac(t.title?t.title:"Error")}}function c(e,n){if(1&e&&(s.Rb(0,"span"),s.zc(1),s.Qb()),2&e){var t=s.bc().$implicit;s.zb(1),s.Ac(t.title?t.title:"Success")}}function a(e,n){if(1&e&&(s.Rb(0,"span"),s.zc(1),s.Qb()),2&e){var t=s.bc().$implicit;s.zb(1),s.Ac(t.title?t.title:"Info")}}function i(e,n){if(1&e&&(s.Rb(0,"span"),s.zc(1),s.Qb()),2&e){var t=s.bc().$implicit;s.zb(1),s.Ac(t.title?t.title:"Warning")}}function m(e,n){if(1&e){var t=s.Sb();s.Rb(0,"div"),s.Rb(1,"div",2),s.Rb(2,"strong",3),s.xc(3,r,2,1,"span",4),s.xc(4,c,2,1,"span",4),s.xc(5,a,2,1,"span",4),s.xc(6,i,2,1,"span",4),s.Qb(),s.Rb(7,"button",5),s.Zb("click",(function(){s.rc(t);var e=n.index;return s.bc(2).close(e)})),s.Rb(8,"span",6),s.zc(9,"\xd7"),s.Qb(),s.Qb(),s.Qb(),s.Rb(10,"div",7),s.zc(11),s.Qb(),s.Qb()}if(2&e){var o=n.$implicit;s.Cb("message message-",o.type,""),s.zb(3),s.hc("ngIf","error"===o.type),s.zb(1),s.hc("ngIf","success"===o.type),s.zb(1),s.hc("ngIf","info"===o.type),s.zb(1),s.hc("ngIf","warning"===o.type),s.zb(5),s.Bc(" ",o.message," ")}}function b(e,n){if(1&e&&(s.Rb(0,"div"),s.xc(1,m,12,8,"div",1),s.Qb()),2&e){var t=s.bc();s.Cb("message-group message-",t.position,""),s.zb(1),s.hc("ngForOf",t.messages)}}var f=function(){var e=function(){function e(n){var t=this;_classCallCheck(this,e),this._ms=n,this.messages=[],this.position||(this.position="bottom-right"),this.msgSubscription=this._ms.getMessages().subscribe((function(e){t.messages=e}))}return _createClass(e,[{key:"ngOnDestroy",value:function(){this.msgSubscription.unsubscribe()}},{key:"ngOnInit",value:function(){}},{key:"close",value:function(e){this._ms.clearSingleMessage(e)}}]),e}();return e.\u0275fac=function(n){return new(n||e)(s.Lb(o.b))},e.\u0275cmp=s.Fb({type:e,selectors:[["app-message"]],inputs:{position:"position"},decls:1,vars:1,consts:[[3,"class",4,"ngIf"],[3,"class",4,"ngFor","ngForOf"],[1,"message-header"],[1,"mr-auto"],[4,"ngIf"],["type","button",1,"ml-2","mb-1","close",3,"click"],["aria-hidden","true"],[1,"message-body"]],template:function(e,n){1&e&&s.xc(0,b,2,4,"div",0),2&e&&s.hc("ngIf",n.messages.length>0)},directives:[g.l,g.k],styles:[".message-group[_ngcontent-%COMP%]{max-width:350px;position:fixed;z-index:100000000000000}.message-group[_ngcontent-%COMP%]   .message[_ngcontent-%COMP%]{width:100%;overflow:hidden;box-shadow:0 .25rem .75rem rgba(0,0,0,.1);border-radius:.25rem;transition:opacity .15s linear;display:block;opacity:1;padding:.7rem;border:1px solid rgba(0,0,0,.1);border-left:10px solid #ccc;background-color:#fff}.message-group[_ngcontent-%COMP%]   .message[_ngcontent-%COMP%]:not(:last-child){margin-bottom:.75rem}.message-group[_ngcontent-%COMP%]   .message[_ngcontent-%COMP%]   .message-header[_ngcontent-%COMP%]{margin-bottom:.5rem}.message-group[_ngcontent-%COMP%]   .message[_ngcontent-%COMP%]   .message-header[_ngcontent-%COMP%]   strong[_ngcontent-%COMP%]{font-size:16px;font-weight:700}.message-group[_ngcontent-%COMP%]   .message[_ngcontent-%COMP%]   .message-body[_ngcontent-%COMP%]{line-height:1.6;font-size:14px}.message-group[_ngcontent-%COMP%]   .message.message-error[_ngcontent-%COMP%]{border-left-color:#ff5722}.message-group[_ngcontent-%COMP%]   .message.message-error[_ngcontent-%COMP%]   .message-header[_ngcontent-%COMP%]{color:#ff5722}.message-group[_ngcontent-%COMP%]   .message.message-success[_ngcontent-%COMP%]{border-left-color:#4caf50}.message-group[_ngcontent-%COMP%]   .message.message-success[_ngcontent-%COMP%]   .message-header[_ngcontent-%COMP%]{color:#4caf50}.message-group[_ngcontent-%COMP%]   .message.message-info[_ngcontent-%COMP%]{border-left-color:#4184f3}.message-group[_ngcontent-%COMP%]   .message.message-info[_ngcontent-%COMP%]   .message-header[_ngcontent-%COMP%]{color:#4184f3}.message-group[_ngcontent-%COMP%]   .message.message-warning[_ngcontent-%COMP%]{border-left-color:#ffbf00}.message-group[_ngcontent-%COMP%]   .message.message-warning[_ngcontent-%COMP%]   .message-header[_ngcontent-%COMP%]{color:#ffbf00}.message-group.message-bottom-right[_ngcontent-%COMP%]{bottom:1rem;right:1rem}.message-group.message-bottom-center[_ngcontent-%COMP%]{bottom:1rem;left:50%}.message-group.message-bottom-left[_ngcontent-%COMP%]{left:1rem;bottom:1rem}.message-group.message-top-right[_ngcontent-%COMP%]{top:5rem;right:1rem}.message-group.message-top-center[_ngcontent-%COMP%]{top:5rem;left:50%}.message-group.message-top-left[_ngcontent-%COMP%]{top:5rem;left:1rem}"]}),e}()}}]);