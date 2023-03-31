Name:		texlive-bxdvidriver
Version:	43219
Release:	2
Summary:	Enables specifying a driver option effective only in DVI output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxdvidriver
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxdvidriver.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxdvidriver.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This single-function package enables authors to specify a
global driver option (dvips, dvipdfmx, etc) which is applied
only when the engine outputs a DVI file. It is useful to create
special document- templates that can be compiled in both
PDF-mode and DVI-mode.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxdvidriver
%doc %{_texmfdistdir}/doc/latex/bxdvidriver

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
