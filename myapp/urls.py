from django.urls import path

from myapp import views

urlpatterns=[



    path('login/',views.login),
    path('login_post/',views.login_post),

    path('admin_home/',views.admin_home),


    path('charge_add/',views.add_charge),
    path('add_charge_post/',views.add_charge_post),


    path('edit_charge/<int:id>',views.edit_charge),
    path('edit_charge_post/',views.edit_charge_post),

    path('delete/<int:id>',views.delete,name='delete'),



    path('charge_view/',views.view_charges),
    path('view_charges_post/',views.view_charges_post),

    path('add_officers/',views.add_depo_officer),
    path('add_depo_officer_post/',views.add_depo_officer_post),

    path('view_users/',views.view_users),
    path('view_users_post/',views.view_users_post),

    path('View_DepoOfficers/',views.view_officers_verify),
    path('view_officers_verify_post/',views.view_officers_verify_post),

    path('Edit_DepoOfficers/<id>',views.Edit_DepoOfficers),
    path('edit_officers_post/',views.edit_officers_post),

    path('delete_officers/<id>',views.delete_officers),

    path('view_complaint/', views.view_complaints),
    path('view_complaint_post/',views.view_complaints_post),

    path('send_reply/<id>',views.send_reply),
    path('send_reply_post/',views.send_reply_post),

    path('Change_pass_admin/',views.Change_pass_admin),
    path('Change_pass_admin_post/',views.Change_pass_admin_post),

####################################################################

    path('depo_officer_home/',views.depo_officer_home),

    path('view_profile_depo/',views.view_profile_depo),


    path('view_pass_request/', views.view_pass_request),
    path('view_pass_request_post/',views.view_pass_request_post),

    path('approve_pass_req/<id>',views.approve_pass_req),
    path('reject_pass_req/<id>',views.reject_pass_req),

    path('view_approved_pass/', views.view_approved_pass),
    path('view_approved_pass_post/',views.view_approved_pass_post),

    path('view_rejected_pass/', views.view_rejected_pass),
    path('view_rejected_do_post/',views.view_rejected_do_post),

    path('update_pass/', views.update_pass),
    path('update_pass_post/',views.update_pass_post),

    path('view_prev_pass/<id>',views.view_prev_pass),

    path('update_pass_date/<id>',views.update_pass_date),
    path('update_pass_date_post/',views.update_pass_date_post),

    path('view_payments_do/', views.view_payments_do),
    path('view_payments_do_post/',views.view_payments_do_post),

    path('view_cancel_req/',views.view_cancel_req),
    path('view_cancel_req_post/', views.view_cancel_req_post),

    path('approve_cancel_req/<id>',views.approve_cancel_req),
    path('delete_approved_cancel_request/<id>',views.delete_approved_cancel_request),

    path('Change_pass_officer/',views.Change_pass_officer),
    path('Change_pass_officer_post/',views.Change_pass_officer_post),


    ######################################################################

    path('user_ui/',views.user_ui),
    path('user_ui_post/',views.user_ui_post),

    path('view_user_profile/',views.view_user_profile),

    path('edit_user_profile/',views.edit_user_profile),
    path('edit_user_profile_post/',views.edit_user_profile_post),

    path('view_DepoOfficer/', views.view_officers),
    path('view_officers_post/',views.view_officers_post),

    path('pass_request/<did>',views.pass_request),
    path('pass_request_post/',views.pass_request_post),
    path('calculate/',views.calculate),
    path('calculate2/',views.calculate2),
    path('edit_user_profile_post/',views.edit_user_profile_post),

    path('view_existing_pass/', views.view_existing_pass),

    path('renew_pass/<id>', views.renew_pass),
    path('renew_pass_post/',views.renew_pass_post),

    path('cancel_pass/<pid>',views.cancel_pass),
    path('cancel_pass_post/',views.cancel_pass_post),

    path('view_approved_cancel/',views.view_approved_cancel),
    path('view_approved_cancel_post/',views.view_approved_cancel_post),

    path('payment/<pid>/<amnt>',views.payments),
    path('payments_post/',views.payments_post),



    path('view_status_download/', views.view_status),
    path('renew_status/',views.renew_status),
    path('cancel_status/',views.cancel_status),



    path('complaint/',views.complaint),
    path('complaint_post/',views.complaint_post),

    path('view_reply/',views.view_reply),
    path('view_reply_post/',views.view_reply_post),

    path('user_home/',views.user_home),

    path('user_change_pswd/',views.user_change_pswd),
    path('user_change_pswd_post/',views.user_change_pswd_post),

    path('user_view_charges/',views.user_view_charges),
    path('user_view_charges_post/',views.user_view_charges_post),

    path('forget_pass/',views.forget_pass),
    path('forget_pass_post/',views.forget_pass_post),

    path('logout/',views.logout),

]
