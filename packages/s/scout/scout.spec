#
# spec file for package scout
#
# Copyright (c) 2021 SUSE LLC
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


%define cnfrepo zypp
Name:           scout
Version:        0.2.7+20230124.b4e3468
Release:        0
Summary:        Indexing Package Properties
License:        MIT
Group:          System/Packages
URL:            https://github.com/openSUSE/scout/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gettext
BuildRequires:  python3
BuildRequires:  python3-rpm
BuildRequires:  python3-solv
BuildRequires:  python3-xml
Requires:       python3
Requires:       python3-solv >= 0.6.0
Requires:       python3-xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The scout tool helps with indexing of various package properties.

%package command-not-found
Summary:        Command Not Found extension for shell
Group:          System/Packages
Requires:       python3
Requires:       python3-rpm
Requires:       scout = %{version}-%{release}
Obsoletes:      command-not-found < %{version}-%{release}
Provides:       command-not-found
Conflicts:      command-not-found

%description command-not-found
The "command not found" message is not very helpful. If e.g. the unzip
command is not found but it's available in a package, it would be very
interesting if the system could tell that the command is currently not
available, but installing a package would provide it.

%prep
%setup -q

%build
# compile scripts
python3 -mcompileall .

%install
# --- scout ---
# install python scripts
mkdir -p %{buildroot}%{python3_sitelib}/%{name}/__pycache__
shopt -s extglob
cp -a scout/!(foo).py %{buildroot}%{python3_sitelib}/%{name}
cp -a scout/__pycache__/!(foo).pyc %{buildroot}%{python3_sitelib}/%{name}/__pycache__
# install data files
install -D -m 0644 repos.conf %{buildroot}%{_datadir}/%{name}/repos.conf
# install scout binary
install -D -m 0755 scout-cmd.py %{buildroot}%{_bindir}/%{name}
# install bash completion
install -D -m 0644 scout-bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/scout.sh
# install manpage
install -D -m 0644 doc/scout.1 %{buildroot}%{_mandir}/man1/scout.1
# install and find languages
for po in i18n/scout/*.po; do
    pofile=${po##*/}
    lang=${pofile%.po}
    msgfmt $po -o i18n/scout/$lang.mo
    install -D -m 0644 i18n/scout/$lang.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/scout.mo
done
%find_lang scout

# --- command-not-found ---
install -D -m 0755 handlers/bin/command-not-found %{buildroot}%{_bindir}/command-not-found
ln -sf command-not-found %{buildroot}%{_bindir}/cnf
# install manpage
install -D -m 0644 doc/command-not-found.1 %{buildroot}%{_mandir}/man1/command-not-found.1
ln -sf command-not-found.1.gz %{buildroot}%{_mandir}/man1/cnf.1.gz
# install shell handlers
for shell in bash zsh; do
    install -D -m 644 handlers/bin/command_not_found_${shell} %{buildroot}%{_sysconfdir}/${shell}_command_not_found
    sed -i 's:__REPO__:%{cnfrepo}:' %{buildroot}%{_sysconfdir}/${shell}_command_not_found
done
# install and find languages
for po in i18n/command-not-found/*.po; do
    pofile=${po##*/}
    lang=${pofile%.po}
    msgfmt $po -o i18n/command-not-found/$lang.mo
    install -D -m 0644 i18n/command-not-found/$lang.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/command-not-found.mo
done
%find_lang command-not-found

%files -f scout.lang
%defattr(-,root,root)
%doc AUTHORS LICENSE README TODO doc/scout.html doc/scout.pdf
%{_bindir}/%{name}*
%{python3_sitelib}/%{name}
%{_datadir}/%{name}
%config %{_sysconfdir}/bash_completion.d/*
%{_mandir}/man1/scout*

%files command-not-found -f command-not-found.lang
%defattr(-,root,root)
%doc handlers/bin/README
%{_bindir}/cnf
%{_bindir}/command-not-found
%config %{_sysconfdir}/*_command_not_found
%{_mandir}/man1/cnf*
%{_mandir}/man1/command-not-found*

%changelog
