#
# spec file for package python-pushy
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


#
%define skip_python3 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pushy
Version:        0.5.4
Release:        0
Summary:        A library for transparently accessing objects in a remote Python interpreter
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pushyrpc/pushy
Source:         https://files.pythonhosted.org/packages/source/p/pushy/pushy-%{version}.zip
BuildRequires:  %{python_module paramiko}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-paramiko
BuildArch:      noarch
%python_subpackages

%description
Pushy is a Python library for allowing one to connect to a remote Python
interpreter, and transparently access objects in that interpreter as if they
were objects within the local interpreter.

Pushy has the novel ability to execute a remote Python interpreter and start a
request servicing loop therein, without requiring any custom Python libraries
(including Pushy) to be initially present. To accomplish this, Pushy requires
an SSH daemon to be present on the remote machine.

Pushy was initially developed to simplify automated testing to the point that
testing software on remote machines becomes little different to testing on the
local machine.

%prep
%setup -q -n pushy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*

%changelog
