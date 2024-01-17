#
# spec file for package cmuclmtk
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           cmuclmtk
Version:        0.7
Release:        0
Summary:        CMU-Cambridge Statistical Language Modeling toolkit
License:        AFL-2.1 and BSD-3-Clause
Group:          System/Libraries
Url:            http://cmusphinx.sourceforge.net
Source:         %{name}-%{version}.tar.gz
Patch1:         decl-mismatch.patch
Patch2:         0002-Fix-includes.patch
Patch3:         0003-Fix-endian-check.patch
Patch4:         0004-Fix-vocab_size.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc
BuildRequires:  gmake
BuildRequires:  gawk

%description
The CMU-Cambridge Language Modeling Toolkit is a free set of tools
for constructing and testing statistical N-Gram language models.
These models have various applications including speech recognition,
machine translation, optical character and handwriting recognition.

This package contains the front-end tools for easy language model
training as well as the basic tools for manipulating N-Gram and text files.

%package -n libcmuclmtk0
Summary:        CMU-Cambridge Statistical Language Modeling toolkit
Group:          System/Libraries

%description -n libcmuclmtk0
The CMU-Cambridge Language Modeling Toolkit is a free set of tools
for constructing and testing statistical N-Gram language models.
These models have various applications including speech recognition,
machine translation, optical character and handwriting recognition.

This package contains the shared library used by the CMU-Cambridge
Language Model Toolkit.

%package -n libcmuclmtk-devel
Summary:        CMU-Cambridge Statistical Language Modeling toolkit
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libcmuclmtk0 = %{version}

%description -n libcmuclmtk-devel
The CMU-Cambridge Language Modeling Toolkit is a free set of tools
for constructing and testing statistical N-Gram language models.
These models have various applications including speech recognition,
machine translation, optical character and handwriting recognition.

This package contains the include files and libraries used to compile
programs using the CMU-Cambridge Language Model Toolkit.

%prep
%setup -q
%patch1 -p1
%patch2
%patch3
%patch4

%build
%configure
make %{_smp_mflags}

%install
make DESTDIR=%{buildroot} install

rm -rf %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_libdir}/*.la

%check
make check || true

%post -n libcmuclmtk0 -p /sbin/ldconfig

%postun -n libcmuclmtk0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS README NEWS COPYING TODO
%{_bindir}/binlm2arpa
%{_bindir}/evallm
%{_bindir}/idngram2lm
%{_bindir}/idngram2stats
%{_bindir}/lm_combine
%{_bindir}/lm_interpolate
%{_bindir}/mergeidngram
%{_bindir}/ngram2mgram
%{_bindir}/text2idngram
%{_bindir}/text2wfreq
%{_bindir}/text2wngram
%{_bindir}/wfreq2vocab
%{_bindir}/wngram2idngram

%files -n libcmuclmtk0
%defattr(-,root,root)
%{_libdir}/libcmuclmtk.so.0
%{_libdir}/libcmuclmtk.so.0.0.0

%files -n libcmuclmtk-devel
%defattr(-,root,root)
%{_includedir}/cmuclmtk/
%{_libdir}/libcmuclmtk.so

%changelog
