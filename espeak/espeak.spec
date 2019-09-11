#
# spec file for package espeak
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           espeak
%define _major_version 1.48
Version:        %{_major_version}.04
Release:        0
%define _version %{version}-source
Summary:        Software speech synthesizer (text-to-speech)
License:        GPL-3.0+
Group:          Productivity/Other
Url:            http://espeak.sourceforge.net
Source:         http://sourceforge.net/projects/espeak/files/espeak/espeak-%{_major_version}/espeak-%{_version}.zip
Source1:        espeak.1
Source2:        mb-lt1
Source3:        mb-lt2
Patch:          easpeak-fix-bufferoverflow-strncpy.patch
Patch1:         gcc6-char-cast.patch
BuildRequires:  gcc-c++
BuildRequires:  portaudio-devel
BuildRequires:  pulseaudio-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
eSpeak is a compact open source software speech synthesizer for English
and other languages.

eSpeak uses a "formant synthesis" method. This allows many languages to
be provided in a small size. The speech is clear, and can be used at
high speeds, but is not as natural or smooth as larger synthesizers
which are based on human speech recordings.

%package devel
Summary:        Software speech synthesizer (text-to-speech) -- Development Files
Group:          Development/Languages/C and C++ 
Requires:       espeak = %{version}

%description devel
eSpeak is a compact open source software speech synthesizer for English
and other languages.

eSpeak uses a "formant synthesis" method. This allows many languages to
be provided in a small size. The speech is clear, and can be used at
high speeds, but is not as natural or smooth as larger synthesizers
which are based on human speech recordings.

%prep
# Probably a mistake from upstream
%setup -q -n %{name}-%{version}-source
%patch -p1
%patch1 -p1
# Don't use the included binary voice dictionaries; we compile these from
# source
%{__rm} espeak-data/*_dict
# Build against portaudio v19 (see ReadMe)
%{__cp} -f src/portaudio19.h src/portaudio.h
# Remove executable bits of documentation
chmod a-x docs/*.html
chmod a-x docs/speak_lib.h
%{__cp} %{SOURCE2} espeak-data/voices/mb/
%{__cp} %{SOURCE3} espeak-data/voices/mb/

%build
cd src
make %{?_smp_mflags} CXXFLAGS="%{optflags}"
cd ..
# Compile the TTS voice dictionaries
export ESPEAK_DATA_PATH=$RPM_BUILD_DIR/espeak-%{version}-source
cd dictsource
# Strange sed regex to parse ambiguous output from 'speak --voices', filled upstream BZ 3608811
for voice in $(../src/speak --voices | \
LANG=C sed -n '/Age\/Gender/ ! s/ *[0-9]\+ *\([^ ]\+\) *M\? *[^ ]\+ *\(\((\|[A-Z]\)[^ ]\+\)\? *\([^ ]\+\).*/\1 \4/ p' | \
sort | uniq); do \
    ../src/speak --compile=$voice; \
done

%install
cd src
make LIBDIR=%{_libdir} DESTDIR=%{buildroot} install
cd ..
# Remove static libraries
%{__rm} %{buildroot}%{_libdir}/*.a
# Install manpage
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/espeak.1
# Rename docs subdir for installation with %doc
%{__mv} docs/ html/
# Fix wrong-script-end-of-line-encoding rpmlint warning
sed -i 's/\r$//' %{buildroot}%{_datadir}/espeak-data/voices/other/lfn

%pre
# Support for seamless update
# Remove when 13.1 is out of update scope
# or when this is directory again
test -d %{_datadir}/espeak-data/voices/en && rm -rf %{_datadir}/espeak-data/voices/en
exit 0

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr (-,root,root,755)
%doc ChangeLog.txt License.txt ReadMe html/
%{_bindir}/espeak
%{_libdir}/libespeak.so.*
%{_datadir}/espeak-data/
%{_mandir}/man1/espeak.1.*

%files devel
%defattr (-,root,root,755)
%{_includedir}/espeak/
%{_libdir}/libespeak.so

%changelog
