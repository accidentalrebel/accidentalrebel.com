// Mobile menu toggle
function toggleMenu() {
    const navLinks = document.getElementById('navLinks');
    navLinks.classList.toggle('active');
}

// Reading progress indicator
window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    document.getElementById('progress').style.width = scrolled + '%';
});

// Simple syntax highlighting - DISABLED for now since Pygments handles it
// document.addEventListener('DOMContentLoaded', function() {
//     // Apply syntax highlighting to code blocks
//     const codeBlocks = document.querySelectorAll('pre code');
//     codeBlocks.forEach(block => {
//         const language = detectLanguage(block);
//         if (language) {
//             highlightCode(block, language);
//         }
//     });
// });

function detectLanguage(block) {
    // Check for class names
    const classList = block.className;
    if (classList.includes('python') || classList.includes('language-python')) return 'python';
    if (classList.includes('javascript') || classList.includes('language-javascript')) return 'javascript';
    if (classList.includes('bash') || classList.includes('language-bash')) return 'bash';
    if (classList.includes('c') || classList.includes('language-c')) return 'c';
    if (classList.includes('asm') || classList.includes('language-asm') || classList.includes('assembly')) return 'asm';
    
    // Try to detect based on content
    const code = block.textContent;
    if (/\b(def|import|from|print)\b/.test(code)) return 'python';
    if (/\b(function|const|let|var)\b/.test(code)) return 'javascript';
    if (/\b(#include|int main|printf)\b/.test(code)) return 'c';
    if (/\b(mov|push|pop|call|ret|jmp|je|jne|lea|sub|add|xor)\b/i.test(code)) return 'asm';
    if (/^\s*[\$#]/.test(code)) return 'bash';
    
    return null;
}

function highlightCode(block, language) {
    let code = block.innerHTML;
    
    switch (language) {
        case 'python':
            code = highlightPython(code);
            break;
        case 'javascript':
            code = highlightJavaScript(code);
            break;
        case 'bash':
            code = highlightBash(code);
            break;
        case 'c':
            code = highlightC(code);
            break;
        case 'asm':
            code = highlightAsm(code);
            break;
    }
    
    block.innerHTML = code;
}

function highlightPython(code) {
    // Keywords
    code = code.replace(/\b(def|class|import|from|return|if|elif|else|for|while|try|except|finally|with|as|pass|break|continue|and|or|not|in|is|None|True|False|lambda|global|nonlocal|yield|async|await)\b/g, 
        '<span class="hljs-keyword">$1</span>');
    
    // Strings
    code = code.replace(/(["'])((?:\\.|(?!\1)[^\\])*?)\1/g, 
        '<span class="hljs-string">$1$2$1</span>');
    
    // Comments
    code = code.replace(/(#.*$)/gm, 
        '<span class="hljs-comment">$1</span>');
    
    // Function definitions
    code = code.replace(/def\s+(<span class="hljs-keyword">def<\/span>\s+)?(\w+)/g, 
        'def <span class="hljs-title">$2</span>');
    
    // Numbers
    code = code.replace(/\b(\d+(?:\.\d+)?)\b/g, 
        '<span class="hljs-number">$1</span>');
    
    return code;
}

function highlightJavaScript(code) {
    // Keywords
    code = code.replace(/\b(function|const|let|var|if|else|for|while|do|break|continue|return|try|catch|finally|throw|new|this|typeof|instanceof|true|false|null|undefined)\b/g, 
        '<span class="hljs-keyword">$1</span>');
    
    // Strings
    code = code.replace(/(["'])((?:\\.|(?!\1)[^\\])*?)\1/g, 
        '<span class="hljs-string">$1$2$1</span>');
    
    // Comments
    code = code.replace(/(\/\/.*$)/gm, 
        '<span class="hljs-comment">$1</span>');
    
    // Numbers
    code = code.replace(/\b(\d+(?:\.\d+)?)\b/g, 
        '<span class="hljs-number">$1</span>');
    
    return code;
}

function highlightBash(code) {
    // Commands and keywords
    code = code.replace(/\b(sudo|cd|ls|mkdir|rm|cp|mv|grep|find|awk|sed|cat|echo|export|alias|chmod|chown)\b/g, 
        '<span class="hljs-keyword">$1</span>');
    
    // Strings
    code = code.replace(/(["'])((?:\\.|(?!\1)[^\\])*?)\1/g, 
        '<span class="hljs-string">$1$2$1</span>');
    
    // Comments
    code = code.replace(/(#.*$)/gm, 
        '<span class="hljs-comment">$1</span>');
    
    // Variables
    code = code.replace(/(\$\w+)/g, 
        '<span class="hljs-variable">$1</span>');
    
    return code;
}

function highlightC(code) {
    // Keywords
    code = code.replace(/\b(int|char|float|double|void|if|else|for|while|do|break|continue|return|struct|typedef|static|extern|const|volatile|sizeof|enum|union|switch|case|default)\b/g, 
        '<span class="hljs-keyword">$1</span>');
    
    // Strings
    code = code.replace(/(["'])((?:\\.|(?!\1)[^\\])*?)\1/g, 
        '<span class="hljs-string">$1$2$1</span>');
    
    // Comments
    code = code.replace(/(\/\/.*$)/gm, 
        '<span class="hljs-comment">$1</span>');
    
    // Include statements
    code = code.replace(/(#include\s*<[^>]+>)/g, 
        '<span class="hljs-meta">$1</span>');
    
    // Numbers
    code = code.replace(/\b(\d+(?:\.\d+)?)\b/g, 
        '<span class="hljs-number">$1</span>');
    
    return code;
}