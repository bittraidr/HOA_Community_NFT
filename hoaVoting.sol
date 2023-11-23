pragma solidity ^0.5.0;
// read in pragma for solidity contract

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
// import token dependencies

contract PolicyFactory is ERC20, ERC20Detailed, ERC20Mintable{
    mapping(address=>uint) public _currently_owned_count;
    mapping(string=>uint) public optionId;
    PropertyNFT public property_contract;
    address[] public _unique_owners;

    constructor(PropertyNFT _property_contract, string memory policy_name, string memory policy_id) ERC20Detailed(policy_name, policy_id,18) public {
        // property_contract=_property_contract;
        property_contract=PropertyNFT(_property_contract);
        _unique_owners=property_contract.view_unique_owners();

        for (uint256 i; i<_unique_owners.length; i++) {
            _currently_owned_count[_unique_owners[i]]=property_contract.currently_owned_count(_unique_owners[i]);
        }

        for (uint256 i; i<_unique_owners.length; i++) {
            _mint(_unique_owners[i], _currently_owned_count[_unique_owners[i]]);
        }
    }

    
    function vote(string memory option) public  {
        require(balanceOf(msg.sender)>0, "Sorry, you cannot vote right now!");
        optionId[option] += balanceOf(msg.sender);
        _burn(msg.sender, balanceOf(msg.sender));
    }
}


contract PropertyNFT is ERC721Full {
    // create contract to create property owner's NFTs

    constructor() public ERC721Full("Property", "PROP") {}
    // Create a constructor for the property NFTs and have the contract inherit the libraries imported from OpenZeppelin.

    struct property {
    // create property structure
        string propertyAddress;
        // variable for properties physical address
        string neighborhood;
        // variable to assign properties to unique neighborhood ids
    }

    mapping(uint256=>property) public hoaPortfolio;
    // address is to property owner
    
    mapping(address=>uint) public currently_owned_count; // investigate if this is redundant with balances
    // {address: uint}, i.e. {0x0000000: 1}

    // create array for unique owner list
    address[] public unique_owners;
    // [0x0000000, 0x00000001, 0x000002]

    function view_unique_owners() public view returns(address[] memory){
        return unique_owners;
    } 

    function get_currently_owned_count(address owner_address) public view returns(uint) {
        return currently_owned_count[owner_address];
    }

    function remove_owner_from_list(address owner_address) public {
        if (currently_owned_count[owner_address]==0){
            for (uint256 i; i<unique_owners.length; i++) {
                if (unique_owners[i] == owner_address) {
                    unique_owners[i] = unique_owners[unique_owners.length - 1];
                    unique_owners.pop();
                    break;
                }
            }
        } 
    }

    function registerProperty(
    // allows for the authenitication and asignment of new properties for voting purposes
        address propertyOwner, 
        string memory propertyAddress,
        string memory neighborhood, 
        string memory propURI
        ) public returns(uint256) {
        // read in property owner, property address, and property URI variables
        uint256 propId = totalSupply();
        // generate new property id

        // check if first time - if yes, then add to unique owners list
        if (currently_owned_count[propertyOwner]==0){
            unique_owners.push(propertyOwner);
        }

        _mint(propertyOwner, propId);
        // mint property to owner's wallet
        _setTokenURI(propId, propURI);
        // map property URI to property id

        hoaPortfolio[propId] = property(propertyAddress, neighborhood);

        currently_owned_count[propertyOwner]+=1;
        // map property information to property owners address

        return propId;
        // return the property id
    }
}

// deployer: 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4
// propertyNFT_address: 0xd9145CCE52D386f254917e481eB44e9943F39138
// PolicyFactory_address: 0x4815A8Ba613a3eB21A920739dE4cA7C439c7e1b1

// user_1: 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2
// user_2: 0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db