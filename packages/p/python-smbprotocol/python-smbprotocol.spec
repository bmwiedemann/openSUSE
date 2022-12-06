#
# spec file for package python-smbprotocol
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-smbprotocol
Version:        1.10.1
Release:        0
Summary:        SMBv2/v3 client for Python 2 and 3
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jborean93/smbprotocol
#Source:         https://files.pythonhosted.org/packages/source/s/smbprotocol/smbprotocol-%%{version}.tar.gz
Source:         https://github.com/jborean93/smbprotocol/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module cryptography >= 2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyspnego}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 2.0
Requires:       python-pyspnego
Suggests:       python-gssapi >= 1.4.1
BuildArch:      noarch
%python_subpackages

%description
This library implements the SMBv2 and SMBv3 protocol.

Features
--------
-  Negotiation of the SMB 2.0.2 protocol to SMB 3.1.1 (Windows 10/Server
   2016)
-  Authentication with both NTLM and Kerberos
-  Message signing
-  Message encryption (SMB 3.x.x+)
-  Connect to a Tree/Share
-  Opening of files, pipes and directories
-  Set create contexts when opening files
-  Read and writing of files and pipes
-  Sending IOCTL commands
-  Sending of multiple messages in one packet (compounding)

%prep
%setup -q -n smbprotocol-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%{python_sitelib}/smbclient
%{python_sitelib}/smbprotocol
%{python_sitelib}/smbprotocol-%{version}*-info

%changelog
