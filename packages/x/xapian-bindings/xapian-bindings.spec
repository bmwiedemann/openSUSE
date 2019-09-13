#
# spec file for package xapian-bindings
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


%bcond_with php
%define php_extension_dir %(php-config --extension-dir)
%bcond_with mono

%if 0%{?suse_version} >= 1320 && 0%{?is_opensuse}
%bcond_with sphinx
%define phpver php7
%define phppkg php7
%else
%bcond_with sphinx
%define phpver php5
%define phppkg php
%endif

Name:           xapian-bindings
Version:        1.4.9
Release:        0
Summary:        Bindings for xapian
License:        GPL-2.0-only
Group:          Development/Languages/Other
Url:            http://www.xapian.org/
Source0:        http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz
Source1:        http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Patch0:         do-not-use-sphinx.diff
Patch1:         fix-php7-directory.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  java-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libxapian-devel = %{version}
%if %{with mono}
BuildRequires:  mono-devel
%endif

%if %{with php}
BuildRequires:  %{phpver}-devel
%endif
BuildRequires:  pkg-config
BuildRequires:  python-devel >= 2.6
BuildRequires:  python-setuptools
%if %{with sphinx}
BuildRequires:  python-sphinx
BuildRequires:  python3-Sphinx
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  ruby-devel
BuildRequires:  tcl-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Xapian is a probabilistic information retrieval library. It offers an
adaptable toolkit that allows developers to add advanced indexing and
search facilities to applications.

%package -n python-xapian
Summary:        Files needed for developing Python scripts which use Xapian
Group:          Development/Libraries/Python
Provides:       python2-xapian = %{version}

%description -n python-xapian
Xapian is a probabilistic information retrieval library. It offers an
adaptable toolkit that allows developers to add advanced indexing and
search facilities to applications.
This package provides the files needed for developing Python 2 scripts
which use Xapian.

%package -n python3-xapian
Summary:        Files needed for developing Python scripts which use Xapian
Group:          Development/Libraries/Python

%description -n python3-xapian
Xapian is a probabilistic information retrieval library. It offers an
adaptable toolkit that allows developers to add advanced indexing and
search facilities to applications.
This package provides the files needed for developing Python 3 scripts
which use Xapian.

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
Group:          Development/Languages/Mono
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
%if %{with php} && %{phpver} == php7
%patch1 -p1
%endif

%build

autoreconf -vfi

%configure        \
    --with-python \
    --with-python3 \
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
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
make install DESTDIR=%{?buildroot} %{?_smp_mflags}

%files -n python-xapian
%defattr(-,root,root)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%if 0%{suse_version} < 1500 && !0%{?is_opensuse}
%doc COPYING
%else
%license COPYING
%endif
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/python/
%{python_sitearch}/xapian/

%files -n python3-xapian
%defattr(-,root,root)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%if 0%{suse_version} < 1500 && !0%{?is_opensuse}
%doc COPYING
%else
%license COPYING
%endif
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/python3/
%{python3_sitearch}/xapian/

%if %{with php}
%files -n %{phppkg}-xapian
%defattr(-,root,root)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%if 0%{suse_version} < 1500 && !0%{?is_opensuse}
%doc COPYING
%else
%license COPYING
%endif
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/php/
%{php_extension_dir}/xapian.so
%{_datadir}/%{phpver}/xapian.php
%endif

%files -n ruby-xapian
%defattr(-,root,root)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%if 0%{suse_version} < 1500 && !0%{?is_opensuse}
%doc COPYING
%else
%license COPYING
%endif
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/ruby/
%{_libdir}/ruby/site_ruby/%{rb_ver}/%{rb_arch}/_xapian.so
%{_libdir}/ruby/site_ruby/%{rb_ver}/xapian.rb

%files -n tcl8-xapian
%defattr(-,root,root)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%if 0%{suse_version} < 1500 && !0%{?is_opensuse}
%doc COPYING
%else
%license COPYING
%endif
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/tcl8/
%{_libdir}/tcl/xapian%{version}/

%if %{with mono}
%files -n xapian-csharp
%defattr(-,root,root)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%if 0%{suse_version} < 1500 && !0%{?is_opensuse}
%doc COPYING
%else
%license COPYING
%endif
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/csharp/
%{_libdir}/_XapianSharp.so
%dir %{_libdir}/mono/
%{_libdir}/mono/XapianSharp/
%dir %{_libdir}/mono/gac/
%{_libdir}/mono/gac/XapianSharp/
%endif

%changelog
