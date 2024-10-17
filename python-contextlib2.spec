%define modname contextlib2

Name:               python-contextlib2
Version:            0.5.0
Release:            1
Summary:            Backports and enhancements for the contextlib module
Group:              Development/Python
License:            Python
URL:                https://pypi.python.org/pypi/contextlib2
Source0:            https://pypi.python.org/packages/source/c/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:          noarch
BuildRequires:      python2-devel
BuildRequires:      python3-devel
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools

%description
contextlib2 is a backport of the standard library's contextlib module to
earlier Python versions.

It also serves as a real world proving ground for possible future
enhancements to the standard library version.

%package -n python2-contextlib2
Summary:            Backports and enhancements for the contextlib module
Group:              Development/Python

%description -n python2-contextlib2
contextlib2 is a backport of the standard library's contextlib module to
earlier Python versions.

It also serves as a real world proving ground for possible future
enhancements to the standard library version.

%prep
%setup -q -n %{modname}-%{version}

sed -i 's/unittest2/unittest/' test_contextlib2.py

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info
rm -rf %{py2dir}
cp -a . %{py2dir}

sed -i 's/unittest2/unittest/' test_contextlib2.py

%build
python setup.py build
pushd %{py2dir}
python2 setup.py build
popd

%install
pushd %{py2dir}
python2 setup.py install -O1 --skip-build --root=%{buildroot}
popd
python setup.py install -O1 --skip-build --root=%{buildroot}

%check
python test_contextlib2.py
pushd %{py2dir}
#python2 test_contextlib2.py
popd

%files
%doc README.md VERSION.txt NEWS.rst LICENSE.txt
%{py_puresitedir}/%{modname}.py*
%{py_puresitedir}/%{modname}-%{version}*

%files -n python2-contextlib2
%doc README.md VERSION.txt NEWS.rst LICENSE.txt
%{py2_puresitedir}/%{modname}.py*
%{py2_puresitedir}/%{modname}-%{version}-*

