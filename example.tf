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

module "75devendra_sahu_gmail_com" {
   source = "./modules/user"

   email_address     = "75devendra.sahu@gmail.com"
   first_name        = "75devendra"
   last_name         = "Sahu"
   bmw_department    = "DE-47"
   bmw_employee_type = "gmail"
   github_username   = "75devendraSahu"
   ad_invite         = true
 }

