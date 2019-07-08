{
    'name': "Jira's Timesheet",
    'depends': [
        'web_grid',
        'hr_timesheet'
    ],
    'author': 'Group1',
    'data': [
        'security/ir.model.access.csv',
        'views/timesheet_trigger.xml',
        'views/assets.xml',
        'views/timesheet_views.xml',
        'views/timesheet_menu.xml',
        'wizard/edit_task.xml',
        'wizard/update_task.xml',
    ],
    'qweb': ['static/src/xml/grid_view.xml'],
    'application': True,

}
