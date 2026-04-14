#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Define root directory
root_dir = Path(__file__).parent

# CSS responsive styles to add
responsive_css = """        /* Responsivo */
        .sidebar {
            transition: transform 0.3s ease-in-out;
        }
        
        .sidebar.hidden-mobile {
            transform: translateX(-100%);
        }
        
        @media (min-width: 768px) {
            .sidebar.hidden-mobile {
                transform: translateX(0);
            }
            .hamburger-toggle {
                display: none !important;
            }
        }
        
        @media (max-width: 767px) {
            aside {
                position: fixed;
                left: 0;
                top: 0;
                width: 100%;
                max-width: 16rem;
                z-index: 40;
                transform: translateX(-100%);
            }
            
            aside.open {
                transform: translateX(0);
            }
            
            main {
                margin-left: 0 !important;
            }
            
            .sidebar-overlay {
                display: block;
            }
        }
        
        .sidebar-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 30;
        }
        
        .sidebar-overlay.show {
            display: block;
        }
"""

# JavaScript code for mobile menu
js_code = """
    // Mobile menu toggle
    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const sidebar = document.querySelector('aside');
    const sidebarOverlay = document.getElementById('sidebarOverlay');

    if (hamburgerBtn && sidebar && sidebarOverlay) {
        function toggleSidebar() {
            sidebar.classList.toggle('open');
            sidebarOverlay.classList.toggle('show');
        }

        function closeSidebar() {
            sidebar.classList.remove('open');
            sidebarOverlay.classList.remove('show');
        }

        hamburgerBtn.addEventListener('click', toggleSidebar);
        sidebarOverlay.addEventListener('click', closeSidebar);

        // Fechar sidebar quando clicar em um link
        document.querySelectorAll('aside a').forEach(link => {
            link.addEventListener('click', closeSidebar);
        });

        // Fechar sidebar com ESC
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeSidebar();
            }
        });

        // Prevenir que o sidebar feche quando clicar dentro dele
        sidebar.addEventListener('click', (e) => {
            if (e.target === sidebar) {
                closeSidebar();
            }
        });
    }
"""

def update_html_file(file_path):
    """Update a single HTML file to be responsive"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already updated
    if 'sidebar-overlay' in content:
        print(f"✓ Already responsive: {file_path}")
        return
    
    # 1. Add overlay div before aside
    if '<aside' in content:
        content = content.replace(
            '<aside',
            '<div class="sidebar-overlay" id="sidebarOverlay"></div>\n<aside class="sidebar"',
            1
        )
    
    # 2. Update main tag for responsive margin
    content = re.sub(
        r'<main class="ml-64',
        '<main class="ml-0 md:ml-64 md:pt-0 pt-16"',
        content
    )
    
    # 3. Add hamburger button inside main (after opening tag)
    hamburger_button = '''<button class="hamburger-toggle fixed top-4 left-4 md:hidden z-40 bg-deep-blue text-white p-2 rounded-lg" id="hamburgerBtn">
        <span class="material-symbols-outlined">menu</span>
    </button>'''
    
    if '<main' in content and hamburger_button not in content:
        # Find first content inside main and insert before it
        main_content = re.search(r'(<main[^>]*>)(\s*)([^<])', content)
        if main_content:
            insert_pos = main_content.end(2)
            # Find the actual content start
            content = content[:insert_pos] + hamburger_button + '\n' + content[insert_pos:]
    
    # 4. Add responsive CSS to style tag
    if responsive_css.replace('        ', '') not in content and '<style>' in content:
        content = content.replace(
            '    </style>',
            responsive_css + '    </style>',
            1
        )
    
    # 5. Add JavaScript before closing body tag
    if js_code.replace('    ', '') not in content and '</body>' in content:
        content = content.replace(
            '</body>',
            f'<script>\n{js_code}\n</script>\n</body>',
            1
        )
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated: {file_path}")

# Find and update all code.html files
code_html_files = list(root_dir.glob('**/code.html'))

print(f"Found {len(code_html_files)} HTML files to update...")
for html_file in sorted(code_html_files):
    try:
        update_html_file(html_file)
    except Exception as e:
        print(f"✗ Error updating {html_file}: {e}")

print("\n✓ All files updated successfully!")
