use std::{collections::HashMap, time::Instant};

use sha256::digest;
use num::{BigInt, Num, ToPrimitive};

fn main() {
    let start = Instant::now();
    let mut hashes: HashMap<u128, String> = HashMap::new();

    let mut i = 0;
    loop {
        let inp1 = i.to_string();
        let input = format!("{}{}", "GIFFEL-", inp1);
        let hash = digest(&input);
        let modded = BigInt::from_str_radix(&hash, 16);
        let res =  match modded {
            Ok(a) => a >> 203,
            Err(_) => BigInt::ZERO
        };

        let res = BigInt::to_u128(&res).unwrap();

        if res != 0 && hashes.contains_key(&res) {
            println!("Found collision!");
            println!("{}", input);
            println!("{}", format!("{}{}", "GIFFEL-", hashes.get(&res).unwrap()));
            println!("Time taken: {} seconds.", (Instant::now() - start).as_secs());
            break
        }

        hashes.insert(res, inp1);
        if i & 0xFFFFFF == 0 {
            println!("{}", i);
        }
        i += 1;
    }
}
