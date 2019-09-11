#
# spec file for package golang
#
# Copyright (c) 2015-2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%global provider        github
%global provider_tld    com
%global project         nsf
%global repo            gocode
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0.0.0+git20161123.5070dac
Release:        0
Summary:        An autocompletion daemon for the Go programming language
License:        MIT
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  golang-packaging
BuildRequires:  xz

BuildRequires:  vim
BuildRequires:  emacs-nox

%{go_nostrip}
%{go_provides}

%description
Gocode is a helper tool which is intended to be integrated with your
source code editor such as vim or emacs. It uses a client-server
architecture for caching purposes (hence "daemon") and provides
context-sensitive autocompletion.

%package -n gocode
Summary:        An autocompletion daemon for the Go programming language
Group:          Development/Languages/Golang
AutoReqProv:    Off

%{go_exclusivearch}

%description -n gocode
Gocode is a helper tool which is intended to be integrated with your
source code editor such as vim or emacs. It uses a client-server
architecture for caching purposes (hence "daemon") and provides
context-sensitive autocompletion.

%package -n vim-completion-golang
Summary:        Golang autocompletion files for Vim
Group:          Productivity/Text/Editors
AutoReqProv:    Off
Requires:       gocode = %{version}
Requires:       vim
Provides:	      vim-plugin-gocode = %{version}

%description -n vim-completion-golang
Vim autocompletion for the Go programming language.

%package -n emacs-completion-golang
Summary:	      Golang autocompletion files for Emacs
Group:		      Productivity/Text/Editors
AutoReqProv:    Off
Requires:	      gocode = %{version}
Requires:	      emacs

%description -n emacs-completion-golang
Emacs autocompletion for the Go programming language.

Add the following to your emacs-config:

```lisp
(require 'go-autocomplete)	; load go autocompletion backend
```

%prep
%setup -q -n %{repo}-%{version}

%build
%goprep %{import_path}
%gobuild ...

%install
%goinstall
%gosrc
%gofilelist

# vim-completion-golang
mkdir -p %{buildroot}%{_datadir}/vim/site/autoload/
install -Dm644 %{_builddir}/gocode-%{version}/vim/autoload/gocomplete.vim \
  %{buildroot}%{_datadir}/vim/site/autoload/gocomplete.vim
install -Dm644 %{_builddir}/gocode-%{version}/vim/ftplugin/go/gocomplete.vim \
  %{buildroot}%{_datadir}/vim/site/ftplugin/go/gocomplete.vim

# emacs-completion-golang
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/
install -m 0644 %{_builddir}/gocode-%{version}/emacs/go-autocomplete.el \
  %{buildroot}%{_datadir}/emacs/site-lisp/

%check
%gotest %{import_path}...

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md LICENSE

%files -n gocode
%defattr(-,root,root)
%{_bindir}/gocode

%files -n vim-completion-golang
%defattr(-,root,root,-)
%{_datadir}/vim/site/autoload/gocomplete.vim
%dir %{_datadir}/vim/site/ftplugin
%dir %{_datadir}/vim/site/ftplugin/go
%{_datadir}/vim/site/ftplugin/go/gocomplete.vim

%files -n emacs-completion-golang
%defattr(-,root,root,-)
%{_datadir}/emacs/site-lisp/go-autocomplete.el

%changelog
