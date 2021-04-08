" In order for neovim to use installed plugins shared with vim
set runtimepath+=/usr/share/vim/site

augroup Fedora
  autocmd!
  " RPM spec file template
  autocmd BufNewFile *.spec silent! 0read /usr/share/nvim/template.spec
augroup END

" vim: et ts=2 sw=2
