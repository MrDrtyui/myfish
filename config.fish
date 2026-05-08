if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -g fish_greeting ""
set -U fish_autosuggestion_enabled 1
set -Ux EDITOR nvim
set -Ux VISUAL nvim

function ai
    python3 ~/.config/fish/scrits/ai.py $argv
end

function ai-clear
    rm ~/.config/fish/scrits/.ai_history.json
end

funcsave ai-clear
starship init fish | source
