#
# spec file for package python-qpid
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           python-qpid
Version:        1.37.0
Release:        0
Summary:        Apache Qpid Python client library for AMQP
License:        Apache-2.0
Group:          Development/Libraries/Python
Url:            http://qpid.apache.org
Source0:        http://www.apache.org/dist/qpid/python/%{version}/qpid-python-%{version}.tar.gz
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  python-xml
Provides:       %{name}-common = %{version}
Obsoletes:      %{name}-common < %{version}
%if 0%{?suse_version} >= 1200
BuildArch:      noarch
%endif

%description
The Apache Qpid Python client library for AMQP.

%files
%doc LICENSE.txt
%doc NOTICE.txt README.md examples
%dir %{python_sitelib}/qpid
%{python_sitelib}/qpid/messaging/
%{python_sitelib}/qpid/saslmech/
%{python_sitelib}/mllib
%{python_sitelib}/qpid/*.py*
%{python_sitelib}/qpid/specs
%{python_sitelib}/qpid/tests
%{_bindir}/qpid-python-test
%exclude %{_bindir}/qpid-python-test.bat
%if "%{python_version}" >= "2.6"
%{python_sitelib}/qpid_python-*.egg-info
%endif

%package -n qpid-tests
Summary:        Conformance tests for Apache Qpid
Group:          Development/Libraries/Python
Requires:       python-qpid >= 1.35.0
Requires:       python-qpid-qmf >= 1.35.0

%description -n qpid-tests
Conformance tests for Apache Qpid.

%files -n qpid-tests
%{python_sitelib}/qpid_tests/
%doc NOTICE.txt
%doc LICENSE.txt

%prep
%setup -q -n qpid-python-%{version}
cd ..

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install \
    --skip-build \
    --prefix %{_prefix} \
    --install-purelib %{python_sitelib} \
    --root %{buildroot}

chmod +x %{buildroot}/%{python_sitelib}/qpid/codec.py
chmod +x %{buildroot}/%{python_sitelib}/qpid/tests/codec.py
chmod +x %{buildroot}/%{python_sitelib}/qpid/reference.py
chmod +x %{buildroot}/%{python_sitelib}/qpid/managementdata.py
chmod +x %{buildroot}/%{python_sitelib}/qpid/disp.py

%changelog
