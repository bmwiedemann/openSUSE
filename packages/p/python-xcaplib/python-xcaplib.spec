#
# spec file for package python-xcaplib
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-xcaplib
Version:        1.2.2
Release:        0
Summary:        Python library for managing XML documents on XCAP servers
License:        LGPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/AGProjects/python-xcaplib
Source:         https://github.com/AGProjects/python-xcaplib/archive/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       xcaplib = %{version}
%python_subpackages

%description
XCAP protocol allows a client to read, write, and modify application
configuration data stored in XML format on a server. XCAP maps XML document
sub-trees and element attributes to HTTP URIs, so that these components can
be directly accessed by HTTP.
XCAPLib includes command-line XCAP client.

%package bash-completion
Summary:        Bash Completion for Python XCAPlib
Group:          Development/Libraries/Python
Requires:       xcaplib = %{version}
Supplements:    (xcaplib and bash)

%description bash-completion
Bash completion for python's XCAP client library.

%prep
%setup -q -n %{name}-release-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/xcapclient
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand find %{buildroot}%{$python_sitelib} -name "xcapclient.py" -exec sed -i -e '/^#!\//, 1d' {} \;
install -Dpm 0644 bash_completion.d/xcapclient %{buildroot}%{_datadir}/bash-completion/completions/xcapclient

%check
# disable testsuite since it requires a live connection to an external XCAP server
#%%pytest

%post
%python_install_alternative xcapclient

%postun
%python_uninstall_alternative xcapclient

%files %{python_files}
%license LICENSE
%doc README xcapclient.ini.sample
%python_alternative %{_bindir}/xcapclient
%{python_sitelib}/xcaplib/
%{python_sitelib}/python_xcaplib-*-info

%files bash-completion
%{_datadir}/bash-completion/completions/xcapclient

%changelog
