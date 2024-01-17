#
# spec file for package docker-bench-security
#
# Copyright (c) 2020 SUSE LLC
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


Name:           docker-bench-security
Version:        1.3.5
Release:        0
Summary:        Docker Bench for Security
License:        Apache-2.0
Group:          Productivity/Networking/Security
URL:            https://dockerbench.com
Source:         https://github.com/docker/docker-bench-security/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       audit
Requires:       docker >= 1.13.0
Requires:       findutils
Requires:       net-tools
%if 0%{?suse_version} > 1320
Requires:       net-tools-deprecated
%endif
%if %{?suse_version} > 1110
BuildArch:      noarch
%endif

%description
The Docker Bench for Security is a script that checks for dozens of common
best-practices around deploying Docker containers in production.

The tests are all automated, and implement the CIS Docker Benchmark.

%prep
%setup -q

%build
sed -i \
	-e 's|\./output_lib.sh|%{_libexecdir}/%{name}/output_lib.sh|' \
	-e 's|\./helper_lib.sh|%{_libexecdir}/%{name}/helper_lib.sh|' \
	-e 's|\./functions_lib.sh|%{_libexecdir}/%{name}/functions_lib.sh|' \
	-e 's|for test in tests|for test in %{_libexecdir}/%{name}/tests|' \
	-e 's|\./"$test"|"$test"|' \
	docker-bench-security.sh
chmod +x docker-bench-security.sh

%install
install -D %{name}.sh %{buildroot}/%{_bindir}/docker-bench-security
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -vpr *_lib.sh tests/ %{buildroot}%{_libexecdir}/%{name}

%files
%license LICENSE.md
%doc README.md
%doc distros
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_libexecdir}/%{name}

%changelog
