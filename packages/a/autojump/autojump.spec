#
# spec file for package autojump
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           autojump
Version:        22.5.3
Release:        0
Summary:        A faster way to navigate the filesystem from a shell
License:        GPL-3.0-or-later
Group:          System/Console
Url:            https://github.com/wting/autojump
Source:         https://github.com/wting/autojump/archive/release-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python3
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildArch:      noarch

%description
autojump is a faster way to navigate one's filesystem. It works by
maintaining a database of the directories one uses the most from
the command line.

Directories must be visited first before they can be jumped to.

%prep
%setup -q -n %{name}-release-v%{version}

# Fix shebangs.
sed -i 's/env python$/python3/' bin/%{name}
sed -i '/env python$/s/^.*$/# -*- python -*-/' bin/%{name}_*.py

%build
# Nothing to build.

%install
python3 install.py \
  --destdir=%{buildroot} \
  --prefix=.%{_prefix}   \
  --zshshare=.%{_datadir}/zsh/site-functions

# Fix the path.
sed -i 's|%{buildroot}/.%{_prefix}|%{_prefix}|' \
  %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh

# Redundant on Python 3.
rm %{buildroot}%{_bindir}/%{name}_argparse.py
sed -i 's/autojump_argparse/argparse/' %{buildroot}%{_bindir}/%{name}*

# Make it a proper Python module instead of polluting bindir.
sed -Ei "s/^(import|from) %{name}_(data|match|utils)/\1 %{name}.\2/" \
  %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}_*.py

mkdir -p %{buildroot}%{python3_sitelib}/%{name}/
for m in data match utils; do
    mv "%{buildroot}%{_bindir}/%{name}_$m.py" \
      "%{buildroot}%{python3_sitelib}/%{name}/$m.py"
done
echo "# -*- python -*-" > %{buildroot}%{python3_sitelib}/%{name}/__init__.py

%py3_compile %{buildroot}%{python3_sitelib}/%{name}/

%check
python3 -m pytest tests

%files
%license LICENSE
%doc AUTHORS README.md
%config %{_sysconfdir}/profile.d/%{name}.sh
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{python3_sitelib}/%{name}/
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_j
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
