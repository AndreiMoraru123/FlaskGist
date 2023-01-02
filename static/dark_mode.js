// import hljs from 'highlight.js/lib/highlight';
//
// function highlightSyntax() {
//   // Get all pre elements on the page
//   const preElements = document.querySelectorAll('pre');
//
//   // Iterate over each pre element
//   preElements.forEach((pre) => {
//     // Get the text content of the pre element
//     const code = pre.textContent;
//
//     // Get the file extension from the parent element's data attribute
//     const fileExt = pre.parentElement.dataset.ext;
//
//     // Choose a syntax highlighting library based on the file extension
//     let highlight;
//     switch (fileExt) {
//       case 'js':
//         highlight = hljs.highlightJS;
//         break;
//       case 'py':
//         highlight = hljs.highlightPython;
//         break;
//       case 'html':
//         highlight = hljs.highlightHTML;
//         break;
//       case 'css':
//         highlight = hljs.highlightCSS;
//         break;
//       case 'java':
//         highlight = hljs.highlightJava;
//         break;
//       case 'c':
//         highlight = hljs.highlightC;
//         break;
//       case 'cs':
//         highlight = hljs.highlightCSharp;
//         break;
//       case 'cpp':
//         highlight = hljs.highlightCPP;
//         break;
//       case 'rb':
//         highlight = hljs.highlightRuby;
//         break;
//       case 'go':
//         highlight = hljs.highlightGo;
//         break;
//       case 'swift':
//         highlight = hljs.highlightSwift;
//         break;
//       case 'sh':
//         highlight = hljs.highlightShell;
//         break;
//       case 'rs':
//         highlight = hljs.highlightRust;
//         break;
//       case 'hs':
//         highlight = hljs.highlightHaskell;
//         break;
//       case 'lua':
//         highlight = hljs.highlightLua;
//         break;
//       case 'erl':
//         highlight = hljs.highlightErlang;
//         break;
//       case 'ex':
//         highlight = hljs.highlightElixir;
//         break;
//       case 'ps1':
//         highlight = hljs.highlightPowerShell;
//         break;
//       default:
//         highlight = hljs.highlightAuto;
//         break;
//     }
//
//     // Use the chosen syntax highlighting library to highlight the code
//     const highlightedCode = highlight(code);
//
//     // Replace the text content of the pre element with the highlighted code
//     pre.innerHTML = highlightedCode;
//   });
// }
//
// // Call the highlightSyntax function when the page is loaded
// document.addEventListener('DOMContentLoaded', highlightSyntax);
