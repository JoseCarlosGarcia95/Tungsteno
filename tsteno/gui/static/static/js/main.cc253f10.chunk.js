(this.webpackJsonpapp=this.webpackJsonpapp||[]).push([[0],{161:function(e,t,n){},164:function(e,t,n){},165:function(e,t,n){"use strict";n.r(t);var a=n(0),s=n(2),c=n.n(s),r=n(54),o=n.n(r),i=n(5),l=n(12),u=n(13),d=n(8),h=n(7),b=n(35),j=n.n(b),m=n(25),k=n(26);window.eel||(window.eel={expose:function(e){},suggestions:function(e){return function(){return Promise.resolve([{name:"autocomplete_1",value:"autocomplete_2",score:1,meta:"development autocomplete"}])}},searchFunction:function(e){return function(){return Promise.resolve([{functionName:"Integrate",description:"*world*!"}])}},evaluate:function(e){return function(){if("plot"==e)return Promise.resolve({processor:"plot",plot_data:[{x:[1,2,3],y:[2,6,3],z:[2,6,3],type:"scatter3d",mode:"lines",marker:{color:"red"}}]});if("plot3d"==e){return Promise.resolve({processor:"plot",plot_data:[{z:[[8.83,8.89,8.81,8.87,8.9,8.87],[8.89,8.94,8.85,8.94,8.96,8.92],[8.84,8.9,8.82,8.92,8.93,8.91],[8.79,8.85,8.79,8.9,8.94,8.92],[8.79,8.88,8.81,8.9,8.95,8.92],[8.8,8.82,8.78,8.91,8.94,8.92],[8.75,8.78,8.77,8.91,8.95,8.92],[8.8,8.8,8.77,8.91,8.95,8.94],[8.74,8.81,8.76,8.93,8.98,8.99],[8.89,8.99,8.92,9.1,9.13,9.11],[8.97,8.97,8.91,9.09,9.11,9.11],[9.04,9.08,9.05,9.25,9.28,9.27],[9,9.01,9,9.2,9.23,9.2],[8.99,8.99,8.98,9.18,9.2,9.19],[8.93,8.97,8.97,9.18,9.2,9.18]],type:"surface"}]})}return Promise.resolve({processor:"default",result:"Hello world!"})}}});var p=window.eel,v=function(e){Object(d.a)(n,e);var t=Object(h.a)(n);function n(e){var a;return Object(i.a)(this,n),(a=t.call(this,e)).state={searchValue:"",searchResults:[]},a.bindSearchFunctions=a.searchFunctions.bind(Object(u.a)(a)),a}return Object(l.a)(n,[{key:"searchFunctions",value:function(e){var t=this;this.setState({searchValue:e.target.value}),p.searchFunction(e.target.value)().then((function(e){return t.setState({searchResults:e})}))}},{key:"render",value:function(){return Object(a.jsxs)("div",{"uk-sticky":"sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky",children:[Object(a.jsxs)("nav",{className:"uk-navbar uk-navbar-container uk-margin",children:[Object(a.jsx)("div",{className:"uk-navbar-center",children:Object(a.jsxs)("a",{className:"uk-navbar-item uk-logo",children:[Object(a.jsx)(m.a,{className:"uk-margin-small-right",icon:k.a})," ","Tungsteno v1.2 (Alpha)"]})}),Object(a.jsx)("div",{className:"uk-navbar-right",children:Object(a.jsxs)("div",{children:[Object(a.jsx)("a",{className:"uk-navbar-toggle","uk-search-icon":"true",href:"#"}),Object(a.jsx)("div",{"uk-drop":"mode: click; pos: left-center; offset: 0",children:Object(a.jsxs)("form",{className:"uk-search uk-search-navbar uk-width-1-1",children:[Object(a.jsx)("input",{className:"uk-search-input",type:"search",placeholder:"Search...",onChange:this.bindSearchFunctions,value:this.state.searchValue,autoFocus:!0}),Object(a.jsx)("div",{"uk-drop":"mode: click; offset: 20",style:{visibility:0!=this.state.searchResults.length?"visible":"hidden"},children:this.state.searchResults.map((function(e,t){var n="";return e.description.split("\n").length>0&&(n=e.description.split("\n")[1]),Object(a.jsxs)("div",{className:"uk-card uk-card-default",children:[Object(a.jsxs)("div",{className:"uk-card-body",children:[Object(a.jsx)("div",{className:"uk-card-badge uk-label",children:"Builtin"}),Object(a.jsx)("h3",{className:"uk-card-title uk-margin-remove-bottom",children:e.functionName}),Object(a.jsx)("p",{children:Object(a.jsx)(j.a,{children:n})})]}),Object(a.jsx)("div",{className:"uk-card-footer",children:Object(a.jsx)("a",{href:"#","data-uk-toggle":"target: #"+e.functionName,className:"uk-button uk-button-text",children:"Read more"})}),Object(a.jsx)("div",{id:e.functionName,"data-uk-modal":!0,children:Object(a.jsxs)("div",{className:"uk-modal-dialog uk-modal-body",children:[Object(a.jsx)("button",{className:"uk-modal-close-default",type:"button","data-uk-close":!0}),Object(a.jsx)("h2",{className:"uk-modal-title",children:e.functionName}),Object(a.jsx)(j.a,{children:e.description})]})})]})}))})]})})]})})]}),this.state.searchResults.map((function(e,t){return""}))]})}}]),n}(c.a.Component);var f=function(){return Object(a.jsx)("div",{id:"nav-primary","uk-offcanvas":"overlay: true",children:Object(a.jsx)("div",{className:"uk-offcanvas-bar uk-flex uk-flex-column",children:Object(a.jsx)("ul",{className:"uk-nav uk-nav-primary uk-nav-center uk-margin-auto-vertical"})})})};var x=function(){return Object(a.jsxs)("header",{children:[Object(a.jsx)(v,{}),Object(a.jsx)(f,{})]})},O=n(36),g=n.n(O),N=n(55),w=function e(t){Object(i.a)(this,e),this.Id=t},y=function(){function e(t){Object(i.a)(this,e),this.cells=[],this.NotebookComponent=t,window.eel.expose(function(e){this.createNewCell(e)}.bind(this),"createNewCell"),this.loadModernUI()}return Object(l.a)(e,[{key:"loadModernUI",value:function(){var e=Object(N.a)(g.a.mark((function e(){return g.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,p.load_modern_ui()();case 2:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}()},{key:"createNewCell",value:function(e){console.log(e),console.debug("Creating a new cell"),this.cells.push(new w(this.cells.length+1)),this.NotebookComponent&&this.NotebookComponent.setState({cells:this.cells})}}]),e}(),C=n(56),S=n.n(C),_=(n(155),n(156),n(57)),F=n(58),I=n.n(F),E=(n(160),function(e){Object(d.a)(n,e);var t=Object(h.a)(n);function n(){var e;return Object(i.a)(this,n),(e=t.call(this)).$rules={start:[{token:"comment",regex:"\\(\\*",next:"comment"},{token:"string",regex:'["](?:(?:\\\\.)|(?:[^"\\\\]))*?["]'},{token:"string",regex:"['](?:(?:\\\\.)|(?:[^'\\\\]))*?[']"},{token:"constant.numeric",regex:/0(?:[xX][0-9a-fA-F][0-9a-fA-F_]*|[bB][01][01_]*)[LlSsDdFfYy]?\b/},{token:"constant.numeric",regex:/[+-]?\d[\d_]*(?:(?:\.[\d_]*)?(?:[eE][+-]?[\d_]+)?)?[LlSsDdFfYy]?\b/},{token:"constant.language.boolean",regex:"(?:true|false)\\b"},{token:"keyword.operator",regex:"!|\\$|%|&|\\*|\\-\\-|\\-|\\+\\+|\\+|~|===|==|=|!=|!==|<=|>=|<<=|>>=|>>>=|<>|<|>|!|&&|\\|\\||\\?\\:|\\*=|%=|\\+=|\\-=|&=|\\^=|\\b(?:in|instanceof|new|delete|typeof|void)"},{token:"lparen",regex:/[[(\[]/},{token:"rparen",regex:/[[(\]]/},{token:"text",regex:"\\s+"}],comment:[{token:"comment",regex:".*?\\*\\)",next:"start"},{token:"comment",regex:".+"}]},e}return n}(window.ace.acequire("ace/mode/text_highlight_rules").TextHighlightRules)),R=function(e){Object(d.a)(n,e);var t=Object(h.a)(n);function n(){var e;return Object(i.a)(this,n),(e=t.call(this)).HighlightRules=E,e}return n}(window.ace.acequire("ace/mode/python").Mode),M=(n(161),function(e){Object(d.a)(n,e);var t=Object(h.a)(n);function n(e){var a;return Object(i.a)(this,n),(a=t.call(this,e)).state={output:{}},a.handleEvaluateCell=a.evaluateCell.bind(Object(u.a)(a)),a}return Object(l.a)(n,[{key:"componentDidMount",value:function(){this.refs.codeEditor.editor.getSession().setMode(new R),Object(_.addCompleter)({getCompletions:function(e,t,n,a,s){p.suggestions(a)().then((function(e){s(null,e)}))}})}},{key:"evaluateCell",value:function(){var e=this;this.props.Cell.Id,this.props.Notebook.cells.length,p.evaluate(this.refs.codeEditor.editor.getValue())().then((function(t){e.setState({output:t})}))}},{key:"render",value:function(){var e;if(this.state.output)switch(this.state.output.processor){case"default":e=this.state.output.result;break;case"plot":console.log(this.state.output),e=Object(a.jsx)("center",{children:Object(a.jsx)(I.a,{data:this.state.output.plot_data,layout:{autosize:!0}})})}return Object(a.jsxs)("div",{className:"uk-card uk-card-default uk-width-1-1 uk-margin uk-box-shadow-hover-medium uk-box-shadow-small",children:[Object(a.jsxs)("div",{className:"uk-card-header",children:[Object(a.jsx)("a",{href:"#",onClick:this.handleEvaluateCell,className:"uk-icon-button uk-button-success uk-margin-small-right",children:Object(a.jsx)(m.a,{icon:k.b})}),Object(a.jsxs)("div",{className:"uk-card-badge uk-label",children:["#",this.props.Cell.Id]})]}),Object(a.jsx)("div",{className:"uk-card-body",children:Object(a.jsx)("div",{className:"uk-editor",children:Object(a.jsx)(S.a,{ref:"codeEditor",mode:"javascript",theme:"github",name:"{this.props.Cell.Id}",width:"100%",height:"auto",setOptions:{enableBasicAutocompletion:!0,enableLiveAutocompletion:!0,enableSnippets:!0,showGutter:!1,minLines:1,maxLines:50,fontSize:16},commands:[{name:"evaluate",bindKey:{win:"Shift-enter",mac:"Shift-enter"},exec:this.handleEvaluateCell}]})})}),Object(a.jsx)("div",{className:"uk-card-footer",children:e})]})}}]),n}(c.a.Component)),L=function(e){Object(d.a)(n,e);var t=Object(h.a)(n);function n(e){var a;return Object(i.a)(this,n),(a=t.call(this,e)).state={},a.Notebook=new y(Object(u.a)(a)),a.state.cells=a.Notebook.cells,a}return Object(l.a)(n,[{key:"componentDidMount",value:function(){}},{key:"render",value:function(){var e=this;return Object(a.jsxs)("div",{className:"uk-container",children:[this.state.cells.map((function(t,n){return Object(a.jsx)(M,{Notebook:e.Notebook,Cell:t},t.Id)})),Object(a.jsx)("a",{href:"#","uk-totop":"true"})]})}}]),n}(c.a.Component),P=[],A={};var V=function(){return Object(a.jsxs)(a.Fragment,{children:[Object(a.jsx)(x,{}),Object(a.jsx)(L,{Cells:P,Properties:A})]})},z=n(63),B=(n(162),n(163),n(164),n(59)),D=n(167);z.a.use(D.a).init({resources:{en:{common:B}},lng:"en",fallbackLng:"en",interpolation:{escapeValue:!1}}),o.a.render(Object(a.jsx)(c.a.StrictMode,{children:Object(a.jsx)(V,{})}),document.getElementById("root"))},59:function(e){e.exports=JSON.parse("{}")}},[[165,1,2]]]);
//# sourceMappingURL=main.cc253f10.chunk.js.map