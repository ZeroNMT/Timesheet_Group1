{
    'name': 'Timesheet Jira',
    'depends': [
        'web_grid',
        'hr_timesheet'
    ],
    'author': 'Group1',
    'data': [
        'security/ir.model.access.csv',
        'views/timesheet_views.xml',
        'views/timesheet_menu.xml',

    ],
    'application': True,

}
