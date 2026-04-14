# Script para atualizar links de navegação em todos os arquivos HTML

$files = @(
    "controle_de_estoque_financeiro_com_coluna_editor/code.html",
    "movimenta_es_vers_o_final_limpa/code.html",
    "resumo_geral_cadastro_de_equipe_nos_boxes/code.html",
    "relat_rio_de_obra_menu_lateral_refinado_final_v2/code.html",
    "registro_de_equipe_cor_de_indicador_ajustada/code.html",
    "listagem_de_colaboradores_rolagem_ajustada_v2/code.html",
    "portal_de_login_engecon_vers_o_final_limpa/code.html"
)

# Mapeamento de links para cada página
$linkMappings = @(
    @{ text = "Resumo Geral"; href = "../resumo_geral_cadastro_de_equipe_nos_boxes/code.html"; icon = "dashboard|grid_view" },
    @{ text = "Movimentações"; href = "../movimenta_es_vers_o_final_limpa/code.html"; icon = "swap_horiz|sync_alt" },
    @{ text = "Estoque"; href = "../controle_de_estoque_financeiro_com_coluna_editor/code.html"; icon = "inventory_2" },
    @{ text = "Obras"; href = "../relat_rio_de_obra_menu_lateral_refinado_final_v2/code.html"; icon = "domain|apartment" },
    @{ text = "Usuários"; href = "../registro_de_equipe_cor_de_indicador_ajustada/code.html"; icon = "group" },
    @{ text = "Compras"; href = "../listagem_de_colaboradores_rolagem_ajustada_v2/code.html"; icon = "shopping_cart" },
    @{ text = "Relatórios"; href = "#"; icon = "assessment|bar_chart" },
    @{ text = "Configurações"; href = "../configura_es_sincroniza_o_visual_absoluta/code.html"; icon = "settings" }
)

Write-Host "Atualizando links em todos os arquivos HTML..."

foreach ($file in $files) {
    $filePath = Join-Path (Get-Location) $file
    
    if (Test-Path $filePath) {
        Write-Host "Processando: $file"
        $content = Get-Content -Path $filePath -Raw -Encoding UTF8
        
        # Substituir href="#" por href="novo_link" para os links de navegação
        # Fazer replace para cada link
        $content = $content -replace 'href="#">\s*<span class="material-symbols-outlined mr-4', 'href="../resumo_geral_cadastro_de_equipe_nos_boxes/code.html">#>' -replace '"><span class="material-symbols-outlined mr-4 text-2xl">dashboard', '"><span class="material-symbols-outlined mr-4 text-2xl">dashboard'
        
        Set-Content -Path $filePath -Value $content -Encoding UTF8
        Write-Host "  ✓ Atualizado"
    } else {
        Write-Host "  ✗ Arquivo não encontrado: $file"
    }
}

Write-Host "`nConcluído!"
