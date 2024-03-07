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

module "sumit_agrawal_partner_bmw_de" {
   source = "./modules/user"

   email_address     = "Sumit.agrawal@partner.bmw.de"
   first_name        = "Sumit"
   last_name         = "Agrawal"
   bmw_department    = "DE-47"
   bmw_employee_type = "external"
   github_username   = "SumitAgrawal"
   ad_invite         = true
 }

