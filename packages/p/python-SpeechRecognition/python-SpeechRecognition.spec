#
# spec file for package python-SpeechRecognition
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define justpython python
Name:           python-SpeechRecognition
Version:        3.8.1
Release:        0
Summary:        Library for performing speech recognition, with support for several engines
# Note: The sources include third party code with different licenses.
# We remove all those before building so it's not installed in the
# generated packages.
License:        BSD-3-Clause
URL:            https://github.com/Uberi/speech_recognition#readme
Source:         https://github.com/Uberi/speech_recognition/archive/%{version}.tar.gz
# Remove information about unbundled libraries.
Patch0:         fix-readme.patch
# PATCH-FIX-UPSTREAM 406-google-cloud-speech.patch gh#Uberi/speech_recognition#406 mcepl@suse.com
# Switch dependency to google-cloud-speech from deprecated oauth2client and googleapiclient
Patch1:         406-google-cloud-speech.patch
BuildRequires:  %{python_module google-cloud-speech}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{justpython}-SpeechRecognition-common-en-US
Requires:       flac
Requires:       python-PyAudio
Requires:       python-google-cloud-speech
Recommends:     python-pocketsphinx-python
BuildArch:      noarch
%python_subpackages

%description
SpeechRecognition Library for performing speech recognition, with support for several engines and APIs, online and offline.

The Speech recognition engine/API supports CMU Sphinx (works offline), Google Speech Recognition,
Google Cloud Speech API, Wit.ai, Microsoft Bing Voice Recognition, Houndify API and
IBM Speech to Text

%package -n python-SpeechRecognition-common-en-US
Summary:        Common files for en-US language model support in python-speech_recognition

%description -n python-SpeechRecognition-common-en-US
SpeechRecognition Library for performing speech recognition, with support for
several engines and APIs, online and offline.

The Speech recognition engine/API supports CMU Sphinx (works offline), Google
Speech Recognition, Google Cloud Speech API, Wit.ai, Microsoft Bing Voice
Recognition, Houndify API and IBM Speech to Text.

This package contains the data for en-US language model to be used by
pocketsphinx from python-SpeechRecognition.

%prep
%autosetup -p1 -n speech_recognition-%{version}

rm -Rf third-party
rm speech_recognition/flac-*
rm LICENSE-FLAC.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mkdir -p %{buildroot}%{_datadir}/speech_recognition
cp -Ra speech_recognition/pocketsphinx-data %{buildroot}%{_datadir}/speech_recognition/
%python_expand rm -Rf %{buildroot}%{$python_sitelib}/speech_recognition/pocketsphinx-data
%python_expand ln -s %{_datadir}/speech_recognition/pocketsphinx-data %{buildroot}%{$python_sitelib}/speech_recognition/

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*
%dir %{_datadir}/speech_recognition/
%dir %{_datadir}/speech_recognition/pocketsphinx-data

%files -n python-SpeechRecognition-common-en-US
%{_datadir}/speech_recognition/pocketsphinx-data/en-US

%changelog
