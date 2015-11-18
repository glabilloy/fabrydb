define(["module"],function(t){var e,i,n,o,r,s=["Msxml2.XMLHTTP","Microsoft.XMLHTTP","Msxml2.XMLHTTP.4.0"],a=/^\s*<\?xml(\s)+version=[\'\"](\d)*.(\d)*[\'\"](\s)*\?>/im,l=/<body[^>]*>\s*([\s\S]+)\s*<\/body>/im,c="undefined"!=typeof location&&location.href,u=c&&location.protocol&&location.protocol.replace(/\:/,""),h=c&&location.hostname,d=c&&(location.port||void 0),p={},f=t.config&&t.config()||{};return e={version:"2.0.10",strip:function(t){if(t){t=t.replace(a,"");var e=t.match(l);e&&(t=e[1])}else t="";return t},jsEscape:function(t){return t.replace(/(['\\])/g,"\\$1").replace(/[\f]/g,"\\f").replace(/[\b]/g,"\\b").replace(/[\n]/g,"\\n").replace(/[\t]/g,"\\t").replace(/[\r]/g,"\\r").replace(/[\u2028]/g,"\\u2028").replace(/[\u2029]/g,"\\u2029")},createXhr:f.createXhr||function(){var t,e,i;if("undefined"!=typeof XMLHttpRequest)return new XMLHttpRequest;if("undefined"!=typeof ActiveXObject)for(e=0;3>e;e+=1){i=s[e];try{t=new ActiveXObject(i)}catch(n){}if(t){s=[i];break}}return t},parseName:function(t){var e,i,n,o=!1,r=t.indexOf("."),s=0===t.indexOf("./")||0===t.indexOf("../");return-1!==r&&(!s||r>1)?(e=t.substring(0,r),i=t.substring(r+1,t.length)):e=t,n=i||e,r=n.indexOf("!"),-1!==r&&(o="strip"===n.substring(r+1),n=n.substring(0,r),i?i=n:e=n),{moduleName:e,ext:i,strip:o}},xdRegExp:/^((\w+)\:)?\/\/([^\/\\]+)/,useXhr:function(t,i,n,o){var r,s,a,l=e.xdRegExp.exec(t);return l?(r=l[2],s=l[3],s=s.split(":"),a=s[1],s=s[0],!(r&&r!==i||s&&s.toLowerCase()!==n.toLowerCase()||(a||s)&&a!==o)):!0},finishLoad:function(t,i,n,o){n=i?e.strip(n):n,f.isBuild&&(p[t]=n),o(n)},load:function(t,i,n,o){if(o.isBuild&&!o.inlineText)return n(),void 0;f.isBuild=o.isBuild;var r=e.parseName(t),s=r.moduleName+(r.ext?"."+r.ext:""),a=i.toUrl(s),l=f.useXhr||e.useXhr;return 0===a.indexOf("empty:")?(n(),void 0):(!c||l(a,u,h,d)?e.get(a,function(i){e.finishLoad(t,r.strip,i,n)},function(t){n.error&&n.error(t)}):i([s],function(t){e.finishLoad(r.moduleName+"."+r.ext,r.strip,t,n)}),void 0)},write:function(t,i,n){if(p.hasOwnProperty(i)){var o=e.jsEscape(p[i]);n.asModule(t+"!"+i,"define(function () { return '"+o+"';});\n")}},writeFile:function(t,i,n,o,r){var s=e.parseName(i),a=s.ext?"."+s.ext:"",l=s.moduleName+a,c=n.toUrl(s.moduleName+a)+".js";e.load(l,n,function(){var i=function(t){return o(c,t)};i.asModule=function(t,e){return o.asModule(t,c,e)},e.write(t,l,i,r)},r)}},"node"===f.env||!f.env&&"undefined"!=typeof process&&process.versions&&process.versions.node&&!process.versions["node-webkit"]?(i=require.nodeRequire("fs"),e.get=function(t,e,n){try{var o=i.readFileSync(t,"utf8");0===o.indexOf("﻿")&&(o=o.substring(1)),e(o)}catch(r){n(r)}}):"xhr"===f.env||!f.env&&e.createXhr()?e.get=function(t,i,n,o){var r,s=e.createXhr();if(s.open("GET",t,!0),o)for(r in o)o.hasOwnProperty(r)&&s.setRequestHeader(r.toLowerCase(),o[r]);f.onXhr&&f.onXhr(s,t),s.onreadystatechange=function(){var e,o;4===s.readyState&&(e=s.status,e>399&&600>e?(o=new Error(t+" HTTP status: "+e),o.xhr=s,n(o)):i(s.responseText),f.onXhrComplete&&f.onXhrComplete(s,t))},s.send(null)}:"rhino"===f.env||!f.env&&"undefined"!=typeof Packages&&"undefined"!=typeof java?e.get=function(t,e){var i,n,o="utf-8",r=new java.io.File(t),s=java.lang.System.getProperty("line.separator"),a=new java.io.BufferedReader(new java.io.InputStreamReader(new java.io.FileInputStream(r),o)),l="";try{for(i=new java.lang.StringBuffer,n=a.readLine(),n&&n.length()&&65279===n.charAt(0)&&(n=n.substring(1)),null!==n&&i.append(n);null!==(n=a.readLine());)i.append(s),i.append(n);l=String(i.toString())}finally{a.close()}e(l)}:("xpconnect"===f.env||!f.env&&"undefined"!=typeof Components&&Components.classes&&Components.interfaces)&&(n=Components.classes,o=Components.interfaces,Components.utils["import"]("resource://gre/modules/FileUtils.jsm"),r="@mozilla.org/windows-registry-key;1"in n,e.get=function(t,e){var i,s,a,l={};r&&(t=t.replace(/\//g,"\\")),a=new FileUtils.File(t);try{i=n["@mozilla.org/network/file-input-stream;1"].createInstance(o.nsIFileInputStream),i.init(a,1,0,!1),s=n["@mozilla.org/intl/converter-input-stream;1"].createInstance(o.nsIConverterInputStream),s.init(i,"utf-8",i.available(),o.nsIConverterInputStream.DEFAULT_REPLACEMENT_CHARACTER),s.readString(i.available(),l),s.close(),i.close(),e(l.value)}catch(c){throw new Error((a&&a.path||"")+": "+c)}}),e});
//@ sourceMappingURL=text.js.map