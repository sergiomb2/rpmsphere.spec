Name:           python3-bokeh
Version:        2.0.2
Release:        1.1
Summary:        Statistical interactive HTML plots for Python
License:        BSD-3-Clause
URL:            https://github.com/bokeh/bokeh/
Source:         https://files.pythonhosted.org/packages/source/b/bokeh/bokeh-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python-rpm-macros
BuildConflicts: python-buildservice-tweak
Requires:       python-Jinja2 >= 2.7
Requires:       python-Pillow >= 4.0
Requires:       python-PyYAML >= 3.10
Requires:       python-numpy >= 1.11.3
Requires:       python-packaging >= 16.8
Requires:       python-python-dateutil >= 2.1
Requires:       python-tornado >= 5
Requires:       python-typing_extensions >= 3.7.4
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%description
Bokeh is a Python interactive visualization library that targets web
browsers for presentation. It provides concise construction of
graphics in the style of D3.js, and favors delivering this capability
with interactivity over large or streaming datasets.

%prep
%setup -q -n bokeh-%{version}

%build
%py3_build

%install
%py3_install
#py3_clone -a %{buildroot}%{_bindir}/bokeh

# Remove hidden files
rm %{buildroot}%{python3_sitelib}/bokeh/server/static/.keep

# Remove test and script files
rm -rf %{buildroot}%{python3_sitelib}/scripts/
rm -rf %{buildroot}%{python3_sitelib}/tests/

%files
%license LICENSE.txt
%doc CHANGELOG README.md
%{_bindir}/bokeh
%{python3_sitelib}/bokeh*

%changelog
* Sat Jun  6 2020 Atri Bhattacharya <badshah400@gmail.com>
- Update to version 2.0.2
  * Allow multiple versions of BokehJS on a page
    [gh#bokeh/bokeh#9812].
  * Cross-timezone issue with session token expiry
    [gh#bokeh/bokeh#9938].
  * Fix server resources with Django integration
    [gh#bokeh/bokeh#9724].
  * Make add_layout update a figure [gh#bokeh/bokeh#8862].
  * BoxAnnotation ignores fill_color=None [gh#bokeh/bokeh#9877].
  * A handful of documentation clarifications, corrections, and
    expansions
  * For full list of changes see %%{_docdir}/%%{name}/CHANGELOG.
- Changes from version 2.0.1 and 2.0.0:
  * See https://docs.bokeh.org/en/latest/docs/releases.html.
- Python2 support dropped since version 2.0.0:
  * Set skip_python2 to 1.
  * Drop conditionals for python2.
- Update BuildRequires, Requires, and Recommends in keeping with
  upstream setup.py.
- Replace tests in %%check with simple `%%python_exec setup.py
  test`; still doesn't work though.
- The examples directory no longer exists; remove from file list.
* Thu Apr 23 2020 Tomáš Chvátal <tchvatal@suse.com>
- Fix build without python2
* Sat Nov  9 2019 Arun Persaud <arun@gmx.de>
- update to version 1.4.0:
  * bugfixes:
    + #8402 [component: bokehjs] No clean way to update vbar_stack
    + #8778 [component: bokehjs] Hover over image is showing wrong
    @image tooltip on flipped axis
    + #8976 [component: bokehjs] [bug] geographical plots cannot be
    saved with the save tool
    + #9035 [component: bokehjs] [widgets] [bug] spinner only
    considers 1 decimal
    + #9129 [component: bokehjs] [widgets] [bug]datepicker displayed
    value is not updating correctly
    + #9136 [component: bokehjs] Inner_width and inner_height not
    available after display
    + #9143 [component: docs] [bug] roadmap link on docs page links to
    a nonexistent page
    + #9152 [component: bokehjs] [bug] hover tooltip breaks with
    full-circle wedge
    + #9174 [component: bokehjs] [bug] nan_color argument in
    linearcolormapper is not used
    + #9185 [component: bokehjs] [regression] [bug] exporting google
    maps pngs sometimes not working properly
    + #9240 [component: build] [bug] building custom extension breaks
    in notebook
    + #9266 [component: bokehjs] [widgets] [bug] datatable sorting
    broken
    + #9267 [component: bokehjs] [bug] range_tool selection is
    over-responsive in y direction
    + #9309 [API: models] [component: docs] [bug] documentation panels
    empty
    + #9317 [regression] [bug] splattable lists no longer allow using
    list-like methods
    + #9324 [component: bokehjs] [bug] background property change not
    working for widgetbox
    + #9338 [component: bokehjs] Include license in bokehjs bundles
    + #9342 [component: bokehjs] [component: server] [regression]
    [bug] server examples with custom models do not work
    + #9343 [component: bokehjs] Save does not work with custom models
    [bug]
  * features:
    + #3700 Structured way to get at documents from javascript
    + #8904 [API: models] Allow to offset plot frame's side panel
    annotations
    + #9009 [component: server] Add support django channels
    + #9135 Be able to order legend items when using groupby legend
    [feature]
    + #9137 [API: models] [notebook] Allow to integrate bokeh models
    with ipywidgets
    + #9139 [component: server] Support ssl termination
    + #9140 [component: server] Support tornado get_current_user
    + #9144 [component: bokehjs] Axis rescaled when legend item
    visibility changed [feature]
    + #9196 [component: bokehjs] [component: build] Add support for
    building bokehjs extensions
    + #9209 [component: server] Add support for globs to `bokeh serve`
    + #9241 Add 256-color palettes, add a function to generate
    diverging palettes
    + #9298 [feature] provide mouse press up event
  * tasks:
    + #8209 [component: docs] Searchable documentation?
    + #9002 [component: bokehjs] [component: build] Unify bokehjs
    build system with extensions' compiler
    + #9070 Improve bokeh/util/logconfig.py call signature
    + #9073 [component: docs] [docs] page for selection tools does not
    tell users how to get the values/indices of the selection
    + #9150 [component: docs] Use bokehjs from cdn when the commit is
    tagged
    + #9155 [component: bokehjs] [component: build] Migrate from
    tslint to (typescript-)eslint
    + #9157 [component: tests] Remove bokeh.embed.notebook.widgets
    from -oo blacklist
    + #9159 [component: build] Unpin python 3.7 version when possible
    + #9160 [component: bokehjs] Enable more eslint rules
    + #9163 [component: build] [component: examples] Don't upload to
    s3 on py27 tests
    + #9165 [component: examples] Update dataset for parallel coords
    plot examples
    + #9167 [component: bokehjs] [component: build] Generate es6
    (es2015) compatible bundles
    + #9170 [component: bokehjs] [component: build] Automatically
    insert class initialization code
    + #9173 [component: docs] [bug] "line_color" not applied from yaml
    theme file
    + #9175 [component: tests] Make bokeh's tests compatible with
    pytest >= 5
    + #9179 Add support for turbo colormap
    + #9181 [component: docs] [bug] [docs] broken images in custom
    tooltip example
    + #9183 [component: docs] Update all docs links
    + #9192 [component: docs] Pillow is already a bokeh dependency
    + #9193 [component: bokehjs] [component: build] Bump eslint-utils
    from 1.4.0 to 1.4.2 in /bokehjs
    + #9199 [component: docs] [bug] [doc] broken link to examples/app
    + #9200 [component: docs] Fix typos in docs, comments, etc
    + #9202 [feature] print full stacktrace on error
    + #9205 [component: build] Don't depend on ipywidgets
    + #9206 [component: docs] Outdated sentence removed from docs
    + #9211 [component: docs] [doc] tpyos
    + #9212 [component: bokehjs] [typescript] Upgrade to typescript
    3.6
    + #9219 [component: docs] Update layout docs
    + #9220 [component: docs] Add websource to reference docs
    + #9226 [bug] update license id to use the proper spdx short
    license id
    + #9228 Update current year
    + #9229 [component: build] Bryanv/update docs automation
    + #9237 [component: docs] [bug] hovertool indices empty when using
    glyphrenderer from a graphrenderer
    + #9239 Improve "splat" list errors
    + #9258 [component: docs] [bug] ajaxdatasource-based glyphs appear
    incompatible with factorrange
    + #9262 [component: docs] Fix structure issues in palette docs
    + #9264 [component: build] Cdn invalidations too narrow
    + #9265 [component: docs] Rename modify_doc in notebook app
    contexts
    + #9271 [component: bokehjs] Upgrade from deprecated package
    istanbul
    + #9272 [bug] improve exception when import _requires fails
    + #9274 If import of channels fails, improve error message to
    install it via pip
    + #9278 [component: docs] Consistently use https protcol for
    cdn.pydata.org urls
    + #9286 [component: docs] Fix user-guide documentation and app
    example typos
    + #9289 [component: docs] Fix broken docs links
    + #9305 [component: docs] Update ga for docs
    + #9312 [component: docs] Update references to jupyter_bokeh
    extension
    + #9340 [component: docs] 1.4.0 misc docs
* Fri Aug 16 2019 Todd R <toddrme2178@gmail.com>
- Update to 1.3.4
  + tasks:
  * [component: build] Update pypi token
- Update to 1.3.2
  + bugfixes:
  * [component: build] Compute runtime deps correctly
  + tasks:
  * [component: docs] [bug] wrong option names in sphinxext documentation
  * [component: build] Use pypi token to upload releases
  * [component: bokehjs] [component: build] Use npm token to publish
- Update to 1.3.1
  + bugfixes:
  * [component: bokehjs] [regression] [bug] export_png broken in bokeh 1.3.0
  + tasks:
  * [notebook] [widgets] Autocomplete should start with a single character
  * [component: build] Upload to backup cdn
  * [component: build] Exclude ipython tests on minimal build
* Fri Jul 26 2019 Todd R <toddrme2178@gmail.com>
- Update to version 1.3.0
  + bugfixes:
  * [component: bokehjs] [widgets] Bokeh datepicker value format inconsistent
  * [component: server] Bokeh charts load very slow with uncaught typeerror: in browser console
  * [component: bokehjs] [widgets] Rangeslider stuck when modified by pressing the keyboard arrows
  * [component: server] [bug] error in the bokeh --serve documentation
  * [component: bokehjs] [widgets] [bug] datatable copy-paste doesn't work with 0s present in a row
  * [component: bokehjs] [widgets] [bug] datatable copy-paste doesn't keep the order of rows after sorting
  * [component: bokehjs] [widgets] [bug] datepicker displayed value is not updating
  * [component: bokehjs] [performance] Inspection indices' filtering is very slow
  * [component: bokehjs] [widgets] [bug] "cannot read property 'style' of null" javascript error when moving slider
  * [component: bokehjs] [bug] typeerror after replacing tools on a toolbar
  * [component: bokehjs] [bug] incompatible definitions of `vbar.width` in bokeh and bokehjs
  * [component: docs] [bug] development guide missing `test` argument for conda install and pytest install failure on windows
  * [component: server] [bug] double slash before prefix in autoreload.js
  * Update docker to work with new conda and bokeh
  + features:
  * [component: bokehjs] [widgets] File open dialog
  * [API: models] [widgets] [feature request] option to collapse datatable rows
  * [component: bokehjs] Make a bokeh textinput callback responsive as text is typed
  * [component: bokehjs] Add hover support for patch, harea, and varea
  * [component: bokehjs] [feature] implement hover anchor on more glyphs
  * Let source.data accept dataframe
  + tasks:
  * [component: examples] Geojsondatasource not bringing in all attributes
  * [component: docs] [component: server] Document signed session usage
  * [component: docs] Texturerepetition missing from docs and `all`
  * [component: tests] Don't call show in tests
  * [component: bokehjs] [component: build] Bump nwmatcher from 1.4.3 to 1.4.4 in /bokehjs
  * [component: docs] Docs typo
  * [component: docs] Documentation: duplicate $name description
  * [component: docs] Fixed analysis
  * [component: build] [task] add downstream tests for pandas-bokeh
  * [component: build] Upload to s3 cdn in parallel
  * [component: docs] [docs] developer notes rendered in live docs
  * [component: docs] Typo/misspelling on mapping geo data page[bug]
  * [component: build] Fix yamlloadwarning in deps.py
  * Color regex needs raw string
  * Use sampledata.bokeh.org cdn
  * [component: docs] [docs] update links to bokehplots.com, gitter and mailing-list
  * [component: build] Exclude landing-2.0 issues from changelog for now
  * [component: bokehjs] [widgets] [feature] extend fileinput to return filename and make output clearer
  * [component: docs] Docs: update documentation urls in readme
  * [component: tests] Update dask test location
  * [component: build] [component: docs] Remove dev build installation instructions
* Tue May 28 2019 Todd R <toddrme2178@gmail.com>
- update to version 1.2.0
  + bugfixes:
  * [widgets] Autocomplete widget not recognizing value change
  * Boxselecttool does not work as expected with gmapplot
  * [webgl] Mixed canvas and webgl glyphs are painted in wrong z-order
  * Rangetool unusable after selection change
  * [widgets] [bug] autocompleteinput widget value attribute does not reflect selection
  * [bug] runtimeerror on adding callbacks after rendering
  * [widgets] Bar_color slider not updating
  * [bug] color mapping bug in crossfilter example
  * exports do not work with firefox webdriver
  * [bug] imageurl selection_glyph raises "typeerror: this.retries is undefined"
  * [bug] customjs callbacks added after initialization do not work
  * layout accepts name as keyword arg but doesn't pass to underlying objects
  * [widgets] [bug] changing slider widget title property does not update view
  + features:
  * [component: server] Slider callback_policy should work for apps
  * Feature request: textures to fill properties?
  * [layout] Legend title
  * [component: bokehjs] [feature] stacked areas and lines
  * allow the webdriver timeout to be customized
  + tasks:
  * [component: tests] Add missing widget callback integration tests
  * Document that boxzoomtool does not work on gmapplot
  * Touch scroll the page when no tools are active
  * [widgets]  add selenium tests for slider and rangeslider
  * Allow reset tool to only emit reset event, and skip built-in reset code
  * Document get_screenshot_as_png better
  * Clean up .gitignore files across the repository
  - #8496 "warning:bokeh.resources:root_url should end with a /, adding one" spam
  * `scripts/deps.py` does not install phantom_js
  - #8861 Create readme to explain server_embed usage
  * Update tile provider example for "mapping geo data" user guide
  * Uploading actual releases to conda bokeh/label/dev
  - #8875 Hatching/stacking follow on work
  * [component: build] Fix security vulnerabilities reported by npm audit
  - #8897 Reference link updated
  * [bug] legend order backwards for stacked area plots
  * Update 1.1.0.rst
  * Docs: fix typo
  * Add release notes for 1.2
* Mon Apr 22 2019 Todd R <toddrme2178@gmail.com>
- update to version 1.1.0
  + bugfixes:
  * [layout] [widgets] Setting responsive for figures in tabs results in buggy tabs
  * [layout] If responsive mode is `height_ar`, toolbar box `above` or `below` doesn't work
  * [layout] Tabs only work with fixed layout
  * [layout] Initialization problem on `scale_width` plots
  * [component: bokehjs] Bokehjs charts not respecting plot size
  * [layout] Figure.width does not update width
  * [layout] Strange widget alignment behavior
  * [component: bokehjs] [layout] Tabs not working
  * [component: bokehjs] [layout] [widgets] Tabs only renders right when at least one tab contains a figure
  * [layout] [widgets] Overlapping plots
  * [layout] Subplots vertical axes don't line up
  * [component: bokehjs] [layout] Widgets do not work in nested layouts
  * [component: bokehjs] [layout] 0.12.4 breaks custom text inputs field length
  * [layout] [widgets] Datatables overlapping when in row or gridplot
  * [component: bokehjs] [layout] Adding new button widgets results in too-wide buttons
  * [component: bokehjs] [widgets] Multiselect freezes ie 11 on change
  * [component: bokehjs] Javascript errors when plotting from a columndatasource populated with a pandas dataframe containing column named field
  * [component: bokehjs] [layout] Tabs widget cannot contain a figure
  * [component: bokehjs] [layout] Textinput not respecting width
  * [component: examples] [regression] Npm detection doesn't work on windows (in native console)
  * [layout] Vertical axes aren't aligned in `plotting/file/categorical`
  * [component: bokehjs] Multiple callbacks for same model call only last callback
  * [component: bokehjs] Tap tool on bokeh server does not select data points with a custom callback
  * [layout] Dynamically turning on axis label does not resize plot
  * [layout] Alignment of plots in a grid
  * [widgets] Autocompleteinput does not complete word when option is clicked
  * [component: bokehjs] [component: tests] Examples/models/file/dateaxis.py is unreliable
  * [component: bokehjs] [component: build] Incorrect module path format when building bokehjs on windows
  * [component: bokehjs] [layout] [widgets] Datatable in tab not displaying contents (with minimal example)
  * [layout] [widgets] Vertical slider
  * [component: bokehjs] [layout] Unsatisfiable constraint when trying to make plot size responsive within panels
  * [layout] Plot layout with scale_both, stretch_both, scale_height
  * [component: bokehjs] [layout] Table covers other widget when table is on the left
  * [component: bokehjs] [layout] Gridplot with sizing_mode="stretch_both"/"scale_both" is totally broken since 0.12.11
  * [component: bokehjs] Disappearing toolbar
  * [component: bokehjs] [layout] Bokeh layout rows and columns not responsive on scale_width or scale_height
  * [component: bokehjs] [layout] Row and column definition gives unexpected layout with option sizing_mode='scale_width'
  * [layout] Repaint() in plot_canvas.coffee causing significant lag
  * [component: bokehjs] [layout] Bokeh spacer sets height to one pixel with scale_width set
  * [component: bokehjs] Different behavior between bokeh and bokehjs with ajaxdatasource
  * [component: bokehjs] [widgets] Checkboxbuttongroup and radiobuttongroup can not be disabled
  * [component: bokehjs] Hovertool display pops under shaded portion of slider
  * [layout] [regression] Stretch_both sizing mode doesn't stretch in 0.13
  * [component: bokehjs] Tilerenderer cache is not invalidated when url changes
  * [performance] Improve datatable performance
  * [component: bokehjs] The "css_classes" attribute on datatable object does not work
  * Compiler issue on windows, importing modules is not working because of backslash incompatibility
  * [component: bokehjs] "tile cannot extend" systemerror when exporting plot with legend placed outside and above plot area
  * [layout] Button groups do not respect the `sizing_mode` or `width` keyword arguments
  * [component: bokehjs] [widgets] Updating css_classes on layout elements has no effect
  * Whisker does not accept explicit negative values
  * [component: bokehjs] Wrong position on catergoricalaxis of extra_y_range
  * Typeerror: index is not a valid datetimeindex or periodindex
  * [component: bokehjs] [typescript] Bokehjs examples to use in node js or angular
  * [component: bokehjs] Grid bands broken when cross grid lines disabled
  * [component: bokehjs] Cds callback property not working
  * [component: bokehjs] [layout] Bug when the middle area between two tabs is clicked
  * Inline ts code failed at compilation on windows (post #8085)
  * [layout] Layout broken in hidden tabs after an update
  * [layout] [regression] Input widget heights behavior
  * [component: bokehjs] Crosshair icon removed from toolbar in gridplots
  * [component: server] Issue with bokeh.client after layout pr
  * [component: examples] Stocks example is not working properly
  * [component: docs] [layout] Incorrect layout with column of div's with image (1.1.0dev3)
  * [widgets] Datatable rows overwrite dropdown menu (1.1.0dev3)
  * [layout] [regression] Dashboard.py example not behaving as expected after the layout pr
  * [component: tests] Make examples' tests work on windows
  * [component: examples] Grid_axis_alignment_no_toolbar is broken in windows (32-bit)
  * [widgets] Assume utc in value_as_date
  * [layout] Text wrapping in div after layout pr
  * [layout] Loading plot in separate jupyterlab tab collapses layout
  * [component: bokehjs] Graphs with list values as attributes fail
  * [component: examples] [regression] Custom widget in doc strange display in 1.1.0dev6
  * [notebook] Autoload_js should load css before javascript
  * [component: bokehjs] [component: docs] Bokehjs columndatasource.change property doesn't exist
  * [component: docs] Typo in plots.py
  * [notebook] [regression] Displaying plot in notebook quickly after output_notebook raises js error
  * [component: tests] Tests sometimes fail on appveyor
  * [layout] Tabs width set on width of contents - truncating tabs
  * [component: bokehjs] [notebook] [regression] Gmap plots not working in the notebook and inline resources
  * Windows phantomjs not killed on selenium termination
  * [component: bokehjs] Hover tooltip breaks with zero-width wedges
  * [component: bokehjs] When line_width is set to 0 the glyph boundaries don't disappear
  * [component: bokehjs] Custom extensions cannot import models/widgets/widget
  * [component: bokehjs] Tooltips not working for segment on inverted y-axis
  * [component: bokehjs] Using range padding with image plots leave lots of empty space
  * [component: bokehjs] [layout] Tabs header doesn't update when layout recomputes
  * [component: bokehjs] Spinner jumps to low after one click, regardless of step
  * [component: tests] Codebase tests fail on windows
  * [component: bokehjs] Range tool gets stuck at minimum width
  * [component: server] Directoryhandler does not handle ipynb files correctly
  * Fixes trying to index dict_keys
  * [component: bokehjs] [regression] Es6 map's polyfill isn't installed in phantomjs
  * [component: bokehjs] Surface3d example fails to compile
  * [component: bokehjs] [layout] Make layout respect aspect ratio with scale_height sizing mode
  + features:
  * [layout] Non-equal proportion split in layouts
  * [layout] Don't make space for element if not visible
  * [component: docs] Sphinx bokeh_plot extension should work outside project docs
  * [component: bokehjs] [widgets] Add numeric input widget
  * [component: bokehjs] Bokeh panel(closable=true) doesn't make 'x' appear on the panel title and closable by user
  * [component: bokehjs] [widgets] Add color picker and spinbox widgets
  * [layout] Add sizing_mode="stretch_width" and "stretch_height"
  * Add js_link convenience method
  * [component: server] Add --index option to specify site index template
  * [API: models] Add support for data source using server-sent events
  * [component: bokehjs] Displaying custom data on hover for rgba image
  * [API: models] Openurl in current tab
  * [component: bokehjs] Make bokehjs importable in nodejs
  * [layout] [regression] Add support for spans to grid layout
  + tasks:
  * [component: bokehjs] [layout] Investigate better implementation for toolbar rendering
  * [layout] Investigate / describe performance issues
  * [component: tests] [layout] Add a series of screenshot tests for all the layout modes
  * [layout] Stop doing two calls to _resize on every resize
  * [API: models] [component: bokehjs] Widgets with js api
  * [component: bokehjs] [layout] Use box-sizing: border-box for everything under bk-root
  * [layout] [performance] Browser rendering extremely slow when many figures in a gridplot
  * [component: examples] Make simple_hdf example interesting and attractive
  * [component: bokehjs] Add a link to bokehjs package on npmjs.com
  * [API: models] [layout] Add visible property to models
  * [component: tests] Task: fix-up skipped app examples for examples tests
  * [layout] Unify meaning of {layoutcanvas,layoutdom}.{_left,_top,_right,_bottom}
  * [API: plotting] [component: bokehjs] Bokehjs typeerror "legend is undefined"
  * [component: bokehjs] [typescript] Rewrite bokehjs' tests in typescript
  * [component: bokehjs] [typescript] Remove unnecessary usage of any type
  * Make error reporting from `export_png()` more robust
  * [layout] Improve reliability, performance and feature coverage of the layout
  * [regression] Do not include large unrelated files in the repository
  * [component: bokehjs] [component: build] Relativize module paths in generated js/d.ts files
  * [component: docs] Autoreloader cannot find bokeh on reload
  * Tile provider causes "model must be owned by only a single document" error
  * [component: server] Delay between autoload.js and websocket request
  * [component: examples] Create custom example to plot parallel plot
  * Make websocket_max_message_size configurable in notebooks
  * [component: build] Pin conda versions with conda_reqs on appveyor too
  * [component: docs] [docs] bad number in webpage patch method documentation
  * [component: docs] Change use of deprecated sphinx app logger
  * Importing abcs from collections is deprecated
  * [component: bokehjs] [typescript] Remove type duplication between models' attributes and properties
  * [typescript] Finalize typing plotting api and remove old declarations
  * [component: tests] Fix pytest's deprecations in examples' tests
  * [component: bokehjs] [typescript] Upgrade typescript and minifier, and enable more tslint rules
  * [notebook] Use utf-8 encoding to open notebook file
  * Daterangeslider returns datetime instead of date
  * [component: examples] Manual_grid layout example has lost it's core functionality in layout pr
  * [component: bokehjs] [typescript] Rewrite custom extensions in typescript
  * [component: build] Use ci.bokeh.org for artifact storage
  * [component: docs] Bryanv/demosite url
  * [component: docs] Add live codepen links for bokehjs api
  * [component: bokehjs] [component: build] Rename bokehjs/build/js/{tree->lib} to match src/
  * [component: bokehjs] [component: build] Handlebars security vulnerability - npm won't install
  * [API: models] Deprecate plot.{h,v}_symmetry
  * [component: bokehjs] Disabled buttons should be gray by default
  * Bad_extra_range_name validation can be incorrect
  * [layout] Don't warn on empty layouts
  * [component: bokehjs] Miscellaneous improvements to bokehjs
  * [component: bokehjs] Don't expose external libraries in the public api
  * [BEP] [component: build] Update maintainers list
  * [component: docs] Updated numfocus donor link
  * [component: bokehjs] [component: build] Upgrade to typescript 3.4
  * [component: docs] Corrected spelling mistakes
  * [layout] Make gridbox.spacing adhere to css argument order
* Sun Jan 20 2019 Arun Persaud <arun@gmx.de>
- update to version 1.0.4:
  * bugfixes:
    + #8558 [py2] Safer alternative fix for unicode notebook issue in
    python 2
  * features:
    + #8513 [notebook] Strip out ipython magics when serving notebooks
  * tasks:
    + #8207 Adding/updating boilerplate code
    + #8525 [component: tests] Don't resize window when running images
    tests
    + #8533 [component: build] Remove warning about `gulp build` in
    prepare.js
    + #8534 [component: docs] Docs tweak to add note about bokeh_dev
    and apps
    + #8541 Pyyaml version is vulnerable to cve-2017-18342
    + #8543 [component: server] Bad error message for nonexistent
    bokeh serve target
    + #8548 [component: docs] Add small documentation to slider
    callback_policy which only apply to customjs
    + #8550 [component: docs] Fix-up bokeh_dev docs (follow-up)
    + #8553 Add model, event, and populate bokeh.models __all__
    + #8555 [py2] Unicode fix when serving notebooks on python 2
    + #8556 [component: docs] Correct three minor typos
* Sun Jan  6 2019 Arun Persaud <arun@gmx.de>
- specfile:
  * update copyright year
- update to version 1.0.3:
  * bugfixes:
    + #7118 [component: bokehjs] Unable to update arrow
    + #8401 [API: models] Incorrect image import from bokeh.models
    + #8493 [component: bokehjs] Polydrawtool shows vertices even when
    not active
  * features:
    + #2828 [component: bokehjs] [widgets] Multi-line textinput box?
    + #7762 [component: bokehjs] Copy & paste from datatable
    + #8444 [component: bokehjs] Feature request: expose sort_columns
    in js datatable object
    + #8502 Support environment variable in addition to
  - -allow-websocket-origin
  * tasks:
    + #8372 Extended bad_column_name error
    + #8379 [component: examples] Export csv example more useful if
    you don't have to hard code headers in download.js
    + #8383 [component: tests] Attempt to enable downstream tests for
    holoviews
    + #8384 [component: bokehjs] Feature: add plot's root id to dom so
    to allow api access to the object
    + #8472 Boilerplates for bokeh/models
    + #8476 [component: bokehjs] [typescript] Upgrade to typescript
    3.2
    + #8481 [component: docs] Doc: remove extra "to execute" from
    embed
    + #8485 Update sampledata bucket url
    + #8491 [component: docs] Typo in range_tool example
    + #8495 [component: tests] Document licenses of included projects
    + #8506 Boilerplate for bokeh/plotting directory
    + #8514 Boilerplate for protocol
    + #8517 Boilerplate for bokeh/server
    + #8523 Property getter for model.id
    + #8528 [component: docs] Release notes
* Sat Dec  1 2018 Arun Persaud <arun@gmx.de>
- update to version 1.0.2:
  * bugfixes:
    + #5721 [component: bokehjs] [widgets] Text_align attribute in
    numberformatter not doing anything
    + #8395 [component: bokehjs] Legend breaks plot when plotting
    empty scatter glyph
    + #8396 [component: docs] Fix small typo [ci skip]
    + #8398 Fix typo and grammar mistakes
    + #8409 [component: docs] Typo in documentation of
    io.export.create_webdriver
    + #8415 Make components() preserve the type of dict
    + #8418 [component: bokehjs] [component: build] Make bokehjs build
    under node 10.x
    + #8425 [component: docs] Apache documentation typo
    + #8428 [component: bokehjs] [component: docs] Can't get gridplot
    to work in bokehjs
    + #8451 [component: bokehjs] [component: build] Run `npm install`
    when `node make *` on fresh install
    + #8457 [component: bokehjs] Embeds with json_item missing
    toolbar/interactivity
    + #8459 [component: bokehjs] Hovertool does not display fields
    within jupyterlab's dark theme
    + #8460 [component: examples] Fix a typo
  * features:
    + #8399 [component: bokehjs] Omit colon in hover tooltips if first
    tuple entry is empty
    + #8411 [widgets] Feature request: add support for setting the
    datatable row height
  * tasks:
    + #8393 [component: docs] "customjs for selections" example in
    docs broken
    + #8405 [component: tests] Fix failing codebase tests
    + #8413 [component: bokehjs] [typescript] Upgrade to typescript
    3.1
    + #8438 [component: bokehjs] [typescript] Clean up semicolons
    after transition to typescript
* Thu Nov  1 2018 Arun Persaud <arun@gmx.de>
- specfile:
  * removed devel from noarch
- update to version 1.0.1:
  * bugfixes:
    + #4096 Bokeh server: color palette rgb is not recognized
    + #8356 [component: bokehjs] Datatable crashes layout if 'field'
    is key in columndatasource data
    + #8362 Combination of "export_png()" and "show()" causes error
    + #8374 [regression] Garbage collection of export_png()
    + #8375 [component: bokehjs] Ellipse and datetime axis
    + #8388 [component: build] Release deploy updates package-lock
    incorrectly
  * tasks:
    + #8367 [component: server] Documentlifecyclehandler should catch
    exception and clean up callbacks
    + #8369 [component: examples] Histogram example should take edges
    as argument to make_plot
    + #8387 [component: docs] Bryanv/101 misc docs
* Tue Oct 30 2018 Todd R <toddrme2178@gmail.com>
- flexx is no longer used.
* Fri Oct 26 2018 Todd R <toddrme2178@gmail.com>
- Update to version 1.0.0
  + bugfixes:
  * [component: bokehjs] Not correct behaviour of hovertool with annular glyph and units='screen'
  * [component: bokehjs] [component: examples] Plotting/file/image_url.py doesn't work without setting {x,y}_range
  * [component: bokehjs] [widgets] Patch/stream message to the columndatasource for datatable widget on front-end triggers response containing entire data source
  * [component: bokehjs] [geo] Flicker when zooming on a tile source with mercatorticker
  * [component: bokehjs] [regression] Deserializationerror when editing data table
  * [component: server] 'serversession' object has no attribute 'session_context'
  * [component: bokehjs] Image hover broken on axes with inverted range
  * [component: bokehjs] [geo] Segments don't show up on gmapplot
  * [component: bokehjs] Log axis minor ticks wrong position
  * If the "selector" argument is explicitily set to the "select" method, an empty list is returned
  * [regression] Export_png not exporting figures correctly
  * [component: bokehjs] [widgets] Datatable and glyph selections not linking properly
  * [component: bokehjs] Draw and edit tools event handling on server broken
  * [component: server] Unhandled exception in application causes all later sessions to fail
  * [component: bokehjs] [widgets] Editing filtered datatable cell impacts wrong row
  * [component: bokehjs] [widgets] Datatable selectable='checkbox' gives javascript error
  * [component: bokehjs] Inaccurate rendering around 0 on tall bars
  * [component: bokehjs] Boxedittool draws on doubletap even when tool inactive
  * [component: bokehjs] Not providing x and y data makes some glyphs not render in legend
  * [component: bokehjs] [notebook] Bug: push_notebook support is broken in jupyterlab for bokeh=0.13.0
  * Bokeh_css and bokeh_js resources are reversed in file.html template
  * [regression] Show() accumulates objects
  * [component: bokehjs] Hovertool interpolation mode doesn't work for horizontal and vertical lines
  * [widgets] Datatable does not stay sorted when the data is updated
  * [py2] Properly use string_types for instance properties and js_on_event
  * Patch_app.py is broken
  * [component: bokehjs] Adding computed_icon getter broke toolproxy icons
  * [component: bokehjs] [regression] Esc has no effect on selections
  * [component: docs] A tiny typo in the document about graphrenderer
  * [component: tests] Verify_all() doesn't give information what failed
  * [component: bokehjs] Y-range for negative value
  + features:
  * making predefined themes available by calling a single function
  * [component: bokehjs] Update legend when legends or other attributes change
  * Pandas periods are not recognised
  * [component: bokehjs] [geo] Support a "patch" with a hole in it / gis support
  * [component: server] Implement --develop mode
  * [component: bokehjs] Save bokeh plot as bokeh plot
  * Custom models distribution without compiler on the server side
  * [component: bokehjs] Let scatter marker type be parameterizable
  * [component: bokehjs] [widgets] Add an option to disable column titles in datatable
  * [component: bokehjs] Oval selection does not update color (does not support hit testing)
  * [API: models] Allow defining custom tooltip for certain tools
  * [component: bokehjs] Feature request: support hit-testing for text glyphs
  * [component: bokehjs] Step glyph support for gaps from missing/non-finite data points (inf, nan)
  * [component: bokehjs] Restrict the drawing tools to draw a single glyph
  * [component: bokehjs] Add clear tool to clear out one or more datasources
  * [component: bokehjs] Expose the more detailed geometry data to the tap tool
  * [component: bokehjs] Feature request: verticalline marker (equivalent to marker='|' in matplotlib)
  * [component: bokehjs] Add tilt option to gmapoptions
  * [component: bokehjs] [typescript] Freehand drawing tool
  * Turn off self.validate checks during update
  * Span location cannot accept datetime whereas labels can deal with it
  * [component: bokehjs] Feature request: bold italic font specification
  * [component: bokehjs] Make image smoothing configurable on tilerenderer
  * [feature request] in the function ‘from_networkx’, convert networkx node/edge attributes to bokeh node_renderer/edge_renderer data_source
  * [feature request] add .copy method to columndatasource
  * Add another theme: balanced
  * [component: bokehjs] Support specifying representative point from legend items
  * [component: server] Allow defining session cleanup hooks on a document
  * [component: bokehjs] Autohide toolbar
  * [component: bokehjs] Fixedticker does not accept minor ticks
  * [feature request] ‘from_networkx’ function for a fixed layout
  * [component: bokehjs] [component: examples] Add adapter property to ajaxdatasource
  * Add webdriver_control and default to reuse
  + tasks:
  * Feature idea: docker image for bokeh server
  * [component: tests] Ci test to make sure bokeh works without heavy dependencies
  * should issue a validation warning when the range values are not unique
  * Valueerror: nattype does not support timetuple
  * [component: bokehjs] No way to cleanup used memory
  * [API: models] It is not possible to set a range1d with datetime.timedelta value
  * [component: bokehjs] Warn on setting empty plot.legend attrs
  * Add missing ticker tests and minor ticker improvements
  * Customize warning formatter
  * Task: pytest marked "selenium" tests should assert no browser console errors
  * Task: add/use selenium fixture in ``export`` tests instead of creating new phantomjs processes
  * Task: add user warn/error to columndatasource.from_df method about dataframe containing "index" column
  * [component: docs] User guide, tweak to "ranges" doc
  * [API: models] Document validation check needed for mis-matched y_range_name
  * [component: bokehjs] [component: server] Pull_session with url paramters isn't working
  * [widgets] Daterangeslider error not logged nor shown in cli
  * [component: docs] Added short usage instructions for examples/app/dash
  * [component: docs] Doc typo (funtion -> function)
  * Improved support for pyinstaller
  * Remove code dependent on ipython pprint machinery
  * Overzealous deduplication of tools for merge_tools
  * [component: tests] Clean up test support
  * [component: docs] Simplify pie example
  * [component: build] Ci scripts with colon in filenames are not valid on windows
  * [component: tests] Bryanv/test cleanup
  * Use generators instead of lists
  * [component: docs] Backticks are broken un docs/*.rst
  * [component: examples] Box_annotation example .ix method is deprecated
  * [component: examples] Ref: use .loc instead of .ix in examples
  * [component: docs] Update documentation for how to use bokeh server with jupyterhub environment
  * [component: tests] Fixed exception raising tests of test_sources
  * [component: examples] Rename joyplots to ridgeplots
  * [component: docs] Docstrings not clear for dimension property for band, span and whisker class
  * [component: server] Bokeh doesn't work with tornado master
  * [component: tests] Initial work to support server selenium tests
  * Remove the arguments parameter from server_session
  * [component: tests] Unit tests failing in windows 7
  * [component: examples] Pandas > 0.23.0 & < 0.23.4 breaks boxplot.py example
  * [component: examples] Issues: none type: bug tag: examples updated main.py
  * [component: tests] Bryanv/misc cleanup
  * [component: docs] Installation docs: need info about export_png/svgs
  * [component: build] [component: tests] Added unit/integration tests for python3.7
  * [component: build] Don't report unversioned python in deps.py output
  * [component: tests] Python 3.7 get_referrers change
  * Remove dead testing code
  * Use np.frombuffer instead of deprecated np.fromstring
  * [component: build] Appveyor build and test for windows
  * [API: models] Plot.{x,y}_range default value
  * [component: docs] Some typo in the guide
  * [component: build] Update requests min version
  * Pandas is optional overall, but required for hexbin
  * [component: build] Refine appveyor.yml settings
  * [component: examples] Example examples/embed/server_session/ is broken, template is missing
  * Add note of  bokeh_phantomjs_path environment variable on missing phantomjs
  * [component: bokehjs] Missing ";" in try_run.js
  * Unhelpful error when passing invalid argument to gridplot
  * [component: docs] [document] add (or update) an example to demonstrate  converting node/edge attributes in from_networkx
  * Split up bokeh.properties
  * [component: docs] Re-unify docs build
  * [component: build] Small build tasks
  * [BEP] Ratify project roles document
  * Bryanv/reduce import code
  * [component: examples] Examples punch list
  * [component: examples] Pandas warning removed in gapminder example
  * [component: examples] Correction selection histogram example
  * [component: examples] Population example legend position -> "bottom_right"
  * Load themes from python modules instead of json files
  * [component: examples] Simple hdf5 example improvement
  * Replace log.warn with log.warning
  * [component: examples] Embed_multiple: better arrangement
  * Boilerplate for bokeh/core
  * [component: docs] Chaco link is a 404 - changed to git repo url
  * Confusing multi_line error message
* Sun Jul  1 2018 arun@gmx.de
- update to version 0.13.0:
  * bugfixes:
    + #799 Templates not included when compiling with py2exe
    + #2080 [component: bokehjs] Hovertool panel for annular wedge
    displays at center coordinates, not over wedge
    + #7428 [component: bokehjs] Correctly showing wedge hover
    tooltips with "clock" orient
    + #7591 [component: bokehjs] [layout] Adding a slider fails to
    load visualization in version 0.12.14
    + #7891 [component: bokehjs] [regression] [widgets] Unable to edit
    datatable cell
    + #7904 [component: examples] Flask_gunicorn_embed.py does not
    work with tornado 5
    + #7916 [component: tests] Code quality tests fail due to pandas'
    regression
    + #7924 [component: bokehjs] [regression] [widgets] Sorting linked
    datatables messed up in bokeh 0.12.16
    + #7926 [component: bokehjs] [widgets] Setting value of
    multiselect in javascript doesn't unselect previous selected
    items
    + #7935 Using on_event with string names in python2.7
    + #7941 [component: docs] Update docs: the hovertool attribute is
    "formatters"
    + #7978 [component: bokehjs] [layout] Sizing mode scale_both grows
    on window resize
    + #7984 [component: bokehjs] [layout] Temp partial fix allowing
    scale_both to work in some cases
    + #7992 [component: server] [memory] Memory leak on
    add_next_tick_callback
    + #8000 [component: docs] Small documentation error for
    boxselecttool
  * features:
    + #3596 Warn about python callbacks when they won't run
    + #4986 [layout] Allow elements to be placed in server templates
    + #6320 [component: bokehjs] Expose initial_start and initial_end
    in range1d
    + #6386 [component: bokehjs] Support line annotations like span
    but with slope
    + #7401 Support passing a pandas.series as x_range for figure
    + #7795 [component: bokehjs] Feature-request: selection-bar
    + #7908 [API: models] Tile source attribution font size
    + #7921 [component: bokehjs] Bryanv/usability
    + #7961 [component: bokehjs] Add a cumsum transform to
    cumulatively sum a single column
  * tasks:
    + #7364 [component: docs] Developing with javascript jsfiddle not
    working in firefox 57.0.3 (macos 10.13.2)
    + #7374 [component: server] Connection errors when sending large
    amounts of data to browser via a bokeh server
    + #7831 [component: docs] Improve documentation for creating
    interactive plots in notebook
    + #7880 [component: bokehjs] [component: build] Upgrade npm
    packages
    + #7905 [component: docs] All gallery examples bundle unnecessary
    extension code
    + #7911 [component: bokehjs] [component: tests] Make bokehjs' unit
    tests more robust
    + #7915 [component: bokehjs] Re-jitter on tap is unexpected
    + #7919 [component: bokehjs] [component: build] Replace gulp with
    a more lightweight solution
    + #7922 [component: build] Move bokeh build and ci to new
    rackspace account
    + #7930 [component: docs] [typescript] Docs still say that
    coffeescript is the implementation language of bokehjs
    + #7936 [component: bokehjs] Resettool doesn't restore initial
    plot when using wmtstilesource and x/y_range
    + #7937 [component: bokehjs] Add support in tablewidget for
    ajaxdatasource
    + #7946 [typescript] Upgrade to typescript 2.9
    + #7950 [component: build] Bryanv/build cleanup
    + #7951 [component: bokehjs] Line plots jaggy when overplotting
    noisy data with `line_join='miter'`
    + #7953 [component: bokehjs] Modifying data source while polydraw
    is editing breaks editing
    + #7957 [component: bokehjs] [component: build] Replace esprima
    with typescript compiler api
    + #7962 [component: bokehjs] [component: build] Run `npm install`
    automatically if package.json changed
    + #7967 [component: docs] Typo in the image_url documentation
    + #7973 Add new maintainer to the list
    + #7977 [performance] High (probably unnecessary) cpu load due to
    is_valid calls
    + #7985 [API: plotting] Bokeh gmapoptions error
    + #7993 [layout] Improve computing of available space for
    responsive layouts
    + #7995 [component: docs] Documentation of cmap functions
    + #8003 [component: docs] [notebook] Updated docs for two-way
    jupyter communication
* Tue May 15 2018 arun@gmx.de
- update to version 0.12.16:
  * bugfixes:
    + #3556 [component: server] Add a server callback once and then
    again as periodic
    + #4298 [component: bokehjs] Ajaxdatasource data initialization
    + #6303 [component: bokehjs] Bokeh.io.export captures screenshot
    before asynchronously loaded models
    + #6698 [component: bokehjs] Bands wrongly coloured
    + #6699 [component: server] Server logger (format, output, etc)
    does not work
    + #7011 [API: models] Error message in notebook when running
    explicit path graph example from user guide
    + #7349 [component: bokehjs] [widgets] Arrow keys don't work if
    the step of slider is very small
    + #7462 [component: bokehjs] Multi_line does not work with
    categorical plots
    + #7476 [component: bokehjs] Plotcanvasview#build_levels removes
    only glyphs when renderers change
    + #7597 [widgets] Bug: datatable view doesn't rerender on
    table.source.change.emit()
    + #7621 `save` creates non-working files when used with widgets
    + #7627 [component: bokehjs] [regression] Selected points get lost
    with tap tool
    + #7705 [component: bokehjs] [regression] "typeerror: cannot read
    property 'is_empty' of null" when using hovertool
    + #7724 [component: bokehjs] [component: server] Plots not
    reacting to sliders inside flask
    + #7736 [component: bokehjs] [regression] [widgets] Editable
    datatable freezes when a cell is edited
    + #7744 [component: docs] Docs - json prototype does not expand
    + #7745 [component: bokehjs] [component: server] Pointdrawtool :
    no python side update of the data source
    + #7761 Permission denied error when invoking export_png() or
    export_svgs from inside jupyter notebook
    + #7783 [component: bokehjs] The child property of panel can't be
    a widget
    + #7790 [component: bokehjs] [regression] [typescript]
    Plotcanvas.save() is missing break statements
    + #7801 [component: bokehjs] [regression] Bokeh 0.12.15 throws
    typeerror on touch devices when dragging
    + #7803 [component: tests] Py.test -m unit doesn't run
    pytest.mark.parametrize tests
    + #7807 [component: examples] [regression] Allow customjs args to
    accept basic python types
    + #7819 [component: bokehjs] [performance] [regression] Rendering
    occurs on mouse move when hover tools is enabled
    + #7836 [component: docs] Minor fix in docs
    + #7840 [component: docs] Html formatter has a small typo
    + #7849 [component: examples] Ionrangeslider example fails when
    adding more than one slider
    + #7868 [component: bokehjs] [geo] The plot disappears when the
    max_zoom value of wmtstilesource is set and this value is
    reached
    + #7885 [regression] Exporting datatable to png broken
    + #7886 [py3] Detect_phantomjs() is broken on py3 when phantomjs
    is not available
  * features:
    + #113 [layout] Axis should have option to have a fixed
    orientation
    + #2427 [component: bokehjs] Make axis wheel zoom configurable
    + #3125 Expose the wheel zoom speed in python
    + #3126 [component: bokehjs] Add box zoom out tool
    + #3442 `boxselecttool` should accept renderers = none
    + #3886 Feature request: add hover inspection image glyphs
    + #4286 [component: docs] Provide examples of using
    remotesource/ajaxdatasource in the docs
    + #5071 [component: bokehjs] Add a method to "reset" a figure
    + #7582 [component: bokehjs] [performance] Consider replacing
    rbush spatial index with flatbush
    + #7643 [API: models] [component: bokehjs] Option to rotate
    additional categorical ticks
    + #7647 [component: bokehjs] Allow custom formatter when using the
    hover tool
    + #7725 [component: examples] Increase `size` and `color` options
    for crossfilter example
  * tasks:
    + #3903 [component: tests] Clean-up jupyter custom.js after
    running examples
    + #4915 [component: docs] [widgets] Default value in dropdown menu
    is stuck on none
    + #4923 Add a type check to `show` for better error reporting
    + #5911 [component: docs] Move off eoled google site search
    + #6175 [component: server] Some clients send bad pong, lower log
    level to reduce noise
    + #6193 [component: docs] Make bokeh_plot work in sphinx by
    default without google_api_key
    + #6240 [component: tests] Fail gracefully when pr is submitted
    from a fork
    + #6306 [component: bokehjs] Allow strict mode for cutomjs,
    etc. written in pure js
    + #6341 [component: server] Add parameter to autoload_server to
    control loading of js/css resources
    + #6657 Task: make columndatasource.column_names attribute a
    property method
    + #7080 [component: docs] [component: server] [notebook]
    Notebook_url="*" fails in show()
    + #7510 'export_png' from bokeh.io triggers 'deprecated' warning
    from selenium using phantomjs
    + #7576 [component: build] Use pscript instead of flexx.pyscript
    + #7715 [component: docs] All release notes on one webpage
    + #7720 [component: build] [component: tests] Add "downstream" ci
    build
    + #7723 [component: build] Markdown description for pypi
    + #7729 [component: build] Update of ipython to 6.3.0 breaks unit
    tests
    + #7734 [component: build] Remove pytest-rerunfailures from ci
    tests
    + #7741 [component: build] Svg export test occasionally fails on
    travis
    + #7750 [component: bokehjs] [component: tests] Investigate output
    from test_defaults
    + #7751 [component: bokehjs] [component: build] [typescript] Keep
    all custom declarations (d.ts) in external/
    + #7753 Revert "don't use --rerun"
    + #7759 [component: tests] Move outstanding static integration
    tests to examples/integration
    + #7765 [component: examples] Added 'pan' to the hexbin example
    + #7774 Make api decorators more debugging friendly
    + #7777 [component: tests] [py3] Switch python versions between
    full and partial examples' travis ci jobs
    + #7778 Remove all deprecations before 0.12.15
    + #7781 [component: docs] Missing docstring for
    get_screenshot_as_png
    + #7786 [component: bokehjs] [component: build] Rename
    bokehjs/src/coffee
    + #7797 [component: docs] Missing documentation of `--show` option
    for command line `bokeh serve`
    + #7800 [component: docs] Add relative path option and handling to
    sphinx ext
    + #7802 Findable and tunable html error boxes please
    + #7814 [component: examples] Surface3d example color fixed to z
    axis
    + #7821 Revert "set a data source's inspected taking multiple
    renderers into account"
    + #7823 [component: bokehjs] Stacked bars failing to update on
    patch
    + #7829 [component: build] Update for npm 6
    + #7835 [component: docs] Jupyter notebooks need to be "trusted"
    for saved js to render without re-executing cells
    + #7841 [component: bokehjs] [component: build] Drop dependency on
    webpack
    + #7854 [component: docs] Dependency collision: nodejs>=8.8,<9.0
    and npm >=6.0 <7.0
    + #7855 [component: docs] Added how-to set up conda environment
    using fish shell
    + #7858 Use full year for ticks in default month-year scale
    + #7860 [component: docs] Update docstring for on_change
    + #7878 Add new mpl cividis palette
    + #7879 [component: bokehjs] [component: build] Resolve reported
    npm issues
    + #7896 [component: docs] Typos
    + #7897 [component: build] [component: tests] Additional
    dependencies for unit tests
    + #7898 [component: docs] Unit tests require missing sampledata:
    airports.csv
* Tue Apr 10 2018 jengelh@inai.de
- Ensure neutrailty and relevance of description.
* Sun Apr  1 2018 arun@gmx.de
- update to version 0.12.15:
  * bugfixes:
    + #6525 [component: tests] Py.test bokeh/tests/test_io.py doesn't
    kill phantomjs precesses
    + #6787 [component: bokehjs] Svg output bleeds past axis
    + #6867 [webgl] Rect shape gets out of figure when panned or
    zoomed with webgl
    + #6871 [component: examples]
    Examples/howto/{js_events,events_app} contain bad css
    + #7054 [component: bokehjs] [component: examples] Line_select.py
    broken again
    + #7087 [webgl] Log scale graph will be blank if output_backend is
    webgl
    + #7168 Webdriverexception when using export_png
    + #7211 [webgl] Webgl incorrect clipping, 0.12.11 onwards
    + #7219 [component: server] Tornado next tick callback issue
    + #7416 [component: bokehjs] Excess text when multi_line hover
    hits two or more lines
    + #7468 [component: server] Increasing memory consumption of bokeh
    server
    + #7508 [component: docs] Fix typo in docs
    + #7515 [component: bokehjs] Bokeh 0.12.14 doesn't highlight
    initially selected options in multiselect widget
    + #7518 [component: bokehjs] [regression] Is ajaxdatasource losing
    the endpoint?
    + #7523 Out of range float values are not json compliant with
    numpy arrays
    + #7537 Export_png does not clean up temporary files before exit
    + #7538 [component: bokehjs] [regression] Adding a title to layout
    removes toolbar from top of plot
    + #7546 [component: bokehjs] [performance] Stream_to_column()
    doesn't implement rollover properly
    + #7562 [component: bokehjs] [widgets] Checkboxbuttongroup active
    list broken in 0.12.14
    + #7587 [regression] Regression streaming datetime columns
    + #7608 [component: docs] Fix typo in docstring
    + #7614 [component: examples] Fix io_loop paramenter in
    examples/howto/server_embed/flask_embed.py
    + #7619 [component: server] Issue with rapid page reloads with
    tornado 5
    + #7622 [component: bokehjs] [widgets] Slider violates start and
    end when using keyboard navigation
    + #7624 [component: docs] Doc: bug: fix user guide docs on embed -
    link schema typo
    + #7645 [component: bokehjs] [layout] Sizing_mode='scale_width'
    makes plot 1 or 2 pixels too wide in notebook
    + #7652 [regression] Regression when plotting images with
    non-binary array types
    + #7681 [regression] [webgl] Webgl initialization broken after pr
    [#7637]
    + #7688 [component: bokehjs] [geo] [regression] Gmapplot not
    rendering
  * features:
    + #2507 [component: bokehjs] Have grid that respects bounds of
    axis
    + #4786 [component: bokehjs] Add a hex tiling glyph
    + #7466 [component: server] [notebook] Notebook_embed.ipynb works
    locally but not remotely via ssh tunnel
    + #7563 [component: bokehjs] Functickformatter option to receive
    all ticks at once
    + #7566 [notebook] Add support for push_notebook in jupyterlab
    + #7600 [component: bokehjs] Global alpha for image_rgba plot
    + #7638 [component: bokehjs] Add a hex scatter marker
    + #7642 [API: plotting] [component: bokehjs] Add mercatoraxis
    class
    + #7685 [component: server] [notebook] Bokeh server compatibility
    with running behind jupyterhub
  * tasks:
    + #2644 [component: docs] Enable image diff testing for user's
    guide source example
    + #3723 [component: tests] Write unittest for ajaxdatasource
    + #5386 [BEP] Clean up beps and migrate to google docs
    + #6481 [typescript] Rewrite bokehjs in typescript
    + #6562 [component: server] Propagate settings to tornado
    application from bokeh server
    + #6594 [component: bokehjs] Add support for headless
    chrome/chromium for image diff tests
    + #6845 [component: bokehjs] Make .selected a proper bokeh model
    + #7125 [notebook] Only first plot in jupyter notebook cell is
    shown
    + #7474 Alpha not working on images
    + #7483 [component: build] [component: server] Add tornado 5 to ci
    testing
    + #7492 In a stacked bar chart there is no way to add tolltips for
    segments in column
    + #7494 [component: build] Specify compilation inputs in
    tsconfig.json
    + #7495 [component: build] [typescript] Upgrade typescript to
    version 2.7.1
    + #7502 [component: build] Resolve compilation errors around
    number.isinteger
    + #7505 [component: docs] Sphinx bokeh extension script directory
    sorting
    + #7509 [component: build] Remove pytest-catchlog dependency
    + #7513 [component: bokehjs] [component: build] Check if
    package.json changed before proceeding with build
    + #7516 [component: docs] [component: examples] Update examples
    and add documentation for selection model
    + #7520 [component: docs] Bokeh-plot directive incomptable with
    sphinx 1.7
    + #7522 [component: docs] Fix typo
    + #7526 Jsonencoder warning when using latest numpy
    + #7530 [component: examples] Add axis names to scatterplot matrix
    + #7531 [component: bokehjs] [component: docs] Update
    documentation after removal of `range1d(start, end) syntax`
    + #7542 [component: docs] Fix typo in figure.vbar_stack docstring
    + #7549 Bokeh channel on anaconda.org contains broken version of
    packaging?
    + #7550 [component: docs] 'conda install flexx -c bokeh' fails on
    windows 7
    + #7553 [component: bokehjs] Make boxedittool match polydrawtool
    ui
    + #7559 [component: tests] Fail travis ci tests when there are ts
    compilation errors
    + #7571 [component: build] [component: docs] Enforce usage of npm
    >= 5.6
    + #7584 [component: build] Don't repeat base install for external
    prs
    + #7585 [component: build] Rev conda_reqs and ignore built python
    files for docker images
    + #7588 [component: docs] Sort all sphinx docs by file
    suffix. 'py' first
    + #7602 Bokeh should not instance its loggers using:
    logging.getlogger(__file__)
    + #7654 [component: bokehjs] [widgets] Datatable index column
    enhancements
    + #7662 [component: docs] Anonymize google analytics collection
    + #7690 [component: docs] The readme.md contains typos and could
    be written more concisely
    + #7711 [component: docs] Typos on palettes page
    + #7716 [component: docs] Release docs for 0.12.15
* Thu Mar 22 2018 toddrme2178@gmail.com
- Add "packaging" dependency
* Sat Feb 10 2018 arun@gmx.de
- specfile:
  * update copyright year
- update to version 0.12.14:
  * bugfixes:
    + #5420 [component: bokehjs] View.classname doesn't respect class
    structure
    + #6655 [component: bokehjs] X/y_range not properly set with tile
    source
    + #6680 [component: bokehjs] Datetime (convert_datetime_type)
    seems to add in extra milliseconds
    + #6932 [layout] 0.12.9 misplaced figure title
    + #7083 [component: bokehjs] Factorrange regression: plot does not
    get updated when factors change
    + #7101 [component: bokehjs] [widgets] Broken datatable
    selecteditor
    + #7139 [component: bokehjs] [regression] [widgets] Datatable
    automatically scrolls down when app loads
    + #7218 [component: bokehjs] Circle not circular
    + #7266 [layout] [regression] Spacer does not display using show
    on 0.12.11
    + #7290 [component: bokehjs] Regression in boxzoomtool with
    match_aspect
    + #7291 [component: bokehjs] Hovertool with attachment="vertical"
    incorrectly positions tooltips
    + #7295 [component: docs] Removed a broken link from server.rst
    + #7298 Remove dependency on phantomjs when other webdriver is
    used
    + #7304 [component: bokehjs] [regression] [widgets] Datatable
    editing regression
    + #7319 [notebook] Themes not applying in the notebook
    + #7327 Output_png and output_svgs fails in the
    settings.phantomjs_path( ) function.
    + #7337 [component: bokehjs] Legend entry for text renderer causes
    error
    + #7370 [component: bokehjs] Regression in graph rendering during
    zoom
    + #7373 [component: bokehjs] [regression] "number.isinteger()"
    javascript error of slider in internet explorer
    + #7386 [component: docs] Error in documentation for handling
    categorical data
    + #7398 [component: bokehjs] [regression] [typescript] Missing
    import of includes function in tile_renderer
    + #7400 Issue with figure and legend when a dataframe is passed as
    a source
    + #7412 [component: bokehjs] [typescript] Variables in widget
    selectview undeclared
    + #7439 [component: bokehjs] [notebook] [regression] Regression
    displaying embedded bokeh plots outside the notebook
    + #7443 [component: bokehjs] [layout] [regression] Bokeh layout
    elements overlap in new version
    + #7448 [component: bokehjs] [regression] [typescript] "typeerror:
    hits.map is not a function" when hovering over multiline
    + #7452 [component: bokehjs] [regression] [widgets] Revert
    nouislider rev update
    + #7460 Bokeh.core.properties.date#transform fails on windows
    + #7461 [component: server] [regression] Unable to reuse sessions
    of a server application
    + #7470 [component: bokehjs] Polydrawtool does not emit event on
    double-click
    + #7475 [component: bokehjs] [regression] Setting range end or
    start through customjs not working
    + #7478 [component: bokehjs] [regression] Selection and
    nonselection glyph properties ignored
    + #7484 [regression] Cannot select tools in certain examples
    + #7488 [component: bokehjs] [regression] Renderers/glyph_renderer
    contains invalid syntax
    + #7503 [component: bokehjs] [regression] [widgets]
    Selecteditorview (and others) doesn't have access to its model
  * features:
    + #6370 [component: bokehjs] Proposing a bokeh draw tool
    + #7292 [API: models] Make it possible to create hovertool with
    attachment set to explicit left, right, above, below
  * tasks:
    + #3250 [component: bokehjs] Tool icons should have the same
    dimensions
    + #3551 Add https to tile providers urls in
    `bokeh/tile_providers.py`
    + #6605 [component: bokehjs] [component: build] Add support for
    tslint in bokehjs' build
    + #6681 [component: server] Streaming numpy datetime64 data does
    not work
    + #6887 Remove all server examples that use
    session.loop_until_closed
    + #7014 [component: bokehjs] The inherited width should be set to
    100%% and up to the user to implement margin and padding
    restrictions
    + #7084 [component: bokehjs] Factorrange regression: bokehjs
    crashes if data has values not in factorrange factors
    + #7164 [component: tests] Axes labels misplaced on multiple
    extra_x_ranges
    + #7267 [component: bokehjs] [component: build] Make bokehjs'
    build work with npm 5
    + #7288 404 error on website page for releases
    + #7289 [component: server] Sort application names in index page
    + #7308 [component: server] Tornado 5.0 compatibility
    + #7318 [component: docs] Make old/dev docs warning banner always
    float
    + #7323 [component: docs] Components not working with notebook
    show in the same cell
    + #7331 [component: tests] Replace strict fp equality with
    allclose
    + #7332 [component: bokehjs] [layout] Initialize box's layout
    variables in initialize()
    + #7344 [component: docs] Minor typos in bokeh server docs code
    example
    + #7346 [component: tests] Resolve pytest --log-file conflict
    + #7354 [component: bokehjs] Remove resettool.reset_size
    + #7376 Add traceback information to exception messages callbacks
    + #7385 [component: docs] Fixed a broken link ('why anaconda')
    + #7391 [component: bokehjs] Multi-gesture tools do not work on
    proxytoolbar
    + #7405 Icons have various visual artifacts
    + #7420 [component: bokehjs] [component: build] [typescript] Move
    gloo2 to its own repository
    + #7426 [notebook] Allow push_notebook() to run when no change has
    occurred
    + #7431 [component: bokehjs] [typescript] Remove attrs from
    hasprops.initialize()
    + #7434 [component: docs] Remove references to autoload_server()
    from the docs
    + #7455 [component: docs] State and check min phantomjs version
    + #7458 [component: build] Update version number in
    package-lock.json
    + #7500 [component: examples] Expand elements example with tooltip
* Thu Dec  7 2017 arun@gmx.de
- update to version 0.12.13:
  * bugfixes:
    + #7283 [component: build] Windows install fails 0.12.12
* Tue Nov 28 2017 arun@gmx.de
- update to version 0.12.11:
  * bugfixes:
    + #1376 [component: bokehjs] [widgets] Implement `widget.disabled`
    + #1651 [layout] Grid plot with row of all none behaves badly
    + #3538 [component: server] Session could auto-no-op any callbacks
    invoked after the session is destroyed
    + #4561 [layout] Models/legends example broken
    + #4574 [layout] [regression] Plot border gets covered up by
    things stuck on edge
    + #4613 Hover tool has own column in ie
    + #4787 [layout] [widgets] Erroneous toolbar separator positions
    using tabs
    + #5761 [layout] Location in colorbar offsets from axis
    + #6065 [component: bokehjs] Touch events fail in device mode
    under chrome devtools
    + #6348 [layout] Layouts with multiple tab widgets don't work
    + #6409 [component: server] Screen distance spec fields fail with
    bokeh.client
    + #6466 [component: bokehjs] [layout] Rendering error with
    toolbar_sticky=false and sizing_mode='scale_width'
    + #6502 [widgets] Programmatically setting the active tab does not
    change the tab in 0.12.6 & 0.12.7
    + #6545 Patch bug: patch slices must have positive (start, stop,
    step) values, got slice(0, 200, 50)
    + #6583 [component: bokehjs] Rect not behaving correctly with zero
    height
    + #6600 [component: build] Downloading dependencies from
    scripts/deps fails
    + #6676 [layout] [regression] Axes' tick labels are trimmed when
    moving plot
    + #6841 [component: bokehjs] [regression] [widgets] Rangeslider
    css_classes not being updated anymore
    + #6946 [component: bokehjs] Graphrenderer view not updating
    + #7060 [layout] [regression] Twin_axis not showing label
    correctly in version 0.12.9
    + #7062 [component: bokehjs] Linked brushing does not work on
    second plot in gridplot
    + #7075 [layout] Changing title attributes does not work as
    expected in bokeh server
    + #7121 [component: docs] Documentation - typo in release file
    0.12.10
    + #7128 [component: server] [regression] When embeding bokeh
    server to flask, attributeerror: 'nonetype' object has no
    attribute '_id' shows up
    + #7162 [component: docs] Fix documentation for properties.rgb
    + #7184 [component: server] [regression] Support stream and update
    with pandas dataframes
    + #7189 [component: bokehjs] Hovertool data not completely
    matching when using cdsview filters in bokeh 0.12.11dev2
    + #7193 [component: bokehjs] [regression] Ion slider extension
    example broken
    + #7199 [component: bokehjs] Missing import of logger in
    toolbar.coffee
    + #7202 [layout] Layout of plot border with axis.visible = false
    + #7212 [component: bokehjs] [notebook] [regression]
    Ie11-incompatible syntax in
    bokeh/core/_templates/autoload_nb_js.js?
    + #7213 [component: bokehjs] Canvas image smoothing in ie11
    + #7222 Double encode escapes in html-safe json strings
    + #7224 [component: bokehjs] [regression] `sdy` in range info is
    inverted and affects panning gmaps
    + #7230 [component: examples] Spectrogram example image broken
    + #7240 [component: docs] Missing figure import on graph example
    + #7250 [component: bokehjs] [widgets] Slider callback doesn't
    occur on particular values
    + #7255 [component: bokehjs] [regression] Zooming performance
    regression in 0.12.11rc
  * features:
    + #1007 [component: docs] Documenting the documentation process
    and guidelines
    + #3644 [component: bokehjs] Would need a figure.step to create
    step line in plot
    + #4635 [layout] Right titles are too far out
    + #4711 Decorator for documenting what version a function or
    method first appeared
    + #5298 Box select does not work with vbar but tap tool does
    + #5937 [component: bokehjs] Lod in linked plots
    + #6565 [component: server] Avoid boiler-plate when constructing a
    bokeh server programmatically
    + #6599 Bokeh server url hard coded as over http
    + #7130 [component: bokehjs] [bokekjs] unable to use customjs in
    bokehjs
    + #7150 [component: bokehjs] [widgets] Adding optgroup
    functionality to select widget
  * tasks:
    + #4394 [layout] Axis label size change does not trigger a
    re-alignment
    + #4874 [layout] Toolbar css class occasionally is
    `bk-toolbar-null`
    + #5648 [API: models] Line renderer raises the "without value
    specification" when a columndatasource is used
    + #6174 [component: bokehjs] Hovertool vline/hline models for line
    glyph (_hit_span method) causes non-intuitive tooltips to
    appear
    + #6447 [layout] Switch layout's coordinate system from view to
    screen
    + #6626 [component: docs] Updates to /docs/dev_guide/setup.html
    + #6990 [component: bokehjs] [layout] Allow toolbar in side panels
    and drop sticky property
    + #7028 Gmaps incompatible with datarange1d, make error
    louder/earlier
    + #7039 [component: docs] Clarify some security considerations
    + #7053 [component: examples] [component: tests]
    Plotting/file/categorical_scatter_jitter needs a seed
    + #7081 [component: docs] User guide still refers to
    bokeh.embed.notebook_div
    + #7096 [component: docs] Typo in server.rst
    + #7100 [component: docs] Renamed custom attribute from range to
    slider
    + #7103 [component: docs] Update bokehjs standalone installation
    guidelines
    + #7104 Bokeh channel version of nodejs is no longer in sync with
    upstream anaconda/nodejs
    + #7114 [component: bokehjs] Add wheelpantool support to bokehjs
    + #7131 Prove of concept: caching of nodejs compilation on model
    bundling
    + #7154 [typescript] Investigate coffeescript 2 and its benefits
    for transition to typescript
    + #7172 [component: docs] Extending bokeh with js library
    documentation needs to clarify use of javascript() to wrap js
    + #7179 [component: docs] Zeppelin notebook integration not
    working
    + #7181 [component: tests] Move annotations' "integration" tests
    to examples
    + #7190 [component: docs] Legend text with click_policy="hide"
    + #7198 [component: docs] Request for improvement to
    columndatasource documentation in reference to multi_line()
    + #7200 [component: docs] Adding additional information in the
    multi_line() documentation
    + #7207 [component: docs] Add kwargs documentation for
    directoryhandler
    + #7229 [component: docs] Multiprocessing in windows is not
    available (error:module 'os' has no attribute 'fork')
    + #7236 [component: examples] Simplify brewer.py example
* Wed Oct 18 2017 arun@gmx.de
- update to version 0.12.10:
  * bugfixes:
    + #4247 [notebook] Performance issues after repeated
    `push_notebook` calls
    + #4965 Datepicker errors on input from chrome on windows 8.1
    + #5415 [notebook] Having multiple `push_notebook` calls in the
    same widget callback doesn't work
    + #5452 [notebook] Plotting bug when using push_notebook() from
    customjs callback
    + #6258 [regression] Colorspec processing is broken
    + #6590 [component: server] Tile sources cannot be shared between
    app sessions
    + #6820 [component: bokehjs] Cdsview not working with text glyph
    + #6831 [component: examples] [regression] Color slider example
    can show hex fp values
    + #6846 [component: bokehjs] Categories on yaxis with hbar fails
    to set initial ranges
    + #6863 [component: server] Datatables do not update properly for
    on_change events 0.12.7
    + #6891 [component: bokehjs] [regression] Customjs for hover no
    longer working - bokeh 0.12.7
    + #6910 [component: bokehjs] The new feature filter (cdsview) not
    behaving has expected
    + #6921 [component: bokehjs] [notebook] [regression] Shared drag
    tools in grid plots only work on the last plot
    + #6926 [component: bokehjs] Daterangeslider incorrect value
    displayed
    + #6947 [component: bokehjs] Color mapping in circle fill colors
    does not take current view (cdsview) into account
    + #6949 [component: bokehjs] Length_units has no effect for rays
    + #6955 Possible bug: hover tool does not work with filtered
    source
    + #6982 [component: bokehjs] Bugfix: bokeh-server: ie fails with
    "object doesn't support this action"
    + #6986 [component: bokehjs] Mercatorticker behavior poorly
    defined for ranges exceeding mercator bounds
    + #6993 [component: bokehjs] [regression] Bad positioning of
    colorbar for 'above' and 'below'
    + #7015 [component: bokehjs] [regression] Functickformatter broken
    with categorical axis
    + #7035 [component: bokehjs] [regression] [widgets] Datatable with
    dynamic number of rows is unstable and breaks
    + #7044 [component: server] Bokeh server sessions not released
    correctly
    + #7048 [component: bokehjs] Datepicker returns one day earlier
    than picked in ie
  * features:
    + #3601 [component: bokehjs] Patchesview._mask_data() changes the
    draw order
    + #4117 [component: bokehjs] Add support for client side filtering
    of data sources
    + #4911 Updating two glyphs using periodic callback
    + #6945 [component: bokehjs] [component: server] [notebook] Use
    bokeh protocol to implement push_notebook
    + #6951 Y_range doesn't understand numpy arrays
  * tasks:
    + #4049 [component: docs] Improve documentation to support running
    unit tests locally
    + #6666 [component: docs] [component: examples] Update sliders in
    examples
    + #6704 [component: bokehjs] Hovertool hit detection fails on
    vertical and near-vertical segment glyphs
    + #6718 [notebook] Push_notebook updates at most one plot
    + #6918 [component: docs] Js code error in documentation
    + #6928 [component: docs] Bryanv/cleanups
    + #6937 [component: docs] Fix typo in notebook.rst
    + #6938 Stop computing unused and expensive bokeh.__base_version__
    + #6943 [component: docs] Fix docstrings
    + #6952 Canonicalize bokeh.client
    + #6957 [component: docs] Generate uuids for sphinx docs js script
    names
    + #6962 [component: docs] Gridplot doctext formatting error
    + #6971 From_networkx fails with networkx 2.0
    + #6978 Passing an index for factors throws value error
    + #6991 [component: docs] Out of date reference to matplotlib in
    user guide for color bars?
    + #6994 Canonicalize bokeh.colors
    + #6999 [component: docs] Incomplete docs re embedding when using
    data tables
    + #7009 [component: tests] Reduce size of travis ci logs
    + #7016 Fix codebase issues
    + #7021 Canonicalize more top level modules
    + #7022 Clean up sampledata
    + #7029 [component: examples] Fixed url typo in examples app &
    changed readme url to https
    + #7031 [component: docs] Server docs are misleading
    + #7033 [component: docs] `bokeh-demos` link doesn't exist
    + #7041 Changed to handle nx2 scale "kwarg error
    + #7052 [component: build] Upgrade typescript to version 2.5.3
    + #7056 [component: bokehjs] Remove bk-logo-{medium,large}
* Sun Sep 24 2017 arun@gmx.de
- update to version 0.12.9:
  * no changelog available
- changes from version 0.12.8:
  * bugfixes::
    + #1329 [widgets] Daterangeslider re-sizing
    + #2268 [widgets] Daterangeslider not rendering
    + #4048 Bounds on axis causes axis labels to go off page
    + #4876 [layout] Tile attribution misaligned (see toolbar on
    right-side example)
    + #6842 [component: docs] Bokeh.models.widgets.sliders is missing
    from the reference documentation menu
    + #6844 [notebook] Bug: bokeh.io.push_notebook is broken
    + #6850 [layout] [regression] Log-axis label layout issue
    + #6852 [component: bokehjs] [regression] Hovertool not rendering
    on hbar glyphs in 0.12.7
    + #6859 [component: bokehjs] [regression] Dateformatter not
    working in tables
    + #6860 [component: examples] Patch color_sliders.py
    + #6873 [component: bokehjs] [widgets] Unable to render <, >, & in
    datatable
    + #6880 [widgets] Datatable rendering broken in notebook
    + #6885 [component: docs] Typo in edgesandlinkednodes docstring
    + #6898 [component: docs] [doc] adjust docstring indentation
    + #6908 [component: bokehjs] [notebook] [regression] Running
    output_notebook with hide_banner=true broken
    + #6909 [notebook] Notebook output generates console errors
    + #6922 [notebook] Unprotected ipython imports break bokeh without
    notebook installed
  * features:
    + #994 Text doesn't respect new lines
    + #5984 Improve data transfer, using a binary transfer protocol
    + #6865 Allow supplying explicit edge paths to graphrenderer
    + #6876 [component: bokehjs] New feature: add a "resettool
    clicked" event
    + #6895 Bokeh daterangeslider returns tuple of integers instead of
    dates
  * tasks:
    + #2458 [component: examples] Add examples for daterangeslider and
    datepicker
    + #5065 Task: refactor select tools
    + #6472 [layout] Make layout canvas' panels not overlap in corners
    + #6560 Using "export_png" or "save" without filename from within
    jupyter notebook saves png file to lib/python
    + #6612 Task: graph visualization improvements
    + #6700 [component: bokehjs] [component: build] [notebook] Bokeh /
    jupyterlab integration
    + #6819 [component: tests] Switch examples tests to use python 3.5
    or 3.6
    + #6832 Simplify data frame length calculation
    + #6837 Remove mpl and bokeh.charts
    + #6847 Check nodejs version number and update documentation
    + #6851 Plots which contain glyph's with infinite bounds fail to
    set initial ranges when match_aspect is set to true
    + #6869 [component: bokehjs] Remove leftover code after pr #6752
    + #6878 [component: bokehjs] [component: server] Bryanv/document
    cleanup
    + #6888 Add trace log level on python side
    + #6902 Add network-related sample data source
- changes from version 0.12.7::
  * bugfixes:
    + #515 Line plots render selections wierd
    + #516 Labels on axis do not like ":" character ;-)
    + #517 Better control over data/screen aspect ratios needed for
    large circles
    + #2240 Tick format language
    + #2527 [widgets] Rendered slider* plots have missing bk-* classes
    + #3466 [geo] Consider dynamic_map.py for deprecation
    + #3935 [component: server] [component: tests] How to get the
    server examples testable again
    + #4295 [component: bokehjs] Investigate disabling user-select
    + #4337 Plot blank if categorical label too long
    + #4503 [component: bokehjs] Date picker widget is unstyled
    + #4507 [widgets] Problem rendering un-wrapped sliders
    + #4599 [component: bokehjs] [layout] Wrapping output in center
    tag causes toolbar misalignment
    + #4880 Error plotting dates before 1970 (on windows?)
    + #4972 [layout] Plot collapses on adding multiple labels
    above/below the plot if title='none' not specified in plot()
    + #6121 [component: bokehjs] [widgets] Autocomplete input
    appearance differs between notebook and html file output
    + #6185 [component: server] Unable to interactively update
    renderer (i.e. circle, triangle, etc.) size using bokeh server
    + #6279 [component: docs] Documentation link not working right
    + #6308 [component: bokehjs] [widgets] Sliders :: customjs can not
    dynamically change title
    + #6450 [component: bokehjs] [layout] Canvas outline does not
    cover top of canvas
    + #6464 [component: build] Examples upload failed on full release
    build
    + #6474 [layout] New panels to a tabs widget does appear
    + #6478 [component: bokehjs] [widgets] Editable data tables not
    modifying python source.data - bokeh server 0.12.6
    + #6486 [component: build] Revert conda build to --no-test
    + #6501 [component: bokehjs] [regression] [widgets] Multiselect
    selection highlight no longer present when programmatically
    selected
    + #6507 [component: docs] User guide docs clerical error
    + #6509 Bokeh png command doesn't maximize window to capture
    entire output
    + #6514 New phantomjs sessions spawned inside bokeh.io._get_svgs
    despite driver arg
    + #6525 [component: tests] Py.test bokeh/tests/test_io.py doesn't
    kill phantomjs precesses
    + #6535 [component: tests] [regression] Py.test reports for
    integration tests are broken
    + #6549 [typescript] Upgrading to typescript=2.4.1 breaks gulp
    build task
    + #6571 [component: build] Export google_api_key in test:docs
    + #6576 [API: plotting] [component: bokehjs] [regression] Bokehjs'
    plotting api broken after pr #6260
    + #6578 [component: tests] [regression] No link to integration
    tests' report after pr #6542
    + #6592 [regression] [webgl] Save tool not functioning for webgl
    backend figures 0.12.6 regression
    + #6593 [component: bokehjs] Vbars with negative y/height do not
    work with hover
    + #6606 [component: docs] "taptool" is incorrectly called
    "tapselecttool" in the reference documentation
    + #6616 [component: bokehjs] [widgets] Pre-selection on rows in a
    bokeh datatable fails to display such selection
    + #6620 [component: build] Scipts/deps.py only works in the root
    environment.
    + #6628 [component: bokehjs] [component: server] [regression]
    Filterable cds broke cds streaming
    + #6642 [component: examples] [regression] [widgets] Export_csv
    example under 0.12.7dev11 doesn't resize table
    + #6653 Typeerror: 'unicode' does not have the buffer interface
    + #6679 [component: bokehjs] [component: build] [notebook]
    [regression] Bokehjs fails to load at all in notebooks after
    0.12.7dev12
    + #6725 Bug: linked selection example doesn't work
    + #6730 [component: bokehjs] Setting range_padding to 0 can lead
    to an empty plot
    + #6731 Setting visible=false doesn't work with glyph functions
    + #6736 [component: bokehjs] Attaching ajaxdatasource to multiple
    glyphs leads to multiple ajax requests
    + #6739 [component: docs] Plots don't render in dev docs due to
    missing resources
    + #6740 Graphrenderer doesn't correctly handle single node graphs
    + #6755 [component: bokehjs] Colormapper special colors do not
    support alpha
    + #6757 [component: examples] Examples/app/spectrogram bug
    + #6786 [component: bokehjs] Label using screen units bound to
    frame is positioned relative to canvas
    + #6808 [component: bokehjs] [notebook] [regression] Nbconverted
    static notebooks fail to render
    + #6809 [component: bokehjs] [notebook] [regression] Inline,
    minified resources do not work in classic notebooks
    + #6829 [component: bokehjs] [regression] Degraded hovertool
    performance in 0.12.7rc4
  * features:
    + #187 Support graphs/trees/networks
    + #474 Easily control aspect ratio
    + #4070 Plotting with subsets (row-wise) of columndatasources
    (like filtered data)
    + #4538 [starter] Allow layout function to accept arbitrarily
    nested lists
    + #5992 Pass http request arguments to autoload_server and
    pull_session
    + #6375 [component: build] Developer docker tools
    + #6492 [component: bokehjs] [widgets] Expose textinput type as a
    property of widget. (for password typing)
    + #6598 [component: server] [notebook] Server url hard coded as
    localhost. with possible fix
    + #6601 [component: bokehjs] Add major_label_overrides to colorbar
    + #6621 [component: server] Add metadata support to bokeh server
    + #6667 Creating a columndatasource with a dataframe makes it
    impossible to use streaming
    + #6709 [component: bokehjs] Increase the number of zoom levels
    available to bokeh tile sources
    + #6788 [notebook] Make notebook display extendible by external
    libraries
  * tasks:
    + #2452 [component: examples] [widgets] Add examples with widgets
    using plotting interface
    + #3245 [component: docs] List methods at top of documentation for
    figure class
    + #3517 Hovertool fails for rects with only negative heights
    + #3917 [component: docs] [component: examples] (re)move
    `tests/compat`, `tests/glyphs`, `tests/notebook`
    + #4196 Remove the resize tool?!
    + #4752 [component: docs] 0.12: missing `toolbar_sticky`
    documentation on migration guide
    + #4859 [component: docs] Bokeh plot in jupyter slides not
    rendered corretly
    + #5431 [component: server] [enh] bokeh server to show url
    + #5502 [component: bokehjs] [widgets] Consider nouislider to
    replace all our slider widgets
    + #5506 [component: bokehjs] [widgets] Fix datepicker widget
    + #5596 [widgets] Fix/drop autocompleteinput
    + #5628 [component: examples] Add synthetic data mode to
    spectrogram
    + #6283 [component: build] [component: tests] Implement travisci
    stages to improve ci builds
    + #6291 Add "png" bokeh command
    + #6332 [component: bokehjs] [component: build] Remove css 'bk-'
    prefixing
    + #6369 Add height/width kwargs to bokeh.io.export to support
    resizing the exported png
    + #6377 [component: docs] Docs suggest `text_align` property works
    on figure titles but it doesn't
    + #6395 [component: bokehjs] [component: build] Investigate errors
    with ts-node 4.0.5
    + #6439 [component: server] Server(..., io_loop=io_loop,
    num_procs=0) --> runtimeerror
    + #6441 [component: tests] Enable exclusion of selenium tests for
    static image export
    + #6453 [component: examples] [starter] Numpy runtime warning in
    missing data example
    + #6455 [API: models] Drop tool.plot property
    + #6467 [component: build] Start building new conda no-arch
    packages for bokeh channel
    + #6480 Bokeh.util.serialization.py convert_datetime_type breaks
    when passed timezone aware datetime
    + #6487 Remove all 0.12.4 deprecations
    + #6496 [component: docs] Reference docs are missing
    bokeh.models.scales automodule
    + #6497 [component: build] Update linux dist on travisci
    + #6512 Bokeh 0.12.6 incompatible with python 2.7.9?
    + #6521 [component: bokehjs] [component: server] Deprecate
    toolevents
    + #6529 [component: build] Only run js tests on py3 builds for now
    + #6530 [component: build] Split bokeh-widgets into bokeh-widgets
    and bokeh-tables
    + #6532 [component: bokehjs] [component: build] Remove
    bokehjs/src/vendor and all associated logic
    + #6543 Remove requests as runtime dependency?
    + #6546 [component: tests] Set initial date in date picker in
    models/file/widgets
    + #6550 [component: docs] Image for jitter example on gallery does
    no reflect example
    + #6557 [component: bokehjs] [component: build] Simplify bokehjs'
    build
    + #6563 [component: build] Fix up stages install order issues
    + #6568 [component: build] Hotfix for travisci log truncation
    + #6577 Columndatasource.stream() setter argument is not
    documented
    + #6581 Deprecate openurl?
    + #6584 [component: bokehjs] [component: build] Add a sample
    configuration for bundling with webpack
    + #6596 [component: docs] Add typescript version of
    extensions_putting_together.py
    + #6619 [component: examples] Examples/howto/server_embed uses
    sample data from web that no longer works
    + #6627 [component: docs] Add additional instructions to
    /docs/dev_guide/setup.html
    + #6629 [component: docs] Reference documentation missing
    bokeh.application and bokeh.command
    + #6634 [component: examples] Add example of custom tooltip to
    example library
    + #6651 [component: docs] Documentation for `crosshairtool` not
    updated
    + #6658 Task: add polyselecttool callback attr
    + #6684 [component: docs] Following dev documentation fails for a
    clean conda env
    + #6687 [component: docs] Bug in "running a bokeh server" page
    + #6700 [component: bokehjs] [component: build] [notebook] Bokeh /
    jupyterlab integration
    + #6715 Remove deprecated functions
    + #6717 [component: docs] Update docstring to reflect changes
    released in 0.12.0
    + #6721 [component: bokehjs] [typescript] Drop tsx templates
    + #6747 Task: expose webdriver as kwarg to export_png and
    export_svgs
    + #6750 [component: docs] 0.12.7 docs/examples
    + #6762 [component: server] [component: tests] Random data in
    server examples causes image diff to fail
    + #6791 Task: refactor jupyter notebook integration to use custom
    mimetypes
    + #6796 [component: examples] Add examples from pycon.pl tutorial
    + #6800 [API: models] [widgets] Automatic configuration of
    slider.format
    + #6810 Call load_notebook via notebook hook
    + #6823 [component: bokehjs] Improve styling of slider widget
* Thu Aug 17 2017 toddrme2178@gmail.com
- Update to version 0.12.6:
  * bugfixes:
    + #2136 Selections only work on the last of two series in one plot
    + #2680 Non-unit specs accept still allow `units` field
    + #3386 `property.__delete__` does not send a change notification
    + #3564 [component: bokehjs] [widgets] Getting values of selected rows from a datatable after reordering with sort
    + #3838 Push_notebook doesn't seem to work display updated table content
    + #4294 [notebook] Replace table source
    + #4433 [layout] Gallery example issues
    + #4657 [regression] Adding an unwrapped widget to document, may not render properly
    + #4764 [component: server] [layout] Issue with interactions between widgets and plots using bokeh server
    + #4810 [component: server] [layout] Trouble swapping out layout contents when using server
    + #4829 [layout] Tabs only consisting of datatables not drawn correctly
    + #4872 [component: server] Arrows not updating from streaming data source
    + #5044 Shift selection in linked brushing plots
    + #5131 [layout] [widgets] Unexpected initial layout with datatable and layout()
    + #5198 Hovertool line_policy 'nearest' 'next' not working
    + #5207 [widgets] Need to resize window before datatable row labels show up
    + #5246 [component: tests] [regression] Py.test prints garbage when there is a syntax error in *.py files
    + #5499 [component: bokehjs] Datetimes on plot are always treated as local time and shifted to utc
    + #5518 [layout] Add new child to existing column
    + #5634 [component: docs] Fix documentation of 'bokeh html foo.py'
    + #5811 [component: bokehjs] Vbar width not updating correctly when too many things updated through `push_notebook`
    + #5856 [component: bokehjs] [layout] Plot becomes unresponsive when button widget is appended to layout
    + #5907 Hover inspection does not work for all glyphs
    + #5914 [component: bokehjs] Unable to right align tick labels
    + #5967 [layout] Unexpected behavior when deleting from layout.children
    + #6005 [component: bokehjs] Box select rendered incorrectly on bokehjs linked example
    + #6035 Na values correctly skipped in linear scale but not in log scale
    + #6047 [component: docs] User_guide/embed.rst still references collections
    + #6080 [component: server] Prefix bug on "active bokeh applications" page
    + #6085 [component: bokehjs] Hover tooltips update impossible
    + #6091 [layout] Sizing_mode breaks gmap alignment
    + #6095 `imageurl.{w,h}` use data units by default
    + #6104 [component: build] Twine upload in build/upload release script incorrect
    + #6105 [component: build] Setup.py auto-generates a bad empty string classifier
    + #6108 [component: bokehjs] [component: tests] Error using datarange1d with auto start/end and datetimeaxis
    + #6111 [component: docs] Fix typo in selection documentation
    + #6115 [component: bokehjs] [widgets] Descending order with tablecolumn still ascending
    + #6120 [component: bokehjs] Hover responds to hidden data when legend.click_policy = 'hide'
    + #6123 [component: bokehjs] [regression] [widgets] Rangeslider bug
    + #6124 [component: bokehjs] Update core/dom.ts to work with upcoming typescript 2.3.0
    + #6127 [component: bokehjs] [regression] Issue upgrading from bokeh 0.12.4 to 0.12.5 with ie 11
    + #6130 [component: bokehjs] Multiline hit_test fails if line_width property utilized
    + #6142 [component: bokehjs] [regression] Regression in legend positioning
    + #6152 [component: bokehjs] [component: server] Bokeh server is incompatible with tornado=4.5
    + #6156 [component: build] [component: docs] Optimized python execution fails due to missing __doc__ instantiation
    + #6199 [component: server] Client.coffee sets binary type incorrectly
    + #6205 [component: tests] Typescript 2.3.0 breaks customjs tests
    + #6207 [component: bokehjs] [regression] [widgets] Htmltemplateformatter still uses underscore
    + #6208 [component: bokehjs] [regression] Possible to use gesture tools after disabling in toolbar
    + #6210 [component: bokehjs] [regression] Bokehjs doesn't work in notebook
    + #6212 [regression] Issue with test build 0.12.6dev3 on windows 7 with ie11
    + #6213 [component: bokehjs] [layout] [regression] Appending layout regression
    + #6226 [component: bokehjs] [component: build] Update coffee-script's version to 0.12.5+
    + #6238 [component: bokehjs] Mousewheel event: delta=none at all times
    + #6244 [component: build] Fails to build in windows 7
    + #6248 [API: plotting] [regression] Gmap not configuring mercator tick formatter
    + #6252 [component: examples] Embed multiple sample data mismatch length
    + #6261 [component: bokehjs] [layout] [regression] Adding new sub-layouts fails to set documemt
    + #6263 [regression] Plot validation doesn't happen for non-application layouts
    + #6301 Yahoo ichart api is failing, should use stock data from bokeh.sampledata.stocks
    + #6311 [regression] Spectrogram performance regression
    + #6316 Bug in screendistancespec serialization
    + #6319 [component: server] Bokeh server does not close http sockets
    + #6328 [component: bokehjs] [notebook] Gmap in notebook unreliable again
    + #6343 [component: examples] Scale/range incompatibility in examples/models/server/population.py
    + #6365 [component: bokehjs] [regression] Imagergba error during change events
    + #6366 Webgl isn't correctly deprecated bokeh 0.12.6dev7
    + #6388 [component: bokehjs] [regression] Selection tool regression
    + #6391 [component: build] Bokehjs' build uses gulp 3.x but @types/gulp 4.x
    + #6393 [regression] Modifying datasources broken
    + #6397 [component: server] More explicit match cases
    + #6398 [regression] [webgl] All webgl examples fail
    + #6400 [component: bokehjs] [regression] Line_select.py example broken
    + #6402 [widgets] Disabled button raises button click protocol event
    + #6411 [regression] Matches() is broken when pandas is not installed
    + #6416 [component: bokehjs] [regression] Hovertool broken with multi_line plots in 0.12.5
    + #6433 [component: bokehjs] [regression] Selecting a line from a multi-line when one is already selected causes an error
    + #6443 Svg images are incorrectly smoothed
    + #6449 [component: bokehjs] [notebook] Protect against exceptions when running inline code
  * features:
    + #538 Headless static (svg, png) image generation
    + #1239 Hover.tooltip convenience function for 'datetime' info
    + #1482 [starter] Datarange1d.rangepadding should allow "fixed" values
    + #1671 [starter] Allow users to specify explicit tick labels
    + #2352 Feature request: error bar plots
    + #5430 [component: docs] [enh] help widget tuned for end user
    + #5599 [component: bokehjs] Feature: hover tool inspector default
    + #5831 Numberspec coordinates should accept datetimes
    + #5885 [notebook] Support embed bokeh into apache zeppelin
    + #6044 "columns must be of the same length" warning does not show context
    + #6064 [component: bokehjs] Remove the hover menu item, and keep the hover function working
    + #6081 Feature request: add support for user-defined custom mappers
    + #6161 [component: bokehjs] Extend hit testing and hover support to segment
    + #6186 Themes not applied in `file_html`
    + #6285 [component: bokehjs] Extend patching to sub-items
    + #6286 [component: bokehjs] [widgets] Enabling/ disabling re-ordering of columns in datatable (freezing columns in place)
  * tasks:
    + #1833 Make get_version consistent between pip-intalled and conda-intalled devel builds
    + #2595 [component: docs] Update hovertool's documentation with field formatting, etc
    + #2984 [component: docs] Update sphinx version to fix documentation parsing issues for google style docstrings
    + #3016 [component: docs] Axis location must be set on creation (documentation fix)
    + #3656 [component: docs] Docs on widgets & interactions should link to the callbacks & events section
    + #4153 [component: bokehjs] Strict trigger() and listento()
    + #4449 [component: bokehjs] Ensure canvas state reset at start of drawing
    + #4948 [starter] Plot title ignores sizing and appears italicized if number is provided but no units are specified
    + #5007 [component: examples] [starter] Update unemployment examples
    + #5268 [component: bokehjs] Improve mappers' inheritance structure
    + #5694 [component: bokehjs] [component: tests] Report code coverage for bokehjs unit tests
    + #5819 [component: docs] Why i can't use operurl in widget callback (e.g. button callback)?
    + #5854 [component: bokehjs] Enable typescript's strictnullchecks
    + #5879 [component: examples] [component: tests] Make "bokeh finished rendering heuristic" work with non-plot examples
    + #5950 [component: docs] Expose all json representations in one place
    + #5951 [component: docs] Sphinxext.bokeh_plot broken
    + #6040 [component: docs] Callback.rst documentation incomplete
    + #6079 [component: docs] Clarify docs for hovertool
    + #6088 [component: examples] Fixing up examples/models/file/
    + #6102 [component: build] Have deploy script use github api token to avoid rate-limiting issues
    + #6113 [component: build] Pypi release includes `scripts`?
    + #6125 [component: bokehjs] Use nounusedlocals to discover unused imports, etc
    + #6129 [component: docs] Fix typo in issue_template.md
    + #6139 [component: bokehjs] [component: build] Use tslib to reduce size of bokehjs
    + #6145 Update obsolete output examples in bokeh.embed docs
    + #6158 [component: docs] For interactive legends, a note about `muted_color` would be helpful
    + #6164 Remove deprecations up to 0.12.3
    + #6184 [component: docs] Bokeh-api documentation improvement suggestions
    + #6188 [component: docs] Missing docstring description of ``state`` arg in bokeh.io.save
    + #6191 Fix deprecated datetime64 use for np_epoch
    + #6197 [component: bokehjs] Remove confusing aliases from layoutcanvas
    + #6228 [component: docs] Task: add missing `packaging` dependency to documentation requirements
    + #6242 [component: bokehjs] Task: remove computed properties implementation
    + #6245 Html title is not escaped
    + #6247 [component: bokehjs] [component: tests] Allow to write bokehjs unit tests in typescript
    + #6251 [component: bokehjs] [component: build] Allow to write bokehjs build files in typescript
    + #6254 Revert "deprecate x/y_mapper_type plot kwargs in place of first-class scale models"
    + #6267 [component: bokehjs] [component: tests] Merge tests/common into tests/core
    + #6269 [component: docs] Bokeh-github directive should not check urls by default
    + #6274 Futurewarning from pandas in bokehjsonencoder
    + #6287 [component: bokehjs] Add migration note for removal of document.resize()
    + #6295 [component: build] Update manifest.in
    + #6309 [component: server] Report tornado version on bokeh server startup
    + #6317 Deprecationwarnings on python 3.6
    + #6323 Add bkcharts shim and dependency
    + #6325 Downstream url for dynamic_map.py has ssl issue
    + #6326 [component: bokehjs] Passing renderer object in cb_data on hovertool customjs callback
    + #6331 [component: docs] Re-building docs - keyerror gallery exception
    + #6336 [component: bokehjs] Silence all change signals during initialization of models
    + #6338 [component: server] Feature request: configurable maximum upload size for tornado server
    + #6385 [component: bokehjs] Rely on request_render and fix up cs code
    + #6387 [component: docs] Fixed typos in setup doc
    + #6408 [component: docs] [component: examples] General 0.12.6 examples and docs tasks
    + #6419 [component: bokehjs] Restore events for "patch", "stream" and "do"
    + #6445 Bump required bkcharts version to 0.2
* Thu May  4 2017 toddrme2178@gmail.com
- Implement single-spec version.
- Fix source URL.
- Update to version 0.12.5
  * bugfixes:
    + #2058 [component: bokehjs] Point hit testing for rects broken with screen space widths
    + #2288 [API: charts] Handle nan as input to bar()
    + #2822 [component: bokehjs] [geo] [starter] Gmapplot resets to (0, 0)
    + #2964 [component: bokehjs] Gmap alignment still off in 0.10
    + #3461 [component: server] Notebook + server not working
    + #3737 [regression] Gmapplot doesn't display anything in jupyter v.4
    + #4135 [component: bokehjs] [component: build] Don't expose external typings beyond bokeh namespace
    + #4539 [component: tests] Js tests reporting as failed even when they all passed
    + #4667 [component: bokehjs] Arrow and line_width
    + #4722 [notebook] Curdoc().theme = theme(json=yaml.load()) is not applied to charts when used in jupyter notebook
    + #4835 Multiple gmap plots whiting out  in notebook.
    + #4875 [component: bokehjs] Graph 'running off'
    + #4952 Theme doesn't apply when using components
    + #4979 [component: bokehjs] [component: server] Cannot add renderers within a callback
    + #5063 [component: tests] Bokehjs tests are failing on regular basis
    + #5152 [component: examples] Wrong data shown in gapminder example app / slider update failing
    + #5185 [layout] [starter] Reset tool fails when figure passed width instead of plot_width, etc.
    + #5336 [component: bokehjs] Strange behaviour of rect-glyph
    + #5353 [component: bokehjs] Extensions do not render when using bokeh.embed.components / bokeh.embed.file_html apis
    + #5416 [component: bokehjs] Multiple model sync in one callback can fail
    + #5488 [component: bokehjs] [starter] Hide annotations via callback
    + #5582 [component: server] --num-procs x and curdoc().session_context.request.arguments don't go well together
    + #5629 [component: server] [starter] Bokeh server reports "none" port when there is a port conflict.
    + #5644 Hasprops.apply_theme does not work on container values
    + #5670 [component: tests] Integration test reports are garbled
    + #5695 [component: docs] Typo in palettes docs
    + #5700 [component: bokehjs] Safe-tag-fix
    + #5706 [API: plotting] Bokeh 0.12.4: columndatasource does not work anymore with bokeh.plotting.image
    + #5720 [component: bokehjs] [component: tests] [regression] It's not possible to debug tests anymore since #5659
    + #5731 [component: tests] Tests broken again, this time due to `attributeerror`
    + #5732 [component: bokehjs] [widgets] Datatable not wired up to respond to streaming patching
    + #5742 [component: examples] Missing template in flask_embed.py and tornado_embed.py
    + #5778 [component: bokehjs] [regression] Autoload_static uses jquery .data()
    + #5789 [component: tests] Some integration tests fail when run with python 2.7
    + #5818 [component: build] Conda convert windows packages cause an error
    + #5848 [component: server] Memory leak in bokeh application
    + #5861 [component: bokehjs] [regression] Instance of figure class in bokehjs does not have reference to xaxis and yaxis
    + #5887 [component: docs] Transform docstring ends abruptly
    + #5888 [component: tests] [regression] Tests/examples/examples_report_plugin.py assumes clone has a remote named origin
    + #5891 [component: docs] Dev_guide/server.html has broken link to user_guide/server.html
    + #5900 [component: bokehjs] Attempt to make layout less fragile
    + #5905 Embed components performance
    + #5910 [component: build] All ci jobs failing due to some change affecting js compilation
    + #5916 Cannot import from .ts in a custom extension
    + #5921 [component: bokehjs] Fix for small bug in array intersection method
    + #5936 [component: bokehjs] [component: build] Bokehjs builds are broken because of dependency update
    + #5954 [component: bokehjs] [regression] Latex label example is broken in dev docs
    + #5956 [component: docs] [regression] Sphinxext.bokeh_plot missing linenos option implementation
    + #5959 [layout] [regression] Notebook comms "basic usage.ipynb" broken
    + #5963 [component: bokehjs] [regression] Js error on callback
    + #5977 Themes aren't applied to document when using `save`
    + #5986 [component: bokehjs] Bug with firefox hover tool coordinates
    + #6006 Toolbar tooltips are blank in examples/app/crossfilter
    + #6012 Importing bokeh.models creates zombie process
    + #6014 [component: build] [regression] Sdists prompting for bokehjs build will block pip installs
    + #6015 [component: bokehjs] Fixed bug in model._process_event method
    + #6018 [regression] Hover tool broken due to undefined roundingfunction
    + #6023 [component: server] Accept server connections from any origin
    + #6030 Boxzoomtool and boxselecttool doesn't clear the overlay when end event is off the plot frame
    + #6032 [component: bokehjs] [regression] Multiple selections via shift+select don't work
    + #6037 [notebook] [regression] Repeatedly displaying a plot degrades performance
    + #6045 [component: examples] Fixed hover on gapminder to display country
    + #6051 [component: bokehjs] [regression] Middle and bottom plot won't pan in y-dimension in custom/gears/gears.py demo on firefox
    + #6054 Issues with examples/plotting/server/animated.py
    + #6059 [component: server] Python event callback not called if no js event callback is registered
    + #6063 [component: docs] Fixed href
    + #6069 [component: docs] Fixed broken link to gapminder example
    + #6075 Resettool does not trigger change events on range1d
    + #6100 Correct cursor handling
  * features:
    + #2274 [component: bokehjs] Interactive legends
    + #2414 [starter] Use [non]selection_glyph="auto" to generate automatically, not none
    + #3715 Interactively hide or show lines after plot finished by clicking (without re-ploting like plot browser feature in matlab)
    + #3748 [component: bokehjs] [component: server] Trigger python event when `level_of_detail` mode finishes
    + #4241 [component: docs] [starter] Create a custom 404 page for bokeh docs
    + #4694 [component: bokehjs] [starter] Angle of glyphs in legend doesn't match glyphs in plot
    + #4927 [component: bokehjs] [starter] Event handler for width/height change of plot
    + #5015 [component: bokehjs] [starter] Customjstransform
    + #5278 [component: bokehjs] [component: server] Feature: emitting tool and ui events and attaching callbacks
    + #5442 [component: bokehjs] [starter] Add scale control to gmaps
    + #5592 [component: bokehjs] [geo] [starter] Gmapoptions are not dynamically applied
    + #5692 [component: server]   make it possible to use relative urls
    + #5973 Cds creation from dataframes should not use tolist()
    + #6043 Avoid isinstance checks in _visit_value_and_its_immediate_references
    + #6055 Use math library instead of numpy for nan/inf checks
  * tasks:
    + #2933 [component: bokehjs] Use only `div` and `canvas` in the generated html
    + #2940 Gmapplot coordinate axes
    + #3210 [component: bokehjs] [component: server] [widgets] Improvements to events
    + #3270 [API: charts] General charts examples improvements
    + #4111 [component: bokehjs] [component: tests] [regression] Check js logs in tests
    + #4285 [component: tests] Testing infrastructure bug/wish list
    + #4321 [component: bokehjs] [webgl] Put webgl functionality in separate bokeh-gl.js?
    + #4854 Code of conduct needed
    + #5060 Limit imports of client/server code to only when necessary
    + #5102 [component: bokehjs] Hovertool tooltip css is vunerable to being overridden by other page css
    + #5121 [component: bokehjs] [component: tests] Fix skipped js tests as result of getter/setter work
    + #5174 [component: bokehjs] [starter] Task: support updating computed transforms fields if dependencies change
    + #5209 [component: build] Stop building noarch conda packages
    + #5232 [component: tests] Intermittently failing examples tests - ggplot_density and graphs
    + #5238 [component: build] [component: docs] Help make examples more visible and easy to use
    + #5254 [component: bokehjs] [component: examples] [component: tests] Examples involving transforms using math.random() fail image diff
    + #5495 [component: docs] [component: server] Document non-script and programmatic use
    + #5541 [component: build] Label image diff results "expected" vs "actual"
    + #5613 [component: build] Windows setup.py build from source and versioneer
    + #5625 [component: bokehjs] Drop jquery from core bokehjs
    + #5638 [component: docs] Examples / charts/ readme states incorrect location for jupyter notebook example code
    + #5640 [component: examples] New app example: exploding pivot charts
    + #5647 [API: charts] Make the default hover tooltip work for donut charts
    + #5664 Remove old deprecations
    + #5666 [py3] Python 3.6 compatibility
    + #5677 Permission denied error when invoking show() from inside jupyter notebook
    + #5679 [component: build] Deploy script should automatically create and upload examples tarballs
    + #5691 [component: docs] Fix a typo in layoutdom
    + #5699 [component: examples] Not necessary loop in weather example?
    + #5704 Move abstract out of properties.py
    + #5705 [notebook] Print bokeh version in notebook "bokehjs loaded" message
    + #5710 [API: models] Deprecate bokeh.models.layouts hbox and vbox
    + #5712 [component: tests] Make sure examples' tests wait until bokeh finished rendering
    + #5718 [component: docs] Bad formatting in selected docstring
    + #5726 [component: bokehjs] Tooltip font color can be turned white by outside css because it's not specified by bokeh
    + #5729 [component: bokehjs] Use only what we need from underscore
    + #5748 [component: tests] Bokehjs/examples/electron/node_modules interfere with code quality tests
    + #5754 Revert "clean up and refactor build"
    + #5756 Revert "bryanv/refactor build"
    + #5757 [component: bokehjs] [component: build] Remove bokehjs/src/vendor/kiwi and use bokeh/kiwi
    + #5759 [component: docs] Typo in axes docs
    + #5770 [component: build] Bryanv/build fixups
    + #5771 [component: build] Break up conda operations to prevent timeout
    + #5772 [component: build] Need to call chdir for persistent effect
    + #5773 [component: build] Fix path for css upload
    + #5775 [component: build] Try token with repr, add some diagnostics
    + #5776 [component: build] Globs don't work in subprocesses w/o shell=true
    + #5777 [component: build] Correctly implement put
    + #5787 [component: build] Pin mpl < 2.0
    + #5788 [component: docs] Migration notes and exceptions about mpl compat.
    + #5793 Bokeh calls logging.basicconfig()
    + #5796 [component: docs] Bokeh 0.12.4 needs python 3.3 but this isn't documented anywhere
    + #5799 Revert "fix rect rendering with log axis"
    + #5810 [component: bokehjs] Don't rely on typedarray.map
    + #5822 Hovertool for last value of a line plot sticks on second last value (works fine with circles)
    + #5826 [API: models] Add bokeh.plotting.gmap to create gmapplot correctly and easily
    + #5827 [component: build] Restore pip installable dev builds
    + #5834 [component: docs] Need to use different sintaxis when using command "bokeh serve" in windows command line
    + #5835 [component: examples] County data: most independent cities in virginia have 'city' left out, which causes confusion when trying to match based on county name
    + #5858 [component: docs] Update install.rst documentation
    + #5871 [API: models] Columndatasource constructor slow
    + #5878 [component: examples] Move models' file examples and add migration notes
    + #5880 [component: tests] Flake8 everything
    + #5882 [component: bokehjs] [component: examples] [component: tests] Test bokehjs/examples and run them on travis ci
    + #5895 [component: docs] Give feedback on bokeh server docs
    + #5896 [component: docs] Typo corrections and clarifications for user_guide/server (#5895)
    + #5902 [component: docs] Typo (missing comma) in example code for labels
    + #5915 [component: examples] Including the color option in the embed simple example
    + #5928 [component: tests] Test_api_crawler assumes it is run in the source directory
    + #5930 [component: bokehjs] Align bokehjs' imports with custom models
    + #5934 [component: bokehjs] Enable typescripts' noimplicitany
    + #5946 [component: build] [component: tests] Disable saucelabs tests for now
    + #5947 [component: build] [component: tests] Re-enable saucelabs tests
    + #5965 [component: bokehjs] Legend should have pointer cursor only when `click_policy != "none"`
    + #5969 Tweak defaults for interactive legend inactive labels
    + #5989 Remove deprecated output_server
    + #5998 [component: build] Update docs upload to work now that host site is behind cloudflare
    + #6010 Revert "deprecate mpl compat"
    + #6016 [component: examples] Sprint prints nan for seleted names set to none
    + #6024 [component: bokehjs] Use `throw new error(...)` instead of `throw error(...)`
    + #6036 [component: examples] Updating embed examples
    + #6039 [component: examples] When embedding with autoload into a page with a different public url need relative_urls=false
    + #6048 [component: docs] Leveraging other libraries should include datashader
    + #6058 [component: examples] Added a tiler with a valid url for second plot in plotting/file/airport_map
    + #6066 Change default for
    + #6071 [component: examples] Update element names and symbols in elements.csv
- Update to version 0.12.4
  * bugfixes:
    + #525 Columndatasource.prototype.get_length gives arbitrary results
    + #2064 Tooltip not working when inverting an axis by passing a `y_range` argument to the figure
    + #2162 Plotting none/nan values fails with log scale axis
    + #2365 [component: examples] Compat/seaborn/sinerror.py is broken
    + #2789 [component: docs] [starter] Range padding possibly discards the log axis properties
    + #3315 [API: charts] Overlapping bins in bokeh charts histogram example
    + #3834 Plot is empty when log scale is used
    + #3931 [component: docs] Update datetimetickformatter docstring with actual default formats from the js side
    + #4602 [API: charts] No x-axis labels on bar graphs with a single bar
    + #4680 [component: bokehjs] [widgets] Datatable header height not large enough to fit header text - in jupyter notebook
    + #4861 [component: bokehjs] Hovertool showing canvas coordinates not data coordinates
    + #5305 [component: docs] [component: examples] [component: server] Embed/animated fails with "did not find model"
    + #5306 [component: examples] [py2] Embed/embed_multiple fails with unicode error on py2
    + #5315 [component: examples] [component: server] [regression] Extension implementation load path problems in apps
    + #5318 Make figure accept title instance
    + #5322 [component: bokehjs] Long "bokeh error"s don't wrap
    + #5323 [component: bokehjs] Colormapper special colors are not respected for images
    + #5324 Colormapper high, low and nan_color do not accept rgb(a) tuples
    + #5330 Syntax error in util/deprecation.py
    + #5333 [component: bokehjs] Document._destructively_move() (in bokehjs) references undefined variable
    + #5337 [component: bokehjs] Charts and plots not rendering with user defined title text_font_size in em
    + #5346 Embedding a server plot will override the window title
    + #5370 [component: bokehjs] Linearinterpolator does not work correctly
    + #5377 [component: docs] Correct comment in dimension example plot
    + #5382 [component: bokehjs] Help tool icon doesn't have transparent background
    + #5389 Creating a line plot with `x_axis_type='log'` fails when `x_max < 1`
    + #5392 [component: bokehjs] [regression] Tools cause hard crash on safari after import/export pr
    + #5398 Datatable css conflict with bootstrap css
    + #5404 Functickformatter.from_py_func() example valueerror
    + #5413 [component: bokehjs] Can't use categorical axis with figure using rects
    + #5453 [py2] Tabe completion on bokeh.palettes doesn't work in python 2
    + #5467 [component: docs] Docstring not reflecting correct function signature
    + #5479 [layout] Merged toolbar is not created properly when row/column layouts added to gridplot
    + #5490 Some named palettes raise valueerror
    + #5522 [component: docs] Bokeh doc website not rendered correctly in ie 11 on win 7
    + #5524 [component: server] [regression] --num-procs broken
    + #5526 [component: bokehjs] Some versions of ie 11 do not support unit8clampedarray
    + #5546 [component: bokehjs] Js column length check logic is backward
    + #5549 [component: bokehjs] Correctly handle data values <= 0 on a log scale
    + #5555 [component: bokehjs] [regression] Bokehjs' examples are broken after import/export pr
    + #5558 [notebook] [py2] [starter] Unicode `__javascript__` external resources breaks output notebook in python 2
    + #5570 [component: bokehjs] Output_notebook raises javascript error if hide_banner=true
    + #5576 [component: bokehjs] Initial range calculation for log plots can cause empty plots
    + #5585 [component: server] Responsive plots don't work with server because of plotdiv
    + #5590 [component: server] Python 2 incompatibility issue with execfile and bokeh server
    + #5591 [notebook] [regression] Custom models don't work in the notebook due to missing __file__
    + #5631 [component: build] [regression] Pin build job to py3.4
    + #5633 [component: build] [regression] Update .travis.yml
    + #5636 Patches incorrectly draws boundaries from geojsondatasource in latest development version on a bokeh server
    + #5645 Font-awesome custom example fails to run
    + #5655 [component: bokehjs] [regression] 0.12.3 resize tool uses plot_width for initializing plot_height
    + #5661 [component: bokehjs] Tool labels appears empty on hover
  * features:
    + #1448 Gridplot could allow 1d child sequence together with (n, m) tuple
    + #1996 Rangeslider needed (again)
    + #2016 [component: bokehjs] X_range = 'auto' with bokehjs
    + #2204 [component: bokehjs] [component: server] [notebook] Look into use of dataviews and arraybuffers for more efficient data send/recv
    + #2833 Using hovertool to display arbitrary html
    + #3817 Toolbar improvements: replace inspector dropdown
    + #5000 Warn on ragged length values in columndatasource
    + #5199 [API: models] Add support bokehjs writable and bokeh readonly properties
    + #5317 Add a colorblind and d3 palettes
    + #5329 Ability to remove tools from plot generated by mpl.to_bokeh
    + #5417 [component: bokehjs] [widgets] Extend textinput with `placeholder`
    + #5435 [component: bokehjs] [enh] add js callback for streaming data
    + #5446 [API: plotting] [component: docs] Improve glyph method function signatures
    + #5471 [component: bokehjs] [enh] add custom classes to elements
    + #5579 [component: bokehjs] [widgets] Adding size attribute to multiselect model
    + #5583 [component: server] [starter] Custom context arguments for the jinja template
  * tasks:
    + #3020 [component: docs] [component: tests] Stricter docs build testing
    + #4290 [component: bokehjs] Clean up toolbar's css
    + #4652 [widgets] Remove broken dialog
    + #4774 [component: docs] Docs: google maps down
    + #4778 [component: docs] Docs: add to reference landing
    + #4785 [component: tests] Clean-up use of saucelabs connect on travisci
    + #4877 [component: docs] Need to include imagesource to docs
    + #4918 Using a custom json encoder
    + #4920 The documentation for `bokeh.plotting.figure` does not describe how to set the axis labels
    + #4991 [component: docs] [starter] Palette option for image/image not documented
    + #5112 [component: docs] [component: examples] [starter] Add an example using categoricalcolormapper and legend
    + #5190 [component: docs] Migration code for 0.12.2 not runnable
    + #5292 Inconsistent legend location naming
    + #5320 [component: bokehjs] [component: build] Use es6 import/export syntax instead of require()
    + #5325 [component: build] Improvements to deploy script
    + #5326 [component: examples] Examples with deprecation warnings
    + #5335 [component: examples] Depreciated example
    + #5339 [component: bokehjs] [component: build] Remove src/vendor/font-awesome and use npm
    + #5360 Better deprecation path for extensions
    + #5362 [component: build] Remove old bokeh-server
    + #5372 [component: server] Remove develop mode stub
    + #5375 [component: tests] [notebook] Notebook image diff tests broken due to "missing kernel"
    + #5376 Change palette references for the brewer qualitative palettes to be slices
    + #5384 [component: docs] Small docs fixes
    + #5395 [component: build] Please consider adding classifiers to setup.py
    + #5400 [component: examples] Add imdb usage notice to movies app
    + #5403 [component: docs] Hbar and vbar need to be added to the user guide
    + #5408 [component: docs] [component: server] Server architecture in dev guide has several out of date links
    + #5411 [component: docs] Document x_axis_location parameter to figure
    + #5423 [component: bokehjs] Prefer const over let in *.ts
    + #5445 [component: server] If main.py is run by bokeh serve, warn about running with directory name instead
    + #5450 [component: bokehjs] Add support for *.tsx source files
    + #5455 [component: tests] Outside pr docs test fails due to missing google api key
    + #5461 [component: docs] Add svg logo
    + #5492 [component: server] Support --port 0 for random port
    + #5493 [component: server] Avoid calling sys.exit in server code
    + #5494 [component: server] Bokehtornado.stop should not stop the ioloop
    + #5507 [component: bokehjs] Replace underscore's functions with native methods were possible
    + #5513 [component: bokehjs] Consider externalizing font-awesome's icons (or removing altogether)
    + #5514 [component: bokehjs] Further slim down boostrap
    + #5517 [component: docs] Small fixups to make sphinx 1.5 work
    + #5532 [component: bokehjs] Deprecate bokeh.$  and bokeh._
    + #5536 [component: bokehjs] Replace `@$(...)` with `@$el.find(...)`
    + #5553 [component: tests] Test custom models' examples
    + #5557 [component: build] [component: docs] [starter] Use python3 version of fabric
    + #5560 Get selenium testing working locally
    + #5562 Correctly deprecating imagergba cols and rows properties
    + #5567 [component: build] Explicitly kill stray processes on travis
    + #5568 [component: bokehjs] [component: build] Upgrade to jsdom 9.x
    + #5578 [API: plotting] [starter] Auto-conversion to columndatasource
    + #5587 [component: docs] Docstring typo
    + #5595 [component: docs] [component: server] Getting bokeh to work behind apache
    + #5602 [component: docs] Document dataspecproperty
    + #5607 [API: charts] Add vbar and hbar glyphs to charts
    + #5609 Investigate removing autoadd, autosave, autopush
    + #5619 [component: docs] Improve palettes docs and docs automation
    + #5626 [component: docs] Split up properties.py
    + #5627 [component: docs] Split up reference docs for bokeh.core
    + #5649 Add nodejs and npmjs version numbers to `bokeh info`
- update to version 0.12.3:
  * tasks:
    + #5258 [component: docs] Double ended sliders extension example
    + #5319 [component: docs] Issues release notes
  * bugfixes:
    + #2415 Trying to render the same plot twice is failing
    + #4347 [API: charts] Hover in charts not displaying data
    + #4616 Cannot edit cells in datatable
    + #4897 [component: docs] Subsections of user guide/adding
    interactions are rendered twice when selected in site guide
    + #4926 [regression] Autoload_static seems to be broken in version
    0.12
    + #5029 Importing us county data fails on 3.5
    + #5107 [component: docs] Bokeh.pydata.org warns that searching
    0.12.1 is old but latest isn't pointing to 0.12.2 yet
    + #5113 [component: bokehjs] Vbar / hbar legend missing glyphs
    + #5118 Gmapplot error attributeerror("'basicproperty' object has
    no attribute 'from_json'",)
    + #5119 Non-server bokeh requires tornado
    + #5123 Vbar hover tooltip not working in master
    + #5125 [component: bokehjs] [component: build] Bokeh npm install
    + #5130 [component: docs] Correct typo in the notebook docs
    + #5132 [component: build] Deploy.sh version update fails when
    last version is a full release
    + #5134 [component: bokehjs] [regression] Fix bad merge
    + #5156 Session.show() does not take into account browser
    + #5170 Viridis6 appears to be reversed
    + #5188 [component: bokehjs] Glyphview should not extend
    rendererview
    + #5202 [API: plotting] [regression] Figure legend not merging
    glyphs on the same data
    + #5218 [API: plotting] [component: bokehjs] [regression] Bokehjs
    plotting api is broken after pr #5017
    + #5223 [component: docs] Span annotation rejects `x` or `y` for
    `dimension` argument
    + #5234 [API: models] Plot not shown if datetimetickformatter
    partially defined
    + #5235 Wheel zoom is centers on center-of-plot, not mouse
    + #5239 [component: docs] Bokeh.models.transforms not in reference
    guide
    + #5248 [component: bokehjs] [regression] Add a polyfill for
    math.log1p() that's not supported by ie
    + #5260 [component: bokehjs] [memory] [regression] Plot updates
    cause heap to grow massively
    + #5271 [component: docs] Docserver.py input causes a syntaxerror
    + #5288 [component: docs] Typo in the legend location docs, and
    why "right_center" instead of "center_right"?
    + #5291 [component: docs] Docserver.py fix
    + #5294 [component: bokehjs] [layout] [regression] Responsive
    layouts broken in master
    + #5302 [component: examples] [component: server] [py2] Bokeh
    serve --show app/gapminder doesn't work
    + #5304 [component: examples] [component: server] [regression]
    App/surface3d doesn't work because custom model path is wrongly
    resolved
  * features:
    + #647 Support latex labels
    + #820 Split bokehjs in multiple plugins
    + #916 [starter] Add zoom button that allows zoom by steps
    + #1589 Bokehjs and node.js integration
    + #2381 Plainer default tooltip styling
    + #2590 [component: bokehjs] [webgl] Ongoing webgl related dev
    + #3856 [component: bokehjs] Populate legend with rows of data
    + #4621 Add `args` parameter to `functickformatter` similiar to
    `customjs`
    + #4886 Allow user defined models to inherit from user defined
    models
    + #5011 [component: bokehjs] [starter] Colormapping - color values
    out of high/low
    + #5013 Discrete/categorical colormapper and colorbar
    + #5153 [API: models] Implement _repr_pretty_ on hasprops and
    model
    + #5164 [API: models] Add support for _repr_html_ to hasprops and
    model
    + #5175 [component: bokehjs] [widgets] Slider with no title
    (feature request)
    + #5204 [component: bokehjs] Feature: support passing suggested
    width/height to document.resize method
    + #5242 Import_optional isn't robust to all import failures
    + #5255 [API: charts] Boxplot: outlier_line_color missing in
    default_attributes of boxplotbuilder
    + #5279 [API: models] Extensions cannot use own `.eco` templates
    as compiler won't compile them
  * tasks:
    + #2056 [starter] Deprecate glyph functions accepting datasource
    and sequence literals simultanously
    + #4526 [API: models] Remove "legend" prefix in some of legend's
    properties
    + #4879 Remove gear glyph from bokehjs to shrink resource size
    + #5076 [component: tests] [starter] Remove yield tests
    + #5083 [API: plotting] [component: docs] [starter] Add example
    using hbar/vbar to make bar charts
    + #5106 [component: bokehjs] Replace mget/mset/get/set with
    getters and setters
    + #5110 Revert "add categorical color mapper"
    + #5116 [component: bokehjs] Make hasprops.id a first class
    citizen
    + #5124 [component: bokehjs] Replace "else if" with switch
    statement
    + #5148 [component: examples] Imdb typo in movies app example
    readme
    + #5159 [component: build] Py.test should use phantomjs from
    bokehjs/node_modules/.bin by default
    + #5160 [component: bokehjs] Deprecate backbone.model.{get,set}()
    + #5165 [component: bokehjs] Bring some structure to our *.less
    sources
    + #5167 [component: bokehjs] Replace obj.unset('prop_name') with
    obj.prop_name = null
    + #5168 [component: build] Revert "pin conda-build version to
    1.21.14"
    + #5171 [component: bokehjs] Replacing jsnlog
    + #5180 Deprecation warning with matplotlib-2.0.0.b4 and bokeh
    0.12.2
    + #5182 [component: bokehjs] Move js palettes to bokeh-api.js
    + #5211 [component: bokehjs] [component: build] Upgrade timezone
    dependency and remove timezone from vendor
    + #5216 [component: bokehjs] [component: build] Upgrade to
    typescript 2.0
    + #5236 Unify and simplify deprecation of things
    + #5250 Change 0.12.4 deprecations to 0.12.3 due to delayed
    release
    + #5251 Change indentation to 2 spaces in *(.d).ts files to match
    other bokehjs sources
    + #5258 [component: docs] Double ended sliders extension example
    + #5262 [component: docs] Dev_guide/notes.rst wasn't updated in a
    year or more
    + #5263 [component: bokehjs] Move common/* to core/* and merge
    util/ with core/util/
    + #5264 [component: bokehjs] Split off backbone.events and don't
    depend on backbone.model if not necessary
    + #5277 [component: tests] With --rerun, bokehjs test harness
    needs to reset directory
    + #5284 Missing ts api for logcolormapper and
    categoricalcolormapper
    + #5299 [component: build] Use our own bokeh channel and avoid
    using conda-forge
    + #5312 [component: examples] Clustering app example does not set
    .data atomically
    + #5319 [component: docs] Issues release notes
- update to version 0.12.2:
  * bugfixes:
    + #4612 Updating of image colormapper
    + #4855 No fill for background and border doesn't work
    + #4903 [component: build] [regression] Deploy.sh needs explicit
    list of files updated
    + #4936 [component: bokehjs] Lasso select is broken with
    non-circle markers
    + #4949 Specifying a selection doesn't work with patches when hit
    testing tools are present
    + #4950 Non-deterministic ordering of css resources for external
    resource loading
    + #4960 [component: examples] Examples/models/* aren't validated
    + #4970 [API: charts] Box plot example fails if no outliers exist
    in data
    + #4984 [component: bokehjs] H_units="screen" and w_units="screen"
    not respected in imageurl
    + #4987 [notebook] [regression] Problem with 'run all' in jupyter
    notebooks with bokeh 0.12.1
    + #4992 Colorbar places axis labels incorrectly in some
    circumstances
    + #4993 Colorbar - setting outline_line_alpha=0 on plot causes bar
    to not appear
    + #4996 Labelset's text color not updating properly on changing
    column data source
    + #4998 [component: bokehjs] Typo in arrow.coffee
    + #5006 [component: docs] Remove trailing whitespace
    + #5010 Colormapping - support nan's and data lower than low
    + #5035 [component: bokehjs] Auto-range on vbar and hbar doesn't
    work
    + #5040 Rendered notebooks not working on nbviewer
    + #5056 Colorbar not working in safari
    + #5074 [component: build] [component: server] Bokeh-0.12.1-py27_0
    conda package from defaults missing server/views/app_index.html
    + #5081 [notebook] Plots do not load upon reopening a notebook if
    notebook handle created
    + #5084 Conda-build 2.0.0 doesn't build noarch packages
  * features:
    + #1441 Colorbar axis
    + #2270 [component: examples] Hide/show image layers
    + #3110 [component: bokehjs] Multi_line and selection callback
    + #4127 [component: bokehjs] Specifying external urls for
    resources
    + #4828 [component: server] Feature: make get arguments available
    for bokeh server apps
    + #4906 New feature: hide tooltip arrow
    + #4924 [component: bokehjs] Tooltips unavailable for `vbar` and
    `hbar` glyphs
    + #4961 [component: bokehjs] Don't end up with white screen under
    an unhandled exception
    + #4981 Support a colormapper as a data transform
    + #4990 Colorbar default direction should be reversed
  * tasks:
    + #3859 [component: docs] Update technical vision part of docs to
    reference new data shader repo
    + #3927 [component: tests] More gracefully handle running
    integration tests for external contributors
    + #4737 [component: examples] Spectrogram example improvements
    + #4824 [component: tests] Devdeps.py doesn't check for test
    dependencies
    + #4840 Implement quantifiedcode suggestions
    + #4869 [component: docs] [starter] User guide "responsive
    dimensions" needs updating
    + #4882 [component: bokehjs] Fixed version in version.coffee
    causes constant "version mismatch" warning
    + #4891 [component: build] Crawl and list all public functions,
    classes, methods
    + #4892 [component: build] Compare public api across versions
    + #4928 Checkbox example is not working as expected
    + #4938 [component: docs] "getting set up" section of
    documentation does not mention the base dependencies of bokeh
    + #4959 [component: tests] Imageurl example fails
    + #4976 [component: bokehjs] [component: build] Split off bokehjs
    js/ts api
    + #4989 Add colorbar public js api definition
    + #5001 [component: docs] Availability of cdn resources via https
    + #5008 Make default hover styling match other default styling
    + #5016 Remove unused reserve_val, reserve_color
    + #5042 [API: models] Disallow set type in `columndatasource.data`
    + #5061 Minor: box plot example indexing
    + #5077 [component: tests] Disable integration tests for external
    contributors
    + #5096 [component: docs] [notebook] Notebook comms and
    push_notebook docs are not up to date
- update to version 0.12.1:
  * bugfixes:
    + #1277 Syncing two input widgets without infinite callback loop
    + #1618 Toolbar buttons do not work on updating server plots
    + #1716 Help tool: hard/impossible to click "learn more" link
    + #2289 Glyph/buttons_server.py dropdown red button looking bad
    (cut) in chrome
    + #2291 [component: bokehjs] Gyphs/widget_server.py column size
    + #2488 Building the conda recipe does not work on windows
    + #3041 [component: examples] [component: tests] Scikit-learn is
    needed by examples/plotting/file/clustering.py
    + #3188 [component: build] Installing dev build through pip,
    receiving standard release instead
    + #3509 Image glyph does not work with server
    + #3639 Bokeh occasionally not working with jupyter notebook
    + #3771 Bokehjs - get_model_by_name() - multiple name error
    + #4329 [component: tests] Test defaults does not report correct
    mismatched defaults
    + #4525 Shout louder on bokehjs build fails
    + #4560 Resize tool mostly broken
    + #4679 [component: bokehjs] [webgl] Draw legend after webgl
    glyphs
    + #4692 [component: docs] Docs version dropdown has extra 0.11.1
    + #4693 [regression] Incorrect rendering of embedded bokeh server
    app in 0.12
    + #4716 [API: models] Typo in bokeh.models.tools.taptool
    `behavior` attr default
    + #4727 [component: docs] First example in quickstart missing
    output_file
    + #4730 [component: tests] [regression] Restore real flake8 test
    failure
    + #4731 [component: docs] Fix documented name for resizetool
    + #4753 [component: examples] Typo in categorical example plot
    title
    + #4759 Reset button no longer appears on gridplots
    + #4760 [component: bokehjs] Rbush 2.0.1 bug on image render
    + #4766 [component: docs] Bokeh.client example in user guide has a
    bug
    + #4781 Remove unused import
    + #4783 [component: server] Using functools.partial in combination
    with add_next_tick_callback() throws exception in py2
    + #4788 [component: docs] Stocks example github link is broken in
    gallery.rst
    + #4791 [component: docs] Docstring of "add_tools" not correct
    + #4793 [component: bokehjs] [regression] Ellipse glyph missing
    rbush bounds format update
    + #4795 [component: bokehjs] [webgl] Webgl line thickness scales
    inappropriately with browser zoom level
    + #4800 [component: bokehjs] [widgets] Multiselect not rendering
    correctly if `options` is `list(dict)`
    + #4806 [component: docs] Update add_glyph docstring
    + #4814 Add npm install to win build; add nodejs to win build deps
    + #4816 [component: docs] Docs fail to build on windows
    + #4834 [component: bokehjs] [regression] Hoover example from
    tutorials doesn't work
    + #4839 Error when using hovertool and taptool with taptool in
    "inspect" behavior
    + #4842 [component: docs] Fixes typo: "go" -> "of"
    + #4853 [layout] Hovertool does not show tooltip of last glyph
    + #4862 Wheel zoom not working on chrome on touchscreen laptops,
    when using scroll wheel
    + #4878 [component: bokehjs] Inline from bokeh.resources has
    broken js?
    + #4884 Bokehjs fails to load for inline in notebook due to
    duplicated int32array
  * features:
    + #673 Trim bokehjs size and reduce code duplication
    + #1191 [starter] Deprecate `notebook=true`
    + #1944 Bokehjs should validate values on `@set(value)`
    + #2610 [component: examples] Improve les mis example
    + #3347 Larger color ranges (particularly gray scale)
    + #3423 [API: models] [component: bokehjs] [component: examples]
    Add vbar and hbar glyphs
    + #4758 Bokeh.palettes missing qualitative brewer color maps
    + #4775 [feature] add cartodb positron tile provider
    + #4808 [component: bokehjs] [component: server] Add .patch method
    for efficient partial data source updates
    + #4866 Add visible property to glyph renderer
  * tasks:
    + #2193 [component: server] Bokeh server deployment: generic linux
    server
    + #2683 [component: bokehjs] [webgl] Our webgl support does not
    work very well on safari
    + #2933 [component: bokehjs] Use only `div` and `canvas` in the
    generated html
    + #3006 [component: tests] Conda install test dependencies for osx
    + #3008 [starter] Warn about version mismatches
    + #3078 [component: docs] Move annotations section of user guide
    into it's own page
    + #3383 [API: charts] Remove io logic from charts
    + #3511 [component: tests] [starter] Get basic tests working on
    windows
    + #3528 [component: bokehjs] [component: build] [component: tests]
    [starter] Add a test to make sure that bokeh*.js don't increase
    significantly in size
    + #4533 Run test_code_quality with flake8 group
    + #4691 [component: bokehjs] Update rbush version
    + #4701 Improve pypy compatibility
    + #4743 [component: docs] Bokeh docs heatmap example broken
    + #4755 Feature request: make tool coalescence optional in
    gridplot
    + #4779 [component: bokehjs] Jqui 1.12 breaks everything, pin to
    old version
    + #4809 [component: docs] Split interaction.rst into three
    sections
    + #4831 Revert "moved the wheel speed zoom from internal to
    defined."
    + #4845 [component: docs] Remove 0.8 and 0.9 links in docs
    dropdown
    + #4846 [component: docs] Only update cds .data "all at once" in
    docs
    + #4849 [component: docs] [starter] Docs should have descriptive
    page titles
    + #4889 [component: build] Simplify changelog
    + #4895 [component: docs] Made a couple copy edits to user guide
    pages
    + #4896 [component: docs] 0.12.1 release notes
- update to version 0.12.0:
  * Responsive layout and styling improvements throughout
  * BokehJS plotting and charts APIs for pure JS dev
  * Legends can be placed outside / next to the central plot area
  * Expanded WebGL support to all markers, fixed webgl bugs
  * New color palettes: Viridis, Magma, Inferno, and Plasma
  * New model types:
    + Arrow, Title, and Label annotations
    + LogColorMapper for scaled color mapping
    + FuncTickFormatter for simpler custom ticking
  * Support for computed transforms (e.g. Jitter) on data columns
  * Documentation improvements:
    + re-done user gude sections for layout
    + new user guide sections for JS APIs
    + new user guide sections for custom extensions
  * Server features:
    + unlocked callbacks for use with threads
    + "--num-threads" option for simpler deployment
    + new index landing page listing installed aps
  * UX improvements
    + toolbar moved to the right, and made sticky, by default
    + left aligned title, closer in, by default
    + smaller, italic axes labels
  * New hosted demos at https://demo.bokehplots.com
  * Many small bug fixes
    +
    http://googlegeodevelopers.blogspot.mx/2016/06/building-for-scale-updates-to-google.html
    + http://bokeh.pydata.org/en/latest/docs/user_guide/layout.html
    + p.title.text = "some_text"
    + session.show(plot)
  * bugfixes:
    + #1256 Vbox doesn't work properly under ie
    + #1445 Changing title on sliders example disables crosshair tool
    + #1642 Selection tools not working with scatter chart
    + #1710 [component: examples] App drop-downs under firefox are the
    wrong size
    + #1848 Tools not working on gallery - windows 7 + chrome
    40.0.2214.111 m
    + #2006 Unable to stack multiple twin axis on same side
    + #2081 Title_text_align plot property behaves strangely
    + #2229 Broken reset tool after use of resize tool
    + #2277 Matplotlib to bokeh conversion discards category labels
    + #2284 Hbox not working properly with plots
    + #2297 [starter] It's possible to extend the lasso tool outside
    the bounds of a plot
    + #2344 Appvbox: width has no effect (firefox)
    + #2350 [widgets] Hbox/hplot not working in ipython notebook
    + #2504 [widgets] Datatables spills out on server rendering (on
    ff)
    + #2525 [component: bokehjs] Setting glyph color to none results
    in an array of nan's
    + #2534 Embed.component log chart axis label messy
    + #2549 [component: docs] Dropdown button example partially hidden
    in user guide
    + #2622 [component: docs] List of color tuples broken?
    + #2699 Rendering error on line when super zoomed in
    + #2977 Stock_app errors and fixes
    + #2997 Touch problems on all but the simplest cases
    + #3004 Line tooltip appears when hovering off the line
    + #3073 [component: examples] Sliders demo uses unminified
    resources
    + #3120 Nan in data causes hover to break if formatter applied
    + #3130 Bokeh does not plot pandas boxplot correctly using
    mpl.to_bokeh()
    + #3134 When plotting pandas dataframe in ipython notebook,
    mpl.to_bokeh(), dates on axis are displayed as numbers
    + #3215 Bokeh + ipython widgets: push_notebook() error?
    + #3226 [component: bokehjs] Text_color does not respect `none`
    + #3252 Button or toggle.disabled=true does not gray out the
    button or toggle
    + #3303 Layout can allow plots to overlap
    + #3329 [component: docs] Docs suggest that add_tools() takes
    shorthand strings, but it doesn't
    + #3434 [component: bokehjs] [starter] Band fill color issue
    display
    + #3464 [component: bokehjs] Maps_cities.py data disappears after
    pan/zoom
    + #3546 [API: charts] Charts + bokeh server: scatter plot added
    twice
    + #3563 [component: bokehjs] Setting min_border does not work
    + #3576 Bokeh histogram attribute density doesn't work
    + #3581 [component: bokehjs] [component: build] Cannot find module
    _process error on bokehjs build
    + #3610 [component: examples] Embed examples and airports_map
    broken on win
    + #3611 [component: examples] Examples/plotting/file/image
    examples broken on win
    + #3612 [component: examples] Plotting/file/line_compare second
    combo ("line join") does not work on win
    + #3615 [component: examples] [component: server]
    Plotting/server/geojson broken on windows
    + #3616 [API: charts] [component: examples] Charts/timeseries
    (step) chart is broken on windows
    + #3620 Lots of warnings when using bokeh in notebook
    + #3659 [API: charts] Histogram bin size auto select
    + #3660 [API: charts] Histogram empty plot with negative values
    + #3661 [API: charts] Bar plot plotting one value
    + #3702 Handle slow callback functions (like querying a remote
    data source) when using x_range.on_change in bokeh server
    + #3774 Mpl shifting pandas boxplot
    + #3783 Reset should call the responsive resize
    + #3795 [webgl] Datetime datapoints to pile up with webgl enabled
    + #3800 [webgl] Bokeh 0.11: enables webgl causes inconsistent
    update of scatter points
    + #3830 [component: docs] Weather example readme references
    non-existent weather.py
    + #3849 [component: docs] Fix typo in docstring
    + #3850 [component: docs] Problem with formatting on docstring for
    `output_file`
    + #3871 [component: bokehjs] [widgets] Multiselect: on_change
    method does not work properly
    + #3875 [API: charts] Error with histogram
    + #3891 [component: docs] Hex rgba strings not supported in 0.11
    + #3893 [regression] Does components() in bokeh.embed work for
    widgets?
    + #3895 [component: bokehjs] [widgets] Button causing
    redirect/reload
    + #3899 Timeseries modifies a pd.dataframe inplace
    + #3915 [component: examples] Brendancol/cross filter fix
    + #3920 [component: docs] Fix typo in docs: toolbar_position ->
    toolbar_location
    + #3924 Fixed color mapper error
    + #3937 Issue while live adding new plots
    + #3943 Using vform method to generate layout can cause extra
    components to be in the document root
    + #3947 [component: docs] Contributing.md code issue
    + #3952 [component: docs] Function links not rendering
    + #3976 [component: docs] Fixed path to image
    + #3985 [component: bokehjs] Bokeh logo with gridplot
    + #3989 Sliders fail to render (they have no dimension)
    + #3992 [component: bokehjs] [notebook] Boxannotation does not
    update consistently
    + #3993 [component: bokehjs] Updating a span (line annotation)
    duplicates it
    + #3996 [component: bokehjs] Box select tool doesn't work when x
    or y range is reversed
    + #4001 [component: docs] Fix links in readme
    + #4003 [component: docs] Quickstart incorrectly states that
    default is inline - when it is cdn
    + #4012 [component: bokehjs] Jupyter notebook css is tied to the
    notebook structure
    + #4018 Fix up formatting of calendars example
    + #4027 Docserver.py is not windows compatible
    + #4034 [component: docs] Fix typo: supervisctl -> supervisorctl
    + #4035 [component: build] Npm install fails on windows
    + #4042 [API: plotting] Generalize the configuration of axes
    + #4044 Fix default bokeh dir on windows
    + #4059 Css in docs broken
    + #4069 [component: bokehjs] [regression] Line picking is broken
    because glyph.glyph_view is no more
    + #4075 When used with `stat=none`, `heatmap` modifies original
    dataframe
    + #4080 [component: bokehjs] Don't attach document multiple times
    when traversing the graph
    + #4086 [component: bokehjs] [widgets] Datatable `getformatter not
    a function` bug
    + #4090 [component: build] Build not succeeding because path
    problem looking for the noarch package
    + #4092 [component: docs] Unclear how to run bokeh command when
    exe not available
    + #4103 Update crossfilter for new typescript api spelling
    + #4104 Crossfilter example: type is not a function error
    + #4109 [component: bokehjs] [component: server] Fix function
    naming in embed.coffee
    + #4110 [component: bokehjs] [regression] Plot resizing is broken
    + #4131 [component: bokehjs] Change type of bokeh.index to
    map<view<component>>
    + #4139 Bokeh datatable renders dates one day off
    + #4155 [component: bokehjs] [regression] Fix bokehjs plotting api
    after making hasprops.set() strict
    + #4157 [component: bokehjs] [regression] Legend doesn't update
    its location after frame resize
    + #4170 [component: bokehjs] [regression] Bokehjs renders twice
    after selection
    + #4178 [component: build] Bokeh thinks site_packages is in conda
    root on windows
    + #4188 [component: bokehjs] Bokeh + flask causes race condition
    + #4190 [component: bokehjs] Toggle button reverses state
    + #4204 Bug report? datepicker widget errors on changing dates
    + #4219 [component: bokehjs] New strict js property updates broke
    datetimetickformatter
    + #4224 Extra_x_ranges should allow range not only range1d
    + #4246 Weird left toolbar in gridplots in dev build and master
    + #4248 [webgl] Line plot scaling issue when webgl is used
    + #4254 [notebook] [regression] Notebook rendering is broken
    + #4265 [regression] [webgl] Webgl broken because public props do
    not exist anymore on the glyph
    + #4275 [component: bokehjs] Remove problem styles for
    sass/autoprefixer support
    + #4278 Label doesn't accept angle property
    + #4313 Save button broken on master
    + #4318 [component: docs] Typo?
    + #4325 Bug --host '*' wildcard result in http "403: forbidden"
    error
    + #4345 [component: bokehjs] When using the browser zoom the plot
    content becomes blurry
    + #4350 Ugly border in gmapplot?
    + #4355 Problem enabling zoom on image_url object
    + #4356 [component: tests] Line hover broken in master
    + #4362 Allow unminified bokehjs to load in notebook
    + #4365 [component: examples] Simple_hdf5 example needs to use the
    full path to the data file
    + #4367 [webgl] Webgl issue on new layout with multiple plots -
    some plots are blank
    + #4379 Title.title_align='center' not working
    + #4385 Help tool is not de-duplicated in toolbarbox (gridplot
    toolbar)
    + #4390 Legend is too tall (and maybe too wide) if more than two
    items
    + #4401 Trigger event when bokeh finishes rendering
    + #4432 [component: bokehjs] Js property mismatches
    + #4435 Chord diagram only has one color when using python 2.7
    + #4439 Multiple renders ocurring
    + #4464 Setting title_text_font_size with title='' errors
    + #4488 [component: bokehjs] [regression] Plots are rerendered on
    resize even if responsive="fixed"
    + #4498 Dropdown type undefined
    + #4501 Gapminder css issue
    + #4506 Re-rendering widgets in a notebook fails miserably (when
    they're in a widgetbox)
    + #4513 Jitter import missing, affecting pr #4490
    + #4530 [component: docs] Link to css colors in docs is broken,
    link address changed
    + #4537 Scale_both isn't quite working right
    + #4541 [component: examples] Clustering app example needs updates
    for recent changes
    + #4543 Movies example has sliders under plot
    + #4554 Layouts got slightly broken during sizing_mode change
    + #4569 [notebook] [regression] Logo missing from notebook
    resource load
    + #4572 [component: bokehjs] [widgets] Changing a toggle button's
    type is broken
    + #4578 Gridplot toolbar broken
    + #4581 Gridplots broken except for fixed
    + #4583 Using gridplot now gives a warning
    + #4587 [component: bokehjs] [component: server] Title js models
    sending bck properties not on python side
    + #4589 [component: examples] [regression] Spectrogram example
    needs fixing up
    + #4601 Toggle button layout broken w/ new widgetbox
    + #4603 [component: examples] Ajax data source needs to specify
    columns explicitly
    + #4606 Toolbar alignment on complex layouts
    + #4611 [regression] Plots disappear after zooming in/out in some
    browsers
    + #4614 Reset tool does not trigger x/y_range callback events
    + #4622 [component: bokehjs] [regression] Lod downsampling is not
    working
    + #4633 Taptool on line glyph with webgl=true causes renderers to
    disappears
    + #4636 Textinput not obeying width parameter
    + #4639 Divide by zero error in logcolormapper
    + #4658 Google maps no longer working due to api update?
    + #4663 Dropdown callbacks broken
    + #4666 Call to reset breaks layouts
    + #4672 Charts heatmap uses deprecated attribute internally
  * features:
    + #149 Allow plot titles to be located on any edge of the plot
    + (not just the top)
    + #219 Preview save tool should auto download-prompt
    + #572 Support for pan/zoom range limits
    + #713 Adding legends through the js interface
    + #844 [API: charts] Add chord chart
    + #1085 [starter] Orientation on titles
    + #2026 [component: server] Allow bokeh server scripts to take
    command-line arguments
    + #2583 [starter] Can't serialize timedelta column
    + #2715 [component: bokehjs] [widgets] Can't add callbacks to
    checkboxgroups
    + #2865 Off-canvas legends
    + #2992 [API: charts] Step chart should have 'index
    + #2995 Reset doesn't reset selections?
    + #3054 [starter] Toolbar improvements: active is programmable
    + #3217 [component: docs] Build documentation with canonical links
    to "latest"
    + #3346 Slider size from python code to css
    + #3493 [starter] Collections.deque should serlialize
    + #3515 Having a __conda_version__.py under bokeh causes version
    to be wrong
    + #3738 [component: bokehjs] [component: server] Add support for
    bokeh static command
    + #3822 Improved annotations and legends
    + #3825 [API: models] Computed transforms
    + #3829 Add stamen toner background tile provider
    + #3832 Support horizontal legend orientations
    + #3846 [component: bokehjs] Real properties for bokehjs
    + #3848 Oval with height=width does not produce a circle
    + #3881 Add support for geojson geometrycollection
    + #3957 [component: bokehjs] [widgets] Delayed update slider
    + #3962 Custom web templates with `bokeh serve`
    + #3994 [component: server] Add option to extend sys.path with app
    directory
    + #4008 Allow for the injection of raw html code
    + #4051 --host whitelist doesn't trust 127.0.0.1 by default
    + #4057 [API: charts] Request: reorderable legends with chart api
    + #4064 [component: bokehjs] [component: examples] Add stock
    example using ts api
    + #4065 [component: bokehjs] The box (zoom or select) tool should
    be configurable to respect aspect
    + #4077 Avoid copies in columndatasource.stream
    + #4082 Expose geometries to taptool callbacks
    + #4118 [component: examples] Add implicit filename support for
    save()
    + #4150 [component: server] App-specific static file serving for
    directory apps
    + #4164 Improving bokeh's layout
    + #4179 Small improvements to label
    + #4180 Set default width and height for markup widgets to none
    + #4184 [component: bokehjs] Expose {x,y}axis in ts plotting api
    + #4201 [component: bokehjs] Make reset tool configurable as to
    what is reset
    + #4205 [component: bokehjs] Add the computedtransforms to the
    dataspec system
    + #4206 [component: examples] Add example for customjs callback
    for exporting columndatasource to csv
    + #4261 There should be an actual click tool
    + #4307 New title api & implementation
    + #4311 [API: charts] [component: bokehjs] Create js/ts charts api
    + #4344 [API: charts] Timeseries not correclty represent x-axis
    when applied to dataframe with datetime index
    + #4363 Bokeh server w/ multiple processes
    + #4372 Logcolormapper?
    + #4373 Add callback support to lassoselecttool
    + #4380 Titles should align with the edge of the frame not the
    edge of the canvas
    + #4384 New layout api - bokeh.layouts - layout, row, column,
    gridplot
    + #4412 [component: server] [starter] Redirect from `/` to
    `/app_name`
    + #4425 Improve server index page
    + #4462 Adding a funcformatter for ticks based on pyscript
    + #4548 [component: bokehjs] Add viridis and other new color maps
  * tasks:
    + #861 Clean up top level directories
    + #1149 [component: build] Build_and_upload.sh needs improvements
    + #1268 [component: docs] Bokeh.plotting.image_url glyph is
    missing width and height parameters in the documentation
    + #1455 Move all base64 encoded images to *.less files
    + #1595 Streaming stock ticker demo
    + #2239 [component: docs] [starter] Docs for styling selection
    overlays
    + #2657 Bokehjs: imageurl glyphrenderer improvements
    + #2752 [component: tests] Selenium tests to do
    + #2759 [component: bokehjs] [starter] Resolve misleading property
    names in `bokeh.index[<item_id>].renderers` and
    `bokeh.index[<item_id>].model.renderers`
    + #2876 [component: examples] [starter] Example embed_multiple.py
    is using old static links
    + #2882 [starter] Allow local resources when building docs
    + #2888 Something in bokeh.util.testing.py breaks making the docs
    + #2897 Ci error on current master (404/410 error with ggplot
    example notebook)
    + #2922 [component: bokehjs] Use numbro.js instead of numeral.js
    for formatting numbers
    + #3014 [API: charts] Pandas sort deprecated in new charts, use
    sort_values instead
    + #3083 [starter] Remove logo_url from resources
    + #3084 [component: docs] Update docs to point to tagged release
    of bokeh examples
    + #3146 Document breaks with roots that are also in non-root
    layouts
    + #3232 [component: tests] Screenshot testing for selenium tests
    + #3390 Known pending issues/tasks for 0.11 release
    + #3514 [starter] Rename bokeh.client.connection
    + #3571 Missing bokeh entry point (otherwise bokeh.bat) for
    windows
    + #3575 [component: server] Bokeh server should display bokeh
    version on startup
    + #3582 [component: docs] [component: server] Embed docs out of
    date
    + #3586 [component: examples] [component: server] Crossfilter
    example refactor
    + #3651 Unifying bokeh and bokehjs project structure
    + #3675 Defining a js callback using python for python 2.x
    + #3730 Difference between public and internal session lifetime
    units
    + #3759 [component: docs] Quickstart edits
    + #3770 [component: server] Periodic callbacks continue after tabs
    are closed
    + #3784 Responsive is false by default, no need to set
    + #3797 [component: bokehjs] Containing all bokeh style to
    .bk-plot
    + #3826 Visual diff tests
    + #3827 Cross browser automated testing
    + #3844 [component: docs] Remove quickstart
    + #3864 [component: bokehjs] Clean bokehjs cruft
    + #3868 Remove leftover comment from when examples were disabled
    + #3869 Test with firefox on saucelabs
    + #3877 [API: models] Pyscript now also works on py27
    + #3889 [component: tests] Speed up examples tests by using
    pytest-xdist
    + #3908 [API: charts] Add xaxis, yaxis accessors to chart class
    + #3913 [component: bokehjs] Some canvas and layout improvements
    + #3927 [component: tests] More gracefully handle running
    integration tests for external contributors
    + #3936 [component: docs] Creating -> create
    + #3938 [component: bokehjs] Changed .bk-plot to .bk-root for
    style wrapper
    + #3945 Demo more prominant report location
    + #3948 [component: docs] Concepts file changes [ci disable
    examples]
    + #3949 [component: docs] Remove duplicate of seaborn from req'd
    pkgs [ci disable examples]
    + #3950 [component: docs] Fixes to 'plotting' [ci disable
    examples]
    + #3951 [component: docs] Add links to more external libraries
    + #3955 [component: build] Noarch conda package and entry points
    + #3963 Revert "changed .bk-plot to .bk-root for style wrapper"
    + #3968 [component: docs] Document usage of a reverse tunnel to an
    instance of a standalone server
    + #3970 Disable data_tables_server example
    + #3997 [component: docs] Issue #3656: added more documentation
    for how to use widgets in the user guide
    + #4029 [component: docs] Fix output_notebook(resources) default
    docstring
    + #4037 [API: plotting] [component: bokehjs] Implementation of
    typescript api
    + #4063 [component: tests] Pytest consistently erroring on logging
    + #4076 [component: bokehjs] [component: docs] In developer guide,
    it's not obvious that "following pages" are indexed in the
    sidebar on the left
    + #4078 [component: bokehjs] Remove support for backbone
    collections
    + #4085 [component: bokehjs] More typescript api
    + #4087 [component: build] Anaconda auth token got staled
    + #4099 [component: build] [component: tests] Fix phantomjs
    download failures
    + #4100 [component: docs] [starter] Add prominent banner to old
    versions of the docs
    + #4101 Head breaks apps that use widgets with type parameter
    + #4116 [component: examples] [component: server] Add a simple app
    showing usage with hdf5
    + #4119 [component: build] Try use setuptools in setup.py (so
    entry points get installed on windows)
    + #4122 [component: docs] [starter] Add new div widget example to
    user guide
    + #4124 [component: bokehjs] Remove obsolete css classes and
    bokehjs/src/templates
    + #4126 Release 0.12 planning
    + #4132 Hotfix - fix path to phantomjs executable
    + #4141 Declarative property management
    + #4149 [component: server] [starter] Log pid on server startup
    + #4159 [component: bokehjs] [component: examples] Add linked
    plotting example to bokehjs
    + #4168 [component: tests] Apply basic code quality rules to all
    source files
    + #4173 [component: docs] There is no make.bat serve to view
    locally build docs on windows
    + #4186 [component: docs] [starter] Need docs support for bokehjs
    widgets split
    + #4187 [component: docs] [starter] Document "bokeh sampledata"
    better
    + #4194 [component: tests] Disable pandas_dataframe test
    temporarily
    + #4195 [component: tests] Restore pandas_dataframe test
    + #4210 [component: bokehjs] [component: build] Built js and css
    not included in npm package
    + #4212 More ts api improvements
    + #4217 Add paragraph and pretext widgets to user guide
    + #4222 [component: examples] Remove or update accidentally
    committed template
    + #4230 [component: docs] Document how to run screenshot tests
    + #4234 [API: charts] [component: docs] Better docs for the chord
    chart
    + #4242 [component: docs] [component: server] Document use of
    bokeh server with apache
    + #4244 [component: examples] Add example with drawing networkx
    graphs
    + #4251 [component: tests] Jitter tests can fail
    + #4253 [component: docs] [component: tests] Add note to testing
    docs about installing bokeh
    + #4267 [component: docs] User guide adding annotations uses
    p.renderers.extend instead of p.add_layout
    + #4279 [component: tests] [webgl] Tests for webgl
    + #4281 It at all -> if at all
    + #4292 Add webgl support for more kinds of markers
    + #4293 [webgl] Webgl blurry on os x, not visible in safari
    + #4323 Move plot to plotcanvas
    + #4341 Refactor webgl into smaller chunks
    + #4358 Revert "make hidpi work for webgl"
    + #4360 Merges the hipdi work into the layout pr
    + #4381 Api issue: title_standoff, title_padding, title_offset
    + #4382 Is title padding working?
    + #4383 Is min_border working?
    + #4387 [component: docs] Layout documentation
    + #4396 Api - name the responsive modes
    + #4397 Update all examples to use new layouts
    + #4399 [API: models] Make toolbar right by default?
    + #4406 Confirm that toolbar works under streaming (ref #3334)
    + #4423 Changed docserver shutdown instruction
    + #4429 [component: examples] #4397 (partial) examples/models
    update layout
    + #4440 [component: docs] Update readme for greater user
    friendliness
    + #4446 [component: docs] Improve dev guide's documentation
    section
    + #4454 Doc: mentioning "ulimit -n" in dev guide
    + #4457 [component: docs] Explicitly document installing into the
    bokehjs directory
    + #4466 [component: docs] Remove deprecated api usage from docs
    examples
    + #4475 Remove dupe props in plotcanvas, cleanup
    + #4480 [component: build] Unnecessary ansi escapes are generated
    by setup on windows
    + #4482 Quiet boto log level
    + #4485 [component: docs] Update docs and docs build to be clear
    that only html output is supported
    + #4492 Tweaks to almar's resize pr
    + #4494 Remove un-used layout css
    + #4496 Undeprecate vbox and hbox
    + #4512 A few fixes to the typings
    + #4514 Split out responsive and sizing_mode as per discussion on
    [#4484]
    + #4515 [component: tests] Cannot run test_code_quality.py on
    windows
    + #4520 Resize tool should not be in defaults
    + #4529 Update docs
    + #4547 [component: docs] [starter] Readme.md under
    examples/plotting/notebook refers to ipython not jupyter
    + #4550 Warn when sticky toolbars might visually overlap other
    components
    + #4557 Improvements to layout functions
    + #4559 [component: examples] Ggplot api update
    + #4566 Pin ggplot version preceding uploading new versions to
    anaconda.org
    + #4584 Set gridplot default location to above
    + #4591 [component: examples] Add surface3d custom model example
    + #4594 Issue with pandas in examples/app/weather
    + #4609 Remove hack unneeded since #4607 introduced in #4312
    + #4620 Responsive no longer supported?
    + #4626 Mpl compat needs minor updates
    + #4629 Small styling tweaks
    + #4654 Examples tweaks
    + #4655 Skip 3 more flaky js tests
    + #4662 Examples cleanup
    + #4669 [component: docs] Arrowhead documentation
    + #4670 Clean up notebook examples
    + #4675 Undeprecate .from_df
    + #4684 Code quality
    + #4685 [component: examples] Bryanv/hotfix examples
    + #4687 [component: docs] Last docs 012
- update to version 0.11.1:
  * settings and documentation for Bokeh server behind an SSL
    terminated proxy
  * bugfixes:
    + MultiSelect works
    + Oval legend renders correctly
    + Plot title orientation setting works
    + Annulus glyph works on IE/Edge
  * features:
    + preview of new streaming API in OHLC demo
    + undo/redo tool add, reset tool now resets plot size
    + "bokeh static" and "bokeh sampledata" commands
    + can now create Bokeh apps directly from Jupyter Notebooks
    + headers and content type now configurable on AjaxDataSource
    + Range update callbacks now return the range object as cb_obj
    (not the plot)
    + Layouts (HBox, VBox, VBoxForm) have been moved from
    bokeh.models.widgets to bokeh.models.layouts, but continue to be
    importable from bokeh.models
    + BlazeDataSource has been removed; it will be maintained by the
    Blaze team in the future.
    + The broken BokehJS API has been removed. We are actively seeking
    a champion/maintainer for a new BokehJS API.
  * bugfixes:
    + #2495 [widgets] Multiselect appears broken
    + #3055 [docs] Search isn't working correctly on docs -
    bokeh.pydata.org
    + #3069 [docs] Table of contents is not scrolling properly on
    bokeh website
    + #3173 Cb_obj for range callback is plot not range
    + #3257 Confusing deprecation message in bokeh/models/plots.py
    + #3304 [examples] Stocks app example is not py2 compatible
    + #3468 [bokehjs] Embed_responsive_with_height.py starts out wrong
    size
    + #3530 _make_io_complainer method of scripthandler uses
    not-imported sys module
    + #3543 [bokehjs] Annulus glyph does not render correctly in ie
    and edge
    + #3552 Use self.mode instead of mode in baseresources.__init__()
    + #3562 [docs] Python callback example in user guide not rendering
    + #3569 [docs] Imageurl example in reference guide is broken
    + #3578 [charts] [docs] Sizing plots, charts: inconsistency
    between doc an api
    + #3591 [docs] Correct links to be demo.bokehplots.com links
    + #3604 [bokehjs] Hovertool.always_active is not implemented
    + #3605 [bokehjs] Webgl aa is broken on firefox on windows
    + #3626 [bokehjs] [server] Support swapping of axes/ranges without
    re-creating entire plot
    + #3636 [tests] Travisci failing every py27 examples test
    + #3646 Fix bad path to bokeh logo static
    + #3658 Hplot spacing too large
    + #3680 [bokehjs] Notebook comms only update last plot
    + #3683 Movies app razzies file path
    + #3690 Add `bind_bokeh_event` methods to `tilerenderer` and
    `dynamicimagerenderer`
    + #3692 [server] Fix error about blocked websocket to list allowed
    origins
    + #3695 [docs] Server example out of date
    + #3698 [docs] Doc: data_source is not an expected attribute to
    text
    + #3699 [charts] Boxplot 1st and 4th whiskers are just of equal
    length
    + #3705 Inline css from embed_multiple.py jinja template overrides
    bokeh plot icon css
    + #3709 [bokehjs] Issue with legend when 'oval shape' is used
    + #3710 [bokehjs] [build] Restore support for --build-dir argument
    to gulp
    + #3711 [bokehjs] Allow to align plot title to left and right
    (center worked before)
    + #3712 [regression] Use make_id() instead of str(uuid.uuid4())
    + #3714 [regression] Restore pretty json formatting and make
    sort_keys=true the default
    + #3726 [server] Pandas required to use the server!
    + #3727 [examples] Update elements.csv
    + #3753 [bokehjs] Should not set parent on anything anymore
    + #3758 Fix bad layouts imports in examples
    + #3769 [bokehjs] Reset tool resets selection incorrectly
    + #3778 Fix issue with bar chart grouping/stacking order
    + #3803 [bokehjs] Publish bokehjs separately in a notebook to
    avoid parsing issues in jquery
    + #3807 [docs] Sync mpl.to_bokeh docstrings with current available
    parameters
    + #3811 [bokehjs] Hot fix for selection reset code
    + #3812 Use import_required for nbformat and nbconvert
  * features:
    + #1683 Reset orignal plot's size
    + #2346 [bokehjs] Extend jscallback support
    + #3254 Add support for undo and redo tools
    + #3505 "bokeh sampledata" command
    + #3506 [starter] "bokeh static" command
    + #3541 [server] Add session expiration time options to `bokeh
    serve`
    + #3542 Log more detailed stats information from the server
    + #3553 [server] Add __main__.py so we can do "python -m bokeh"
    + #3592 [docs] Add a sitemap builder
    + #3593 [server] Add option to parse jupyter notebooks as input to
    bokeh command
    + #3638 [server] Provide method for turning server autoadd off
    + #3682 Add headers and contenttype configuration to ajax data
    source
    + #3768 Initial commit of streaming api
  * tasks:
    + #2159 [docs] [server] Bokeh server documentation is incomplete
    + #3243 [tests] Build new pytest-selenium package
    + #3305 [server] Evaluate bokeh server on windows
    + #3404 [docs] Todos for new docs
    + #3417 [charts] [examples] Add detailed tutorial on individual
    charts components
    + #3508 Remove remotedata directory
    + #3548 [tests] Latest versions of firefox have a heavy to load
    startpage that we don't need
    + #3566 Remove bokeh/styling_tool_overlays.html
    + #3568 Use split not contains for browser compatibility
    + #3583 [docs] Remove some example notebooks that are superfluous
    + #3587 Add plotting of razzies
    + #3588 [docs] Quick add of demo apps to gallery
    + #3599 [examples] Update periodic table example to reflect recent
    changes
    + #3607 [build] Add javascript channel to meta.yaml and improve
    scripts/dev_environment
    + #3633 [docs] User guide server
    + #3637 [docs] 0.11.0 documentation fixes and flake8
    + #3662 [bokehjs] Remove hasparent (involves moving glyph
    display_defaults into defaults)
    + #3663 Remove abstractrendering cruft
    + #3664 [docs] Examples reorg
    + #3672 [bokehjs] Fix base of bokehjs class hierarchy
    + #3676 [build] Minified files should not try to load .map files
    + #3677 Server should optionally enable xheader support
    + #3686 [docs] Auto-update the "releases" link in conf.py
    + #3687 [docs] Docs updates/0.11.0
    + #3694 Remove not filled out portions of docs
    + #3697 Add renderer base class to *_renderer models
    + #3703 Task/add component base class
    + #3721 [docs] Hotfix small doc addition to select
    + #3728 Removed rogue debugger statement
    + #3735 [bokehjs] [models] Task/3651 unify directory structure
    + #3739 [build] [tests] Remove version pin from pytest-selenium
    + #3742 [docs] Reference docs have bad path to layouts.py
    (autodocs fail for layouts)
    + #3749 [bokehjs] Move defaults.coffee (for models and widgets)
    into test/ directory
    + #3751 [bokehjs] Remove unused close_wrapper module and
    coffee/api directory
    + #3752 [bokehjs] [build] Generate defaults for test task, not
    scripts:coffee
    + #3755 [docs] Quickstart edits
    + #3766 [bokehjs] Task/rename hasproperties to hasprops
    + #3775 Removing blazedatasource
    + #3790 Don't use spaces in json separators to reduce data size
    + #3802 [bokehjs] Move vbox and hbox to top since they are layouts
    on coffee layer
    + #3805 [build] Add new creds for rackspace
    + #3808 [docs] Fix quotes around links to examples notebooks
    + #3815 Hotfix/apps examples
* Fri Feb 26 2016 tbechtold@suse.com
- Require python-python-dateutil. package was renamed
* Mon Jan 11 2016 toddrme2178@gmail.com
- Update to 0.11.0
  * New Tornado and websocket-based Bokeh Server
  * User-Defined Models allowing anyone to extend Bokeh
  * GeoJSON data source and map tiles renderer
  * WebGL support for rendering lines
  * Python -> JS compilation for CustomJS callbacks
    (Py3 only for now)
  * New general push_notebook() based on Jupyter comms
  * Updates to charts
  * UX improvements
  * Known issues
  * many small bug fixes
- Update to 0.10.0
  * Initial webgl support (check our new examples: maps city,
    iris blend, scatter 10K, clustering.py)
  * New charts interface supporting aggregation
    (see our new Bars, BoxPlot, Histogram and Scatter examples)
  * Responsive plots
  * Lower-level jsresources & cssresources
    (allow more subtle usesof resources)
  * Several test machinery fixes
  * Several build machinery enhancements
  * More pytest-related fixes and enhancements
  * More docs fixes and enhancements
  * Now the glyph methods return the glyph renderer (not the plot)
  * Gmap points moves consistently
  * Added alpha control for imageurl objects
  * Removed python33 testing and packaging
  * Removed multiuserblazeserver
- Update to 0.9.3
  * Support horizontal or vertical spans
  * Provide raw_components version of bokeh.embed.components
  * Prevent Bokeh from eating scroll events if wheel tool is
    not active
  * bokeh.models.actions are now called bokeh.models.callbacks and
    Callback is now CustomJS
  * Additional validation warnings
  * Cleaned up gulp source mapping
  * Fixes in our build machinery
  * Cleaned up models section of the reference guide
  * Use pytest instead of nose
  * Beginning to add selenium tests
* Mon Jul 27 2015 toddrme2178@gmail.com
- Update to 0.9.2:
  * Several nan-related fixes including the slow rendering of plots
  * Removed some unused dependencies
  * Fixes in our automated release process
  * Fixed the patchs vanishing on selection
  * More control over ticks and gridlines
  * MPL compatibility updated
  * Several examples updated
  * bugfixes:
  - #735 Inconsistent conversion of np.nan to json data in bokehjs
  - #1005 Nan in data source column causes problem with glyph interface
  - #1039 Bokeh server can display an empty document without any visible errors
  - #1075 [tests] Test failure if websocket client is not installed
  - #1139 Hover tool swaps sides at an off-center position
  - #1176 Session.store_document() fails in table_server example
  - #1264 Stock app fails to refresh after drop down is updated
  - #1381 Fill_color argument doesn't handle rgb(a) tuples properly
  - #2513 Fix release script failures
  - #2514 Bug: all patches vanish on selection
  - #2524 Setting a fixed font size value as a string is deprecated warnings
  - #2529 [docs] Internal server error on quickstart
  - #2582 [bokehjs] [regression] Slow plot rendering for 0.9.1
  - #2586 [bokehjs] Decimated glyph needs visuals set also
  - #2593 [docs] Fix typo in charts user guide
  - #2600 [bokehjs] Hotfix/fixed ticker
  * features:
  - #194 [widgets] Widget/controls integration
  - #2379 Get a warning about an invalid column name
  - #2496 Improve mouseover information in texas example
  - #2548 [bokehjs] Need more control over ticks and gridlines
  * tasks:
  - #2441 Warning when instantiating plot with no arguments
  - #2540 Add console warning when bokeh-plot fails
  - #2541 [docs] Breaking out inline plot examples in user guide into files
  - #2543 Mpl update
  - #2546 Clean up examples, use standard bokeh.io output
  - #2547 [docs] Fix typo in components deprecation message
  - #2554 [branches] Fix bug on ie (avoid using indices)
  - #2577 [docs] Editing up to concepts
  - #2598 Serializing data with numpy optional
  - #2605 Hotfixes 0.9.2
* Fri Jul 10 2015 toddrme2178@gmail.com
- Update to 0.9.1
  * New callbacks options for hover, selection, and range updates
  * Documentation for widgets and new callbacks in the User's Guide
  * Much more flexible embed.components that can embed multiple objects
  * Implemented a validation framework to provide errors and warnings
  * More than 30 smaller bugfixes
  * bugfixes:
  - #1254 [docs] Setting small plot_width or plot_height to categorical plot without min_border
  - #1255 [docs] Bokeh.embed.components second parameter not optional
  - #1926 [docs] Tap_select tool is actually tap
  - #2040 Expose level parameter in python
  - #2161 Color tuples not supported
  - #2176 Fix error: unable to parse uri to data
  - #2245 Bokeh-server --url-prefix is being ignored
  - #2282 [starter] [tests] Testmatrix script not in sync with bep 2
  - #2303 [build] Tagging on release produce wrong names in binstar packages
  - #2306 [bokehjs] [regression] Fix issues preventing bokehjs 0.9 working on jsfiddle site
  - #2311 [bokehjs] [docs] Broken link to help pages from bokeh plots
  - #2316 Text glyph font size from columndatasource field not working in 0.9
  - #2329 Diamond/diamondcross both show diamonds
  - #2336 [docs] Categorial heatmap gallery example missing (bad path)
  - #2338 Valueerror: min() arg is an empty sequence
  - #2356 [bokehjs] Force glyphs to always beginpath before rendering
  - #2357 Crosshairtool lacks "dimension" property
  - #2359 [docs] Animated line and animated glyph gallery examples are broken
  - #2365 [examples] Compat/seaborn/sinerror.py is broken
  - #2366 Patches doesn't render with reversed ranges
  - #2376 Hover on discontinuous patches
  - #2396 [bokehjs] [docs] Tools seems to be broken in latest version of chrome and chromium
  - #2416 Datetime scalar transformation loss of resolution
  - #2431 Datarange1d start and end bug
  - #2436 Bokeh jquery overriding previously loaded jquery
  - #2445 Prevent non-compliant json generation
  - #2459 Hotfix for components
  - #2478 [examples] Pin seaborn version
  - #2482 Deactivate tests before building to avoid huge packages
  - #2484 Use the correct extension
  - #2498 Use bokeh's jquery for server template
  * features:
  - #602 Add object integrity validation
  - #1727 Add categorical y axis
  - #1754 `to_bokeh` ignores alpha
  - #1873 [docs] Palette argument for charts not well documented
  - #1960 Throw exception if nonexistent keyword arguments are given
  - #2100 Fix handling of initial columns in crossfilter
  - #2213 Feature: bokeh-server with https enabled
  - #2335 Tab completion for splattable lists
  - #2348 Extend embed.component to let multiple objects be rendered in multiple divs
  - #2354 Add support for `styles` in google map `map_options`
  - #2368 [bokehjs] Minor grid lines
  - #2371 [docs] Add mailing list to gmane
  - #2390 [examples] Slider demo - animated bubble
  - #2410 Allow users to specify jinja2 template variables
  - #2411 Task/add range update callback
  - #2465 Callback for box selection tool
  * tasks:
  - #850 [docs] Clarify how axes can be labelled
  - #853 [docs] Widget documentation
  - #2234 [bokehjs] Better bokehjs debug mode
  - #2293 [docs] [starter] Update bep2 install instructions
  - #2302 Updating bokeh server image
  - #2305 [docs] Server section on user guide
  - #2308 [build] [docs] Improve some tooling around version reporting
  - #2309 [docs] User guide improvements/typo corrections
  - #2313 [docs] Sampledata.download() defaults to home directory
  - #2320 Remove extra whitespace
  - #2322 [docs] [doc] changed `tap_select` to `tap`
  - #2337 [docs] Change binstar.org references to anaconda.org references
  - #2342 [build] Remove sbt-based build system
  - #2343 [docs] Keep output html filename consistent with exercise name
  - #2358 [examples] Added palettes example to gallery
  - #2400 [branches] Extend embed.component to let multiple objects be rendered in multiple divs
  - #2403 [branches] Added test, improved conditionals
  - #2404 [branches] Added error prompt wth message
  - #2406 [branches] Added document support alongside plotobject
  - #2407 [branches] Line too long
  - #2412 [bokehjs] Standardize callback interface with args
  - #2420 Build enhancements
  - #2421 Quasi-complete automation
  - #2433 Spectrogram improvements
  - #2440 Allow gridplot.select uses name & type paramters
  - #2457 [examples] Add example plotting widget with play stop
  - #2477 Add hovertool callback examples
  - #2481 [docs] Open docs pr for 0.9.1 release
  - #2483 [examples] Open pr for small example (only) updates for 0.9.1
  - #2485 Elide some unnecessary checks for map plots
  - #2510 [docs] Add 0.9.1 release highlights
  - #2511 Revert some automated commits
- Changelog from previous 0.9.0 update:
  * Callback Action, serverless interactivity in static plots
  * Hover inspection along lines
  * Client side LOD downsampling for interactive tools
  * Full User guide rewrite
  * Reduce BokehJS boilerplate and switch to use browserify
  * Several example bugfixes
  * bugfixes:
  - #746 Grid without axis?
  - #1479 Indicator of stacked hover tooltip has vertical offset
  - #1599 Glyph renderer not masking data before rendering
  - #2066 Angle property not working for square glyph
  - #2095 Examples/glyphs/data_tables.ipynb error
  - #2105 Release_update.sh is generating a superfluous "id" package
  - #2119 Simpleapp broken
  - #2124 Stock_app_simple.py does not respond to 2. change on the
    dropdown field
  - #2128 [examples] Simpleapp stock demo histograms not updating on
    selection
  - #2130 [docs] Fixed typo in documentation
  - #2134 Selections not working with nominal/categorical axis
  - #2153 [docs] Fix typo, example has two css, one should be js
  - #2158 [charts] Color cycles for bokeh charts
  - #2180 Add shrinkwrap to lock to versions and upgrade jsdom
  - #2217 [regression] Selection_histogram example broken after new
    hit_test redesign
  - #2228 [docs] Update quickstart.rst
  - #2231 [bokehjs] Multiselect broken
  - #2233 [bokehjs] [regression] Vboxform broken
  - #2238 Avoid layout breaking when simpleapp managing buttons
  - #2246 [regression] Update datarange1d that wasn't updated on
    notebook after last api change
  - #2253 Run binstar upload in the correct 'scripts' location
  - #2256 Use another env variable is case of weird previous use of
    the i var
  - #2258 Pin binstar until binstar build fix the platform path
    problem
  - #2261 [docs] Fix two small typos
  - #2262 [bokehjs] Direction is not being passed to draw_legend in
    annular wedge, arc, and wedge
  - #2269 [bokehjs] [regression] Hbox/hplot broken
  - #2278 Examples failures
  - #2280 [docs] Doc: grammar fix for intro to models
  * features:
  - #351 Cycle colors for plots
  - #1486 Add line hit testing and hover inspection along lines
  - #1517 Change datarange objects to query renderers for preferred
    bounds
  - #1519 [starter] Add simple lod downsampling on the client side
  - #2098 Decimal.decimal cannot be sent across session
  - #2112 Remove as much of src/vendor as is practical
  - #2137 Move data sources on to glyphrenderers
  - #2140 [bokehjs] [build] Streamline bokehjs build in develop mode
  - #2151 [docs] Add cdn links in embedding docs
  - #2156 Add an option to remove the `help` button of the bokeh
    toolbar
  - #2174 Simple callback action
  - #2178 Add a "callback" to a source.selected event
  - #2185 Allow users to specify a desired number of ticks
  - #2207 [docs] User guide rewrite
  - #2275 [examples] Initial commit of color_sliders.py
  * tasks:
  - #1751 Remove pinned packages
  - #2038 [bokehjs] [build] What is the best way to develop bokehjs
    with incremental rebuilds?
  - #2078 [tests] Use pyflakes
  - #2087 Simplifying glyph units
  - #2106 Setup.py build message improvements
  - #2126 [examples] Update selection histogram example
  - #2132 Reduce bokehjs boilerplate
  - #2139 [docs] Updating exercises to match current master
  - #2146 Automatic devel build only in py27 in the new travisci
    matrix
  - #2168 Remove extraneous comma from unemployment csv
  - #2196 Bokehjs install failing because dependencies source
    doesn't exist
  - #2211 [bokehjs] [regression] Make relative dev work again
  - #2224 Make a script to check for dev and docs dependencies
  - #2237 [docs] Update readme.md
  - #2241 [build] Obsolete protocole sslv3
  - #2254 Revert "run binstar upload in the correct 'scripts'
    location"
  - #2257 Follow-on for user guide
  - #2285 Setup.py: note that this also works with `develop`
  - #2296 Remove '*' imports from examples
  - #2298 [tests] Add info in the warn message about some missing
    dependecies
* Sun May 24 2015 toddrme2178@gmail.com
- Update to version 0.9.0
  * No upstream changelog
* Mon Mar  2 2015 toddrme2178@gmail.com
- Update to version 0.8.1
  * Fixed HoverTool
  * Fixed Abstract rendering implementationa and docs
  * Fixed chart gallery and docs
  * Removed leftovers from the old plotting API implementation
  * Some other minor docs fixes
  * bugfixes:
  - #1801 Bokeh server crashing when reloading flask app
  - #1909 Make tooltips properly centered on data points
  - #1910 [docs] [examples] Fix charts gallery
  - #1914 Remove spurious curplot
  - #1918 Nameerror: name 'jsbuild' is not defined
  - #1920 [regression] Examples/plotting/file/hover.py broken after 0.8 release
  - #1921 [docs] [regression] Tutorial gallery is broken
  - #1922 [examples] App_reveal fails importing old plotting stuff
  - #1925 [docs] Docs error in chart section
  - #1933 [docs] Bokeh glyph quick reference 404 (docs)
  - #1940 Spectrogram needs updating to use figure()
  - #1943 `publishing` example from the `embed` directory fails
  - #1945 [docs] More broken doc links
  - #1946 [docs] Fix charts on userguide showing old functionality
  - #1963 Feature/fix ar zoom
  * features:
  - #899 [docs] Hosted server examples in the gallery
  - #1929 [starter] Image glyph method should have a default palette
  * tasks:
  - #1731 [docs] Add a section about bokeh-scala/bokeh.jl/... to main documentation
  - #1905 Better error messages for blaze version mismatch
  - #1908 Release 0.8.0
  - #1962 Hot fixes for examples
- Update to version 0.8.0:
  * New and updated language bindings: R, JavaScript, Julia, Scala, and Lua now available
  * Better bokeh-server experience:
  - live gallery for server apps and examples!
  - new "publish" mode Bokeh plots and apps
  - docs and advice for real-world deployments
  * Simpler and more easily extensible charts architecture, with new Horizon chart
  * Dramatic build and documentation improvements:
  - 100%% complete reference guide
  - full docs and BokehJS version deployed for every "dev" build and RC
  - sphinx extensions for easy inline plots
  * Shaded grid bands, configurable hover tool, and pan/zoom for categorical plots
  * Improved and more robust crossfilter
  * AjaxDataSource for clients to stream data without a Bokeh server
  * bugfixes:
  - #165 May need to dilate canvas 1px
  - #766 Resize handle offset when there are axis labels
  - #833 Screen units for x,y
  - #1221 Call to `show()` not displaying figure in ipython notebook
  - #1286 Decouple show method in charts
  - #1296 Map_from_screen broken
  - #1305 [docs] `cd sphinx; make html` fails
  - #1522 Tools "help button" issues
  - #1578 Donut charts example not drawing annular lines
  - #1584 Investigate serialization of alpha values
  - #1702 [build] Running bokeh-server in development environment under windows
  - #1705 [docs] Reset doesn't reset box select
  - #1709 [examples] Selection_update stack trace when doing pan/zoom/select ops
  - #1717 [docs] Documentation: wrong title font property name in user guide
  - #1721 [docs] Documentation: user guide describes unsupported axis locations
  - #1723 [bokehjs] Setting plot_{width,height} doesn't work
  - #1738 [docs] [starter] Reference guide formatting issues
  - #1749 [bokehjs] Datatable requires columndatasource to have an `index` field
  - #1753 Make sure sys is available for sys.exit() call on failure
  - #1761 Importing bokeh breaks standard python if ipython also installed
  - #1775 Using bokeh keyword in host url affect config.prefix value
  - #1787 [docs] Autoload script examples out of date
  - #1798 Use_prefix for include not functioning completely correctly
  - #1809 Seems to be some curplot leftover in the codebase
  - #1821 Bokeh ipython magic imports plotting.hold, but plotting.hold is dead
  - #1824 [regression] Bokeh_pretty doesn't have an effect
  - #1835 Enable runs of travisci in branches tagged with xxx.dev[rc].xxxxxxxx form
  - #1837 Fix any caracther in the ruby regex to support the tag containing sha
  - #1838 Hotfix for files encryption
  - #1839 [docs] Fix parameter name: host -> root_url
  - #1840 Fix broken werkzeug import in bokeh-server
  - #1864 Fix charts not working with server
  - #1876 Boxplot chart does not work with iterables of lists
  - #1896 [docs] Fix up docstring table rendering in sphinx
  - #1897 [docs] Make source location in glyphs docstrings be actual links
  - #1902 Feature/server gallery
  - #1904 [examples] Change [x,y]_label to [x,y]label in charts examples
  * features:
  - #380 Add some examples of mplsupport inside ipython notebooks
  - #586 [tests] Add sphinx tutorials to travis
  - #626 [starter] Make radius dimension configurable for circles
  - #749 Adding support for a constrained box zoom
  - #822 [docs] Update docs with architecture diagram
  - #842 [bokehjs] Add axis label formatters (sprintf-style, etc.)
  - #889 Bokeh.plotting.patches line_dash argument only takes a list
  - #987 [starter] Pan and zoom in categorical plots
  - #1091 [bokehjs] Text autocomplete widget
  - #1217 Make bokeh-server gunicorn friendly
  - #1257 Embedding using matplotlib compatibility layer
  - #1281 Scatter doesn't have box zoom
  - #1375 Load bokehjs in a notebook during `import bokeh`
  - #1464 Charts palette should be configurable
  - #1478 [bokehjs] Hoverplot.tooltips should allow html and/or markdown and/or
  - #1515 Restore bokehjs interface
  - #1546 We need to support bokeh[version].[min].js[css] in the cdn to support devel builds
  - #1574 charts should be subclasses of plot
  - #1635 Implement blaze/remote data source to support streaming data in plots
  - #1682 Ajax/json data source
  - #1703 Extending/fixing crossfilter
  - #1730 Being able to hide the axis
  - #1733 Adding horizon high-level chart (clean version)
  - #1734 Bound needs to accept datetime obects
  - #1746 [docs] Add simple inline examples to all or most plotting.py glyph functions
  - #1768 Enable tabbed faceting on crossfilter
  - #1779 Try to only build on master
  - #1780 Negative bar charts
  - #1786 [starter] Vbox/hbox should accept single list as well
  - #1788 Build on travis ideas
  - #1792 Allow grids to shade alternating bands
  - #1795 [bokehjs] Tap+open url
  - #1799 Copy on write
  - #1802 [examples] Add glyphs/linked_tap_server example
  - #1815 Step chart should use line, not segment
  - #1816 [docs] Add bokeh-plot examples to chart docstrings
  - #1823 Add support for bokeh_dev=true python something.py
  - #1858 Feature/multiuser applet support
  - #1862 Hotfix to support local docs with a correct bokehjs
  - #1887 Feature/blaze interface
  * tasks:
  - #906 [docs] Axis and grid needs an update in the user guide
  - #946 [docs] Columndatasource documentation update
  - #1060 [docs] Document that some ar example need scipy + pil to work
  - #1148 [build] Dev build sdists do no carry correct version info
  - #1170 [docs] Need documentation for bokeh server
  - #1503 [bokehjs] Remove unused datafactorrange
  - #1518 [build] Build/release automation improvements.
  - #1540 Some improvements on the devel build
  - #1568 Programmatically upload bokeh js/css to the container
  - #1571 Remove deprecated plotting api
  - #1593 Scatter plot demo with linked density histograms
  - #1656 Plotting.gridplot setting id from name
  - #1687 Release 0.7.1
  - #1688 [docs] Documentation build improvements
  - #1690 [docs] Sphinx autoprops dependency for bokeh models
  - #1692 [docs] Better reported version for deployed dev docs
  - #1694 [docs] Sphinx plot extension directive
  - #1695 Pin scipy
  - #1696 Selection/histogram minor issues
  - #1697 Load_notebook doesn't work with ipython master
  - #1712 [examples] Charts examples should split file/server/notebook
  - #1728 [docs] Timeseries tutorial formatting improvements
  - #1739 Create test matrix script
  - #1743 [docs] Add to doc best use of push_notebook for interact style things, not streaming
  - #1745 Catch ioerror in load_notebook and add logging to the python side
  - #1747 [docs] Document all model attributes
  - #1750 Temporary fix until conda get fixed with python3
  - #1755 Wip fix for conda build
  - #1758 Check apps are in sync with the new api
  - #1765 Task/remove bokeh js
  - #1766 [examples] [tests] Move/rename examples.html
  - #1770 Remove debugging lines
  - #1771 Add doc build to the devel build script
  - #1777 Feature/deploy
  - #1794 [docs] [labels] Add "starter" tag
  - #1813 [docs] Document new charts design
  - #1817 Split chart builders into a sub-package
  - #1818 [tests] Improve/re-org charts tests
  - #1819 Use properties for private models and builders in bokeh.charts
  - #1834 [build] Pin conda-build to get travisci running again
  - #1843 Rename range property to interval
  - #1846 [docs] Add proper docs for properties.py
  - #1860 [docs] Split up dev guide into multiple files
  - #1867 [docs] Clearer docs, new section about installing npm and nodejs
  - #1870 Rename get_data, get_source, prepare_values, draw builders methods
  - #1884 Remove click for dependencies
  - #1885 Axis.hide should have been called axis.visible
  - #1889 Delete click from the conda recipe
  - #1899 [docs] Change docstring example with better data
- Update to 0.7.1:
  * Several bokeh.charts bug fixes and enhancements, such as configurable tools
  * Docs improvements, in particular, documenting json for bokeh.models
  * Mpl compatility improved, now returning the plot object
  * A lot of encoding fixes, including fixes in some of our sample data
  * Faster runs in TravisCI using the new docker-based containerized infrastructure
  * New and improved examples, such as the Interactive Image Processing with Numba and Bokeh notebook
  * bugfixes:
  - #127 Implement proper caching headers and gzip on bokeh.pydata.org
  - #167 It is possible to outrun the resize tool edit
  - #236 Opening a notebook containing embed.js causes typeerror if bokeh-server was restarted
  - #382 Hover tool pops up in odd places in the notebook
  - #520 Let escape reset selections
  - #593 Gridplot breaks layout / overlaps next input cell in ipython notbook
  - #821 Need explicit synchronization for render loop
  - #1265 Handontable rendering issue
  - #1316 Examples/app/stock_applet does not work when embedded
  - #1385 Server/image.py example failing on master
  - #1397 Dropdown tool buttons don't have tooltips and dropdown menus broken
  - #1409 [tests] Tests sometimes fail with `websockettimeoutexception` on travis-ci
  - #1490 Scatter chart auto creates wrong x/y labels
  - #1510 [regression] Hover tool behaviour with multiple renderers
  - #1513 [build] Update tutorial gallery to new plotting.py api
  - #1523 [docs] Gallery thumbs out of sync
  - #1527 Dot chart segment badly renders in some use cases
  - #1529 Donut chart is broken when called with dataframe inputs
  - #1535 [docs] Obsolete returned value in plotting.figure() documentation
  - #1539 Debugjs setting was broken
  - #1545 Grey9 very light with 0.7.0
  - #1551 Donut chart is broken when called with iterables of non float values
  - #1554 Mpl.to_bokeh() should return a handle to the plot
  - #1556 Travis ci failures
  - #1592 Bokehjs unrecoverable errors in notebook
  - #1601 Plotting.save still relies on global state
  - #1605 [regression] Remove 0xa0 characters (and encode source files properly)
  - #1606 $ can get overridden in the notebook
  - #1613 [docs] Corrected typo to fix issue #1612
  - #1621 Charts behaviour when notebook=true and server arguments are specified
  - #1622 Minor selection bugs
  - #1625 Plot.add_tool wrong error message
  - #1627 [regression] Resources(..., minified=false) in bokeh.plotting
  - #1628 Typo fix ``line_with`` -> ``line_width`` in ipython interactive widgets notebook example
  - #1643 Don't request_render() twice during plot initialization
  - #1644 Hovertool with snap_to_data=true fails on some glyphs
  - #1654 Line downsample zoom to fine-level detail results in error on js client
  - #1658 [docs] Fix typo
  - #1660 Pan/zoom being allowed on categorical charts
  - #1679 Slider should accept float stepwise
  * features:
  - #190 Selection architecture
  - #596 Need to support italic+bold font style in textproperties enum
  - #646 [docs] Specifing a parameter without any usage does not result in a warning
  - #696 There should be a way to control order that renderers are drawn
  - #978 Bokeh command line tool
  - #1134 Add_glyph()'s signature should have `glyph` as the first argument
  - #1220 Histogram normalization
  - #1459 Charts should make tools configurable
  - #1484 Add glyphs/sprint example
  - #1489 Authentication refactoring
  - #1507 Odd histogram behaviour
  - #1516 Easy range1d interface
  - #1524 Some matplotlib markers are not handled correctly
  - #1538 [tests] Add charts base tests
  - #1557 Mpl.to_bokeh() should use the same tools found in bokeh.plotting.figure
  - #1567 Use the containerized travisci infrastructure
  - #1629 Charts.gmap class
  - #1636 Gridplot should accept none for empty positions
  - #1657 Add/improve minimal cli features
  - #1663 [docs] [documentation] on embedding
  - #1665 [docs] Embed simple
  * tasks:
  - #1129 [docs] Bokehjs documentation nor source does not mention that it uses jquery and jqueryui
  - #1406 Remove bokeh.{objects,glyphs,widgets}
  - #1471 [tests] Add tests for dataadapter and new charts implementation
  - #1472 Remove bokeh.charts.categoricalheatmap and promote heatmap as only heatmap chart available
  - #1475 Improve bokeh.chart code style and docstrings
  - #1506 Release 0.7.0
  - #1537 Use conda graphviz package
  - #1544 Use more specific type for plot.{left,right,above,below}
  - #1548 [docs] S/dic/dec
  - #1550 [docs] Fixed typo: bojehjs -> bokehjs
  - #1553 [docs] Update readme.md
  - #1575 Don't "fix" singleton array case when expected type is array
  - #1579 [docs] Auto document json for bokeh.models
  - #1580 Provide hooks to easily dump models with all properties
  - #1581 [docs] Write script to integrate all bokeh.models and their json into dev docs
  - #1583 Remove crufty glyph properties
  - #1590 Add missing properties to ticker classes
  - #1593 Scatter plot demo with linked density histograms
  - #1594 Additional kernels for numba examples
  - #1596 Streaming netcat example for bokeh cli tool
  - #1597 Interactive filter using cli tool
  - #1598 Twitter scrapping map demo using cli tool
  - #1600 [docs] Documenting relations between bokeh and yhat/ggplot?
  - #1604 [tests] Add some widget testing and minor fix for object testing
  - #1607 [docs] Update release notes on pydata.org
  - #1608 [docs] Docs build/deploy improvements
  - #1610 [tests] Examples using yahoo's finance data should use a fixed period
  - #1612 Typo in chartobject error message when filename argument is missing
  - #1619 [docs] Fix broken link to quickstart
  - #1661 Small fixes or updates to demos leading to 0.7.1 release
  - #1675 [docs] Misc docs updates leading to 0.7.1 release
- Update to 0.7.0:
  * IPython widgets and animations without a Bokeh server
  * Touch UI working for tools on mobile devices
  * Vastly improved linked data table
  * More new (and improving) bokeh.charts (high level charting interface)
  * Color mappers on the python side
  * Improved toolbar
  * Many new tools: lasso, poly, and point selection, crosshair inspector
  * bugfixes:
  - #598 Hover tool doesn't work with gridplot
  - #616 Less build doesn't properly detect changes
  - #623 Issue with inverted ranges
  - #704 Errow message in windows
  - #798 Embedded notebook style problem
  - #802 Toolbar hidden behind gridplot when wrapped
  - #804 Spaces in file name causes problems when distributing via rdist on unix-like os
  - #808 Cannot style minor ticks
  - #827 Spectrogram app not working: custom.coffee missing
  - #870 Need real solution for mpl plot clone problem
  - #881 Changes script output needs manual intervention
  - #919 Bokeh/examples/glyphs examples broken
  - #926 Legends don't appear on a plot in the order they're given
  - #927 [docs] Bad state on save
  - #936 Remove google maps js from _page_base.html
  - #972 Hover in plots stops working in angularjs upon navigation
  - #983 [docs] Bar chart is not documented
  - #1021 Running stock_app and slider_app fails on reload
  - #1027 [regression] Bokeh 0.5 over 10x slower than 0.4.4
  - #1055 Current setup.py install released js with devel build using pip but not with conda
  - #1062 Cleaning some examples failures
  - #1076 [tests] Mpl 1.4.0 is causing failures in test through the mplexporter
  - #1192 `conda install bokeh` not installing pyzmq
  - #1202 Gridplot() renders new toolbar in a funky way
  - #1245 Wheel zoom not working with chrome
  - #1252 Tool order inconsistent across all examples
  - #1267 Mapoptions json encoding problem
  - #1271 Fix for axis types string comparision (is vs ==)
  - #1287 Sorting/selecting broken in ht example
  - #1293 [regression] Plots with vertical toolbar have extra space above the plot
  - #1295 Make selection geometry available to the python side
  - #1298 Line_color=none not respected
  - #1299 Multiple plots now stack horizontally
  - #1300 Hover tool does not display
  - #1303 Stocks app histograms do no update on selection
  - #1306 Crossfilter filter does not work
  - #1313 'help' button text box sometimes disappears before you can click 'learn more'
  - #1314 Tools don't have a blue underline in notebook and server examples
  - #1319 Bokeh.charts.bar displays overlapping bars
  - #1320 Multiple gmapplot instances on a single document causes errors
  - #1337 Build_palettes.py not python 3 compatable
  - #1338 Bugfix/py3 palettes (closes #1337)
  - #1342 Linked brushing broken in notebook
  - #1343 Gridplot causes javascript error in notebook
  - #1348 Fix gridplots with hover tools
  - #1367 Properly set map div height
  - #1377 Data table not displaying
  - #1378 [docs] Fix spelling: s/embded/embed/
  - #1380 Fix "python setup.py build"
  - #1384 - fixing document merging
  - #1386 [regression] Fixing crossfilter
  - #1400 Hasprops.clone() should use changed_properties_with_values()
  - #1403 [build] Meta.yaml doesn't specify minimal tornado version
  - #1414 Broken server downsample -- property 'type' not found
  - #1415 Server downsample -- pandas error
  - #1417 Fix typo
  - #1422 Strange "nan" string in some mpl plots
  - #1425 Bokeh cdn assets are currently unavailable
  - #1427 Plotting/file/periodic and plotting/file/hover broken on master
  - #1429 Broken examples on master
  - #1431 [windows] Notebooks/animated not working (only on windows) on master
  - #1433 Tools get lost on grid plots
  - #1435 Embed fontawesome's fonts in css (to avoid 404 errors)
  - #1442 [regression] Fix spectrogram issues
  - #1446 Plotting/server/image example broken on master
  - #1461 Some gridplot issues
  - #1466 Abstract rendering -- deserialize on client js not working
  - #1474 Charts markers not showing correctly on legend
  - #1485 More specific css - otherwise when bokeh plots are embedded inside list
  - #1496 Fix unitialized var usage in bokeh.index
  - #1500 Fix charts not working with server output
  * features:
  - #72 Mechanism to express color mappings to bokehjs
  - #144 Add an example with multiple axes
  - #543 Websockets refactoring
  - #546 Plotting.show for server session should just show a single object
  - #547 Don't include gmaps api script in templates
  - #683 Remove pandasdatasource
  - #693 Examples/app/applet should use bokeh.sampledata
  - #761 [docs] Hard to find example notebooks
  - #774 Modify build_and_install.sh to handle release candidates
  - #849 We need a tools refactor
  - #863 Allow plot frame/tools to be configurable
  - #911 Rewrite spectrogram demo to use mostly python
  - #918 Multiple axis exposed on the python side
  - #1198 Abstract rendering: version check
  - #1225 Replace glyphspecs with the properties system
  - #1240 Support for geojs maps
  - #1273 Feature/geojs
  - #1285 Single axis zoom
  - #1294 Feature/more tools
  - #1309 Passing iterables straight to bokeh.charts (histogram)
  - #1321 Small tweaks to the coffeescript
  - #1327 Add 'help' to properties
  - #1345 Refactor plotting interface
  - #1351 Allow to specify alternative types for properties
  - #1359 Cleanup of table widgets
  - #1368 Add option (maybe default?) for bokeh logo to be de-saturated and placed on the rhs of the toolbar
  - #1372 More systematic approach to tool validation
  - #1374 Feature/server startup cleanup
  - #1392 Support subtyping for view models
  - #1411 Update examples to use new plotting api
  - #1437 Need methods to clear docs
  - #1451 Add glyphs/calendars example
  - #1488 Method to update data source contents in the notebook
  * tasks:
  - #836 Dev packages should be available at least for linux-64 and osx
  - #862 Remove data files in bokeh/tests
  - #880 Credentials for the release
  - #907 Rename widgetobjects.py
  - #909 Simplify dataspecs
  - #950 [docs] Update quickstart/bokeh.js build instructions
  - #999 Migration to bokeh organization
  - #1004 Change setup.py - building js
  - #1243 Clicking buttons in plots embedded in forms triggers form submit
  - #1250 Add more properties to handsontable, e.g. {row,column}_resize
  - #1251 Tools hidden by default in plotting/server/elements.py
  - #1253 Release 0.6.1
  - #1261 [docs] Add info about sample data download to user guide and faq
  - #1310 Rename glyph-> glyphrenderer and baseglyph -> glyph
  - #1311 Introduce bokeh.api module
  - #1325 Set {np.}random.seed(1) in examples/test
  - #1330 Reduce weight of gallery images
  - #1333 [docs] Dvreed77/palette docs
  - #1336 Hotfix for problem with pandas 0.15
  - #1353 Remove 'type' property from guides
  - #1357 Add missing icon files
  - #1364 Replace continuumio organization with bokeh and remove kinectjs
  - #1370 Removing gevent
  - #1371 Remove objectexplorer
  - #1382 Improve implementation of slickgrid-based datatable
  - #1389 Remove unused ar views, inherit from hasproperties instead of hasparent
  - #1391 [docs] Improve documentation: make it easier for users to get started
  - #1401 Hotfix/figure subclass of plot
  - #1407 Deprecate bokeh.{objects,glyphs,widgets}
  - #1408 [docs] Add contributing guidelines
  - #1418 [tests] Increase socket timeout
  - #1424 [tests] More unit tests
  - #1436 [BEP] [docs] Conventions for tying issues and prs
  - #1458 Try to recover the slideshow example featuring the embed api
  - #1465 Task/examples
  - #1473 [docs] Document new bokeh.chart implementation
  - #1498 [BEP] [docs] Add bep 0 with meta-information about bep process
  - #1499 [docs] Add deprecations to glyph funcs on document
  - #1504 Documentation updates for release 0.7
* Wed Oct 15 2014 toddrme2178@gmail.com
- Update to 0.6.1
  * Toolbar enhancements
  * bokeh-server fixes
  * Improved documentation
  * Button widgets
  * Google map support in the Python side
  * Code cleanup in the JS side and examples
  * New examples
- Update to 0.6.0
  * Abstract Rendering recipes for large data sets:
    isocontour, heatmap, hdalpha
  * Improved, configurable tool bar for plots
  * Full Python 3 support for bokeh-server
  * Much expanded User Guide
  * Support for multiple axes
  * Plot object graph query interface
  * New charts in bokeh.charts: TimeSeries and Categorical HeatMap
  * Hit-testing for patch glyphs
* Fri Aug 29 2014 toddrme2178@gmail.com
- Initial version
