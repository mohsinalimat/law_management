from . import __version__ as app_version

app_name = "law_management"
app_title = "Law Management"
app_publisher = "Solufy"
app_description = "Manage lawyers, clients, matters(cases), trials and its invoicing"
app_email = "contact@solufy.in"
app_license = "MIT"

# Includes in <head>
# ------------------

fixtures = [{
	"doctype": "Workflow",
		"filters": {
			"name": [ "in", ["Matter", "Client Request"] ]
			}
		},
	{
	"doctype": "Workflow State"
    },
	]


# include js, css files in header of desk.html
# app_include_css = "/assets/law_management/css/law_management.css"
# app_include_js = "/assets/law_management/js/law_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/law_management/css/law_management.css"
# web_include_js = "/assets/law_management/js/law_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "law_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}


# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "law_management.utils.jinja_methods",
#	"filters": "law_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "law_management.install.before_install"
# after_install = "law_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "law_management.uninstall.before_uninstall"
# after_uninstall = "law_management.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "law_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }


doc_events = {
    'Client Request': {
        'validate': [
            'law_management.law_management.doctype.client_request.client_request.validate'
        ],
  	},
  	'Matter': {
        'validate': [
            'law_management.law_management.doctype.matter.matter.validate'
        ],
  	},
};

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"law_management.tasks.all"
#	],
#	"daily": [
#		"law_management.tasks.daily"
#	],
#	"hourly": [
#		"law_management.tasks.hourly"
#	],
#	"weekly": [
#		"law_management.tasks.weekly"
#	],
#	"monthly": [
#		"law_management.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "law_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "law_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "law_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"law_management.auth.validate"
# ]
