#
# spec file for package legendary
#
# Copyright (c) 2026 SUSE LLC and contributors
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

Name:           legendary
Version:        0.20.41
Release:        0
Summary:        An Epic Games Launcher alternative
License:        GPL-3.0-only
URL:            https://github.com/Heroic-Games-Launcher/legendary.git
Source:         %{name}-%{version}.tar.gz
BuildRequires:  python313-filelock
BuildRequires:  python313-PyInstaller
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module requests < 3.0}
BuildRequires:  %{python_module requests-futures}
Requires:       %{python_module requests-futures}
%ifarch aarch64
ExclusiveArch: aarch64
%endif
%ifarch x86_64
ExclusiveArch: x86_64
%endif

%description
A replacement for the Epic Games Launcher.

%prep
%autosetup -p1

%build
pyinstaller --onefile --name legendary legendary/cli.py

%install
install -Dm0755 dist/legendary %{buildroot}/%{_bindir}/legendary

%files
%license LICENSE*
%{_bindir}/legendary

%changelog
