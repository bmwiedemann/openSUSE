#
# spec file for package python-Cheetah
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-Cheetah
Version:        2.4.4
Release:        0
Summary:        Cheetah is a template engine and code generation tool
License:        MIT
URL:            http://www.cheetahtemplate.org/
Source:         https://files.pythonhosted.org/packages/source/C/Cheetah/Cheetah-%{version}.tar.gz
Patch0:         shebang.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(python)
Conflicts:      python3-Cheetah3
Provides:       python-cheetah = %{version}
Provides:       python2-Cheetah = %{version}
Obsoletes:      python-cheetah < %{version}

%description
Cheetah is an open source template engine and code generation tool.

It can be used standalone or combined with other tools and frameworks. Web
development is its principle use, but Cheetah is very flexible and is also being
used to generate C++ game code, Java, sql, form emails and even Python code.

%prep
%setup -q -n Cheetah-%{version}
# Remove she-bang lines for non-executable scripts:
%patch0 -p1

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%fdupes %{buildroot}

%files
%license LICENSE
%doc CHANGES README.markdown TODO
%{_bindir}/cheetah*
%{python_sitearch}/*

%changelog
