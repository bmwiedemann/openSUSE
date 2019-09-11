#
# spec file for package rstudio
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

Name:           rstudio
Version:        1.2.679
Release:        0
Summary:        Integrated Development Environment for GNU R
License:        AGPL-3.0
Group:          Development/Tools/IDE
Url:            http://www.rstudio.com/
Source:         https://github.com/rstudio/rstudio/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://s3.amazonaws.com/rstudio-buildtools/libclang-3.5.zip
Source2:        https://s3.amazonaws.com/rstudio-buildtools/pandoc-1.17.2.zip
Source3:        https://s3.amazonaws.com/rstudio-dictionaries/core-dictionaries.zip
Source4:        https://s3.amazonaws.com/rstudio-buildtools/mathjax-26.zip
Source5:        https://s3.amazonaws.com/rstudio-buildtools/gwt-2.8.1.zip
Source6:        https://s3.amazonaws.com/rstudio-buildtools/gin-2.1.2.zip
# URL is broken https://github.com/rstudio/rstudio/issues/4088
Source7:        plumber-0.4.6.zip
BuildRequires:  R-base-devel >= 2.11.1
BuildRequires:  R-rsconnect
BuildRequires:  xml-commons-jaxp-1.4-apis 
BuildRequires:  xml-commons-resolver12
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  boost-devel >= 1.68
BuildRequires:  build
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 4.8
BuildRequires:  gcc-fortran
BuildRequires:  hicolor-icon-theme
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
# has to be built with Java 7 https://github.com/rstudio/rstudio/issues/1837
BuildRequires:  java-devel = 1.8.0
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(pango)
BuildRequires:  unzip
%if 0%{?suse_version} >= 1330
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_signals-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_random-devel
BuildRequires:  libboost_iostreams-devel
%else
BuildRequires:  boost-devel
%endif
# TODO: unbundle https://github.com/rstudio/rstudio/issues/1614
#BuildRequires:  mathjax
#BuildRequires:  pandoc
#BuildRequires:  libclang
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(Qt5Sensors)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5DBus)
Recommends:     R-base-devel
Requires:       R-rsconnect
#Requires:       R-plumber
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
RStudio is a set of integrated tools designed to help you be more productive
with R. It includes a console, syntax-highlighting editor that supports direct
code execution, as well as tools for plotting, history, and workspace management.

%prep
%setup -q

# unpack libclang
mkdir -p dependencies/common/libclang/
unzip -qd dependencies/common/libclang %{SOURCE1}
mv dependencies/common/libclang/libclang-3.5/include/clang-c dependencies/common/libclang/builtin-headers
mkdir -p dependencies/common/libclang/3.5

# unpack pandoc
mkdir -p dependencies/common/pandoc/1.17.2
unzip -qd dependencies/common/pandoc/1.17.2 %{SOURCE2}

# unpack core-dictionaries.zip to
mkdir -p dependencies/common/dictionaries
unzip -qd dependencies/common/dictionaries %{SOURCE3}

# unpack mathjax
unzip -qd dependencies/common/ %{SOURCE4}

mkdir -p dependencies/common/plumber
unzip -qd dependencies/common/plumber/ %{SOURCE7} 

# unpack gwt to
mkdir -p src/gwt/lib/gwt
unzip -qd src/gwt/lib/gwt/ %{SOURCE5}
mv src/gwt/lib/gwt/gwt-2.8.1 src/gwt/lib/gwt/2.8.1

# unpack gin to
mkdir -p src/gwt/lib/gin/2.1.2
unzip -qd src/gwt/lib/gin/2.1.2 %{SOURCE6}


%build
%cmake -DRSTUDIO_TARGET=Desktop -DCMAKE_BUILD_TYPE=Release -DQT_QMAKE_EXECUTABLE=OFF -DCMAKE_INSTALL_PREFIX=%{_libexecdir}/rstudio
make %{?_smp_mflags}

%install
%cmake_install

install -d -m 0755 %{buildroot}%{_bindir}
ln -s %{_libexecdir}/rstudio/bin/%{name} %{buildroot}%{_bindir}/%{name}

# make rpmlint happy
%if 0%{?suse_version} > 1030
%fdupes -s %{buildroot}%{_libexecdir}/rstudio/R
%fdupes -s %{buildroot}%{_libexecdir}/rstudio/resources
%endif

# cleanup
find %{buildroot}%{_libexecdir}/rstudio -name .gitignore -delete
find %{buildroot}%{_libexecdir}/rstudio -name .Rbuildignore -delete
rm %{buildroot}%{_libexecdir}/rstudio/{INSTALL,COPYING,NOTICE,README.md,SOURCE}

%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files
%defattr(-,root,root)
%doc COPYING NOTICE README.md
%{_bindir}/%{name}
%{_libexecdir}/rstudio
%{_datadir}/applications/rstudio.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/rstudio.xml
%{_datadir}/pixmaps/rstudio.png

%changelog
