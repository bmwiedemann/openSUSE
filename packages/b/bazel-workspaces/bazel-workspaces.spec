#
# spec file for package bazel-workspaces
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


Name:           bazel-workspaces
Version:        20191011
Release:        0
Summary:        Bazel workspaces for libraries packaged in openSUSE
License:        Apache-2.0
Group:          Development/Tools/Building
Url:            https://github.com/kubic-project/bazel-workspaces
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildArch:      noarch

%description
Bazel workspaces for libraries packaged in openSUSE which allow to link those
libraries dynamically to software build by Bazel.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -R * %{buildroot}%{_datadir}/%{name}
rm -f %{buildroot}%{_datadir}/%{name}/{LICENSE,README.md}

%files
%license LICENSE
%doc README.md
%{_datadir}/%{name}

%changelog

