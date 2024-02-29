module "sebastian_N_schuetz_partner_bmw_de" {
   source = "./modules/user"

   email_address     = "sebastian.n.schuetz@partner.bmw.de"
   first_name        = "Sebastian"
   last_name         = "Schuetz"
   bmw_department    = "EE-81"
   bmw_employee_type = "external"
   github_username   = "SebastianNSchuetz"
   ad_invite         = true
 }
