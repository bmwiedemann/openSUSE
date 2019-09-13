#
# spec file for package python-audiolazy
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# tests are incompatible with pytest 3.2 -- https://github.com/danilobellini/audiolazy/issues/6a
%bcond_with     test
Name:           python-audiolazy
Version:        0.6
Release:        0
Summary:        Real-Time Expressive Digital Signal Processing (DSP) Package for Python!
License:        GPL-3.0-only
Group:          Development/Languages/Python
Url:            http://github.com/danilobellini/audiolazy
Source:         https://files.pythonhosted.org/packages/source/a/audiolazy/audiolazy-%{version}.tar.gz
BuildRequires:  %{python_module PyAudio}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module pytest < 3.2}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module sympy}
%endif
BuildArch:      noarch
Requires:       python-PyAudio
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-scipy

%python_subpackages

%description
AudioLazy is a package written in pure Python proposing digital audio signal
processing (DSP).

It prioritizes code expressiveness, clarity and simplicity, without precluding
the lazy evaluation, and can be used together with Numpy, Scipy and
Matplotlib as well as default Python structures like lists and generators.

It also features:

- A ``Stream`` class for finite and endless signals representation with
  elementwise operators (auto-broadcast with non-iterables) in a common
  Python iterable container accepting heterogeneous data;
- Strongly sample-based representation (Stream class) with easy conversion
  to block representation using the ``Stream.blocks(size, hop)`` method;
- Sample-based interactive processing with ``ControlStream``;
- ``Streamix`` mixer for iterables given their starting time deltas;
- Multi-thread audio I/O integration with PyAudio;
- Linear filtering with Z-transform filters directly as equations (e.g.
  ``filt = 1 / (1 - .3 * z ** -1)``), including linear time variant filters
  (i.e., the ``a`` in ``a * z ** k`` can be a Stream instance), cascade
  filters (behaves as a list of filters), resonators, etc.. Each
  ``LinearFilter`` instance is compiled just in time when called;
- Zeros and poles plots and frequency response plotting integration with
  MatPlotLib;
- Linear Predictive Coding (LPC) directly to ``ZFilter`` instances, from
  which you can find PARCOR coeffs and LSFs;
- Both sample-based (e.g., zero-cross rate, envelope, moving average,
  clipping, unwrapping) and block-based (e.g., window functions, DFT,
  autocorrelation, lag matrix) analysis and processing tools;
- A simple synthesizer (Table lookup, Karplus-Strong) with processing tools
  (Linear ADSR envelope, fade in/out, fixed duration line stream) and basic
  wave data generation (sinusoid, white noise, impulse);
- Biological auditory periphery modeling (ERB and gammatone filter models);
- Multiple implementation organization as ``StrategyDict`` instances:
  callable dictionaries that allows the same name to have several different
  implementations (e.g. ``erb``, ``gammatone``, ``lowpass``, ``resonator``,
  ``lpc``, ``window``);
- Converters among MIDI pitch numbers, strings like "F#4" and frequencies;
- Polynomials, Stream-based functions from itertools, math, cmath, and more!
  Go try yourself! =)

%prep
%setup -q -n audiolazy-%{version}
sed -i 's/\r$//' *.rst
sed -i 's/\r$//' *.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_expand py.test-%{$python_bin_suffix}
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGES.rst README.rst
%license COPYING.txt
%{python_sitelib}/audiolazy/
%{python_sitelib}/audiolazy-%{version}-py*.egg-info

%changelog
