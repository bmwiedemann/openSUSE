#
# spec file for package trash-cli
#
# Copyright (c) 2025 SUSE LLC
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


Name:           trash-cli
Version:        0.24.5.26
Release:        0
Summary:        Command line interface to the freedesktop.org trashcan
License:        GPL-2.0-or-later
URL:            https://github.com/andreafrancia/trash-cli
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         remove_six.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
Requires:       python3-psutil
BuildArch:      noarch

%description
trash-cli trashes files recording the original path, deletion date, and permissions.
It uses the same trashcan used by KDE, GNOME, and XFCE, but you can invoke it from the command line (and scripts).
The command line interface is compatible with rm and you can use trash-put as an alias to rm.

%prep
%autosetup -p1

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%{_bindir}/trash*
%{_mandir}/man1/trash*
%{python_sitelib}/trash*

%changelog
