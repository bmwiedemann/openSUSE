#
# spec file for package powerline
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define powerline_python_sitelib %{python3_sitelib}
Name:           powerline
Version:        2.8
Release:        0
Summary:        Status line and prompt utility
License:        MIT
Group:          System/Console
URL:            https://github.com/powerline/powerline
Source0:        https://github.com/powerline/powerline/archive/%{version}/powerline-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  fontconfig
BuildRequires:  python3-Sphinx
BuildRequires:  python3-base
BuildRequires:  python3-setuptools
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  tmux
BuildRequires:  vim-base
Requires:       powerline-fonts
Requires:       python3
Recommends:     python3-pygit2
%{?systemd_requires}

%description
Powerline is a status line plugin for vim, and provides status lines and prompts
for several other applications, including zsh, bash, tmux, IPython, Awesome and
Qtile.

%package fonts
Summary:        Powerline Fonts
Group:          System/Console
Requires:       fontconfig
BuildArch:      noarch

%description fonts
This package provides the powerline fonts.

%package docs
Summary:        Documentation for powerline
Group:          System/Console
BuildArch:      noarch

%description docs
This package provides the powerline documentation.

%package -n vim-plugin-powerline
Summary:        Powerline VIM plugin
Group:          System/Console
Requires:       powerline
Requires:       vim
BuildArch:      noarch

%description -n vim-plugin-powerline
Powerline is a status line plugin for vim, and provides status lines and
prompts.

%package -n tmux-powerline
Summary:        Powerline for tmux
Group:          System/Console
Requires:       powerline
Requires:       tmux
BuildArch:      noarch

%description -n tmux-powerline
Powerline for tmux.

Add

    source %{_datadir}/tmux/powerline.conf

to your ~/.tmux.conf file.

%prep
%autosetup -p1

# Change shebang in all relevant files in this directory and all subdirectories
find -type f -exec sed -i '1s=^#!%{_bindir}/\(python\|env python\)[23]\?=#!%{_bindir}/python3=' {} +

%build

%install
sed -i -e "/DEFAULT_SYSTEM_CONFIG_DIR/ s@None@'%{_sysconfdir}/xdg'@" powerline/config.py
sed -i -e "/TMUX_CONFIG_DIRECTORY/ s@BINDINGS_DIRECTORY@'%{_prefix}/share'@" powerline/config.py
CFLAGS="%{optflags}" \
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot} --optimize=1

# build docs
pushd docs
make html
rm _build/html/.buildinfo
# A structure gets initialized while building the docs with os.environ.
# This works around an rpmlint error with the build dir being in a file.
sed -i -e 's/abuild/user/g' _build/html/develop/extensions.html

make man
popd

# config
install -d -m0755 %{buildroot}/%{_sysconfdir}/xdg/%{name}
cp -r powerline/config_files/* %{buildroot}/%{_sysconfdir}/xdg/%{name}/

# fonts
install -d -m0755 %{buildroot}/%{_sysconfdir}/fonts/conf.d
install -d -m0755 %{buildroot}/%{_datadir}/fonts/truetype
install -d -m0755 %{buildroot}/%{_datadir}/fontconfig/conf.avail

install -m0644 font/PowerlineSymbols.otf %{buildroot}/%{_datadir}/fonts/truetype/PowerlineSymbols.otf
install -m0644 font/10-powerline-symbols.conf %{buildroot}/%{_datadir}/fontconfig/conf.avail/10-powerline-symbols.conf

ln -s %{_datadir}/fontconfig/conf.avail/10-powerline-symbols.conf %{buildroot}/%{_sysconfdir}/fonts/conf.d/10-powerline-symbols.conf

# manpages
install -d -m0755 %{buildroot}/%{_mandir}/man1
for f in powerline-config.1 powerline-daemon.1 powerline-lint.1 powerline.1; do
	install -m0644 "docs/_build/man/$f" "%{buildroot}/%{_mandir}/man1/$f"
done

# awesome
install -d -m0755 %{buildroot}/%{_datadir}/%{name}/awesome/
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/awesome/powerline.lua %{buildroot}/%{_datadir}/%{name}/awesome/
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/awesome/powerline-awesome.py %{buildroot}/%{_datadir}/%{name}/awesome/

# bash bindings
install -d -m0755 %{buildroot}/%{_datadir}/%{name}/bash
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/bash/powerline.sh %{buildroot}/%{_datadir}/%{name}/bash/

# fish
install -d -m0755 %{buildroot}/%{_datadir}/%{name}/fish
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/fish/powerline-setup.fish %{buildroot}/%{_datadir}/%{name}/fish

# i3
install -d -m0755 %{buildroot}/%{_datadir}/%{name}/i3
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/i3/powerline-i3.py %{buildroot}/%{_datadir}/%{name}/i3

# ipython
install -d -m0755 %{buildroot}/%{_datadir}/%{name}/ipython
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/ipython/post_0_11.py %{buildroot}/%{_datadir}/%{name}/ipython
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/ipython/pre_0_11.py %{buildroot}/%{_datadir}/%{name}/ipython

# qtile
install -d -m0755 %{buildroot}/%{_datadir}/%{name}/qtile
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/qtile/widget.py %{buildroot}/%{_datadir}/%{name}/qtile

# shell bindings
install -d -m0755 %{buildroot}/%{_datadir}/%{name}/shell
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/shell/powerline.sh %{buildroot}/%{_datadir}/%{name}/shell/

# tcsh
install -d -m0755 %{buildroot}/%{_datadir}/%{name}/tcsh
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/tcsh/powerline.tcsh %{buildroot}/%{_datadir}/%{name}/tcsh

# tmux plugin
install -d -m0755 %{buildroot}/%{_datadir}/tmux
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/tmux/powerline*.conf %{buildroot}/%{_datadir}/tmux/

# vim plugin
install -d -m0755 %{buildroot}/%{_datadir}/vim/site/plugin/
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/vim/plugin/powerline.vim %{buildroot}/%{_datadir}/vim/site/plugin/powerline.vim
rm -rf %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/vim/plugin
install -d -m0755 %{buildroot}/%{_datadir}/vim/site/autoload/powerline
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/vim/autoload/powerline/debug.vim %{buildroot}/%{_datadir}/vim/site/autoload/powerline/debug.vim
rm -rf %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/vim/autoload

# zsh
install -d -m0755 %{buildroot}/%{_datadir}/%{name}/zsh
mv %{buildroot}/%{powerline_python_sitelib}/powerline/bindings/zsh/powerline.zsh %{buildroot}/%{_datadir}/%{name}/zsh

# systemd
rm -f %{buildroot}%{powerline_python_sitelib}/powerline/dist/systemd/powerline-daemon.service
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 powerline/dist/systemd/powerline-daemon.service %{buildroot}%{_unitdir}/powerline.service
install -d -m 0755 %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcpowerline

# cleanup
rm -rf %{buildroot}/%{powerline_python_sitelib}/%{name}/config_files
find %{buildroot}/%{powerline_python_sitelib}/%{name}/bindings -name "*.py[a-z]" -delete

%fdupes %{buildroot}%{powerline_python_sitelib}

%pre
%service_add_pre powerline.service

%post
%service_add_post powerline.service

%preun
%service_del_preun powerline.service

%postun
%service_del_postun powerline.service

%files
%license LICENSE
%doc README.rst
%config %{_sysconfdir}/xdg/%{name}
%{_bindir}/powerline
%{_bindir}/powerline-config
%{_bindir}/powerline-daemon
%{_bindir}/powerline-render
%{_bindir}/powerline-lint
%{_sbindir}/rcpowerline
%{_mandir}/man1/powerline.1%{?ext_man}
%{_mandir}/man1/powerline-config.1%{?ext_man}
%{_mandir}/man1/powerline-daemon.1%{?ext_man}
%{_mandir}/man1/powerline-lint.1%{?ext_man}
%{_unitdir}/powerline.service
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/awesome
%{_datadir}/%{name}/awesome/powerline.lua
%{_datadir}/%{name}/awesome/powerline-awesome.py
%dir %{_datadir}/%{name}/bash
%{_datadir}/%{name}/bash/powerline.sh
%dir %{_datadir}/%{name}/fish
%{_datadir}/%{name}/fish/powerline-setup.fish
%dir %{_datadir}/%{name}/i3
%{_datadir}/%{name}/i3/powerline-i3.py
%dir %{_datadir}/%{name}/ipython
%{_datadir}/%{name}/ipython/post_0_11.py
%{_datadir}/%{name}/ipython/pre_0_11.py
%dir %{_datadir}/%{name}/qtile
%{_datadir}/%{name}/qtile/widget.py
%dir %{_datadir}/%{name}/shell
%{_datadir}/%{name}/shell/powerline.sh
%dir %{_datadir}/%{name}/tcsh
%{_datadir}/%{name}/tcsh/powerline.tcsh
%dir %{_datadir}/%{name}/zsh
%{_datadir}/%{name}/zsh/powerline.zsh
%{powerline_python_sitelib}/*

%files fonts
%license LICENSE
%doc README.rst
%{_sysconfdir}/fonts/conf.d/10-powerline-symbols.conf
%{_datadir}/fontconfig/conf.avail/10-powerline-symbols.conf
%dir %{_datadir}/fonts/truetype
%{_datadir}/fonts/truetype/PowerlineSymbols.otf

%files docs
%doc docs/_build/html

%files -n vim-plugin-powerline
%license LICENSE
%doc README.rst
%dir %{_datadir}/vim/site/autoload
%dir %{_datadir}/vim/site/autoload/powerline
%{_datadir}/vim/site/autoload/powerline/debug.vim
%dir %{_datadir}/vim/site/plugin
%{_datadir}/vim/site/plugin/powerline.vim

%files -n tmux-powerline
%license LICENSE
%doc README.rst
%dir %{_datadir}/tmux
%{_datadir}/tmux/powerline*.conf

%changelog
