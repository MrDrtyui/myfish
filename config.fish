if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -g fish_greeting ""
set -Ux EDITOR nvim
set -Ux VISUAL nvim

starship init fish | source
