#
# spec file for package xapian-bindings
#
# Copyright (c) 2023 SUSE LLC
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


%define php_extension_dir %(php-config --extension-dir)
%if 0%{?suse_version} >= 1320 && 0%{?is_opensuse}
%define phpver php7
%define phppkg php7
%bcond_with sphinx
%else
%define phpver php5
%define phppkg php
%bcond_with sphinx
%endif
%bcond_with php
%bcond_with mono
%define skip_python2 1
Name:           xapian-bindings
Version:        1.4.21
Release:        0
Summary:        Bindings for xapian
License:        GPL-2.0-only
Group:          Development/Languages/Other
URL:            https://www.xapian.org/
Source0:        https://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz
Source1:        https://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Patch0:         do-not-use-sphinx.diff
Patch1:         fix-php7-directory.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  java-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libxapian-devel = %{version}
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  ruby-devel
BuildRequires:  tcl-devel
BuildRequires:  xz
%if %{with mono}
BuildRequires:  mono-devel
%endif
%if %{with php}
BuildRequires:  %{phpver}-devel
%endif
%if %{with sphinx}
BuildRequires:  python3-Sphinx
%endif
%if 0%{?sle_version} == 150400
# python38_version_nodots doesn't evaluate correctly in 150400
%define python_files() -n python3-%{**}
%define python_sitearch %{python3_sitearch}
%else
%if 0%{?suse_version} >= 1550
# If we have multiple python flavors, build bindings for all of them
%define python_subpackage_only 1
%python_subpackages
%else
%define python_files() -n python3-%{**}
%define python_sitearch %{python3_sitearch}
%endif
%endif

%description
Xapian is a probabilistic information retrieval library. It offers an
adaptable toolkit that allows developers to add advanced indexing and
search facilities to applications.

%if 0%{?python_subpackage_only}
%package -n python-xapian
Summary:        Files needed for developing Python scripts which use Xapian
Group:          Development/Libraries/Python

%description -n python-xapian
Xapian is a probabilistic information retrieval library. It offers an
adaptable toolkit that allows developers to add advanced indexing and
search facilities to applications.
This package provides the files needed for developing Python 3 scripts
which use Xapian.
%else

%package -n python3-xapian
Summary:        Files needed for developing Python scripts which use Xapian
Group:          Development/Libraries/Python

%description -n python3-xapian
Xapian is a probabilistic information retrieval library. It offers an
adaptable toolkit that allows developers to add advanced indexing and
search facilities to applications.
This package provides the files needed for developing Python 3 scripts
which use Xapian.
%endif

%if %{with php}
%package -n %{phppkg}-xapian
Summary:        Files needed for developing PHP scripts which use Xapian
Group:          Productivity/Networking/Web/Servers
Requires:       %{phpver}

%description -n %{phppkg}-xapian
Xapian is a probabilistic information retrieval library. It offers an
adaptable toolkit that allows developers to add advanced indexing and
search facilities to applications.
This package provides the files needed for developing PHP scripts
which use Xapian.
%endif

%package -n ruby-xapian
Summary:        Files needed for developing Ruby scripts which use Xapian
Group:          Development/Languages/Ruby
Requires:       ruby

%description -n ruby-xapian
Xapian is a probabilistic information retrieval library. It offers an
adaptable toolkit that allows developers to add advanced indexing and
search facilities to applications.
This package provides the files needed for developing Ruby scripts
which use Xapian.

%package -n tcl8-xapian
Summary:        Files needed for developing TCL scripts which use Xapian
Group:          Development/Libraries/Tcl
Requires:       tcl

%description -n tcl8-xapian
Xapian is a probabilistic information retrieval library. It offers an
adaptable toolkit that allows developers to add advanced indexing and
search facilities to applications.
This package provides the files needed for developing Tcl scripts
which use Xapian.

%package -n xapian-csharp
Summary:        Files needed for developing C# applications which use Xapian
Group:          Development/Languages/Other
Requires:       mono-core

%description -n xapian-csharp
Xapian is a probabilistic information retrieval library. It offers an
adaptable toolkit that allows developers to add advanced indexing and
search facilities to applications.
This package provides the files needed for developing C# applications
which use Xapian.

%prep
%setup -q
%if %{without sphinx}
%patch0 -p1
%endif
%if %{with php} && "%{phpver}" == "php7"
%patch1 -p1
%endif

#remove shebang in python examples
sed -i '1{/env python/ d}' python3/docs/examples/*.py

%build

autoreconf -vfi
mv python3 python3_plain
%{python_expand # configure different python flavors first
cp -r python3_plain python3
export PYTHON3=%{_bindir}/$python
%configure --with-python3  --docdir=%{_docdir}/%{name}
mv python3 python%{$python_bin_suffix}
}
mv python3_plain python3
%configure        \
    --without-python \
    --without-python3 \
%if %{with php}
    --with-%{phppkg} \
%endif
    --with-ruby   \
    --with-tcl    \
%if %{without mono}
    --without-csharp \
%else
    --with-csharp \
%endif
    --docdir=%{_docdir}/%{name}
%make_build
%{python_expand # make for each python flavor
pushd python%{$python_bin_suffix}
%make_build
popd
}

%check
%make_build check
%{python_expand # check for each python flavor
pushd python%{$python_bin_suffix}
%make_build check
popd
}

%install
make install DESTDIR=%{?buildroot} %{?_smp_mflags}
%{python_expand # make for each python flavor
pushd python%{$python_bin_suffix}
make install DESTDIR=%{?buildroot} %{?_smp_mflags}
popd
# packaged twice
rm -r %{?buildroot}/%{_docdir}/%{name}/python3/examples
mv %{?buildroot}/%{_docdir}/%{name}/python{3,%{$python_bin_suffix}}
chmod a-x %{?buildroot}/%{_docdir}/%{name}/python%{$python_bin_suffix}/docs/examples/*.py
chmod a-x %{?buildroot}/%{_docdir}/%{name}/python%{$python_bin_suffix}/docs/introduction.rst
d=%{?buildroot}/%{$python_sitearch}
find $d -name '*.pyc' -delete
$python -m compileall $d
$python -O -m compileall $d
%fdupes %{?buildroot}/%{$python_sitearch}
}

%files %{python_files xapian}
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%license COPYING
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/python%{python_bin_suffix}/
%{python_sitearch}/xapian/

%if %{with php}
%files -n %{phppkg}-xapian
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%license COPYING
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/php/
%{php_extension_dir}/xapian.so
%{_datadir}/%{phpver}/xapian.php
%endif

%files -n ruby-xapian
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%license COPYING
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/ruby/
%{_libdir}/ruby/site_ruby/%{rb_ver}/%{rb_arch}/_xapian.so
%{_libdir}/ruby/site_ruby/%{rb_ver}/xapian.rb

%files -n tcl8-xapian
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%license COPYING
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/tcl8/
%{_libdir}/tcl/xapian%{version}/

%if %{with mono}
%files -n xapian-csharp
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%license COPYING
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/csharp/
%{_libdir}/_XapianSharp.so
%dir %{_libdir}/mono/
%{_libdir}/mono/XapianSharp/
%dir %{_libdir}/mono/gac/
%{_libdir}/mono/gac/XapianSharp/
%endif

%changelog
